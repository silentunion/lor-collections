import os
from os.path import basename
from pathlib import Path
import psycopg2
import json

base_path = Path(__file__).parent
config_path = base_path / 'config.json'

with open(config_path) as f:
    config = json.load(f)


class LORConnect():
    def connect(self):
        self.conn = psycopg2.connect(
            user=config['PGUSER'], 
            password=config['PGPASSWORD'],
            host=config['PGHOST'],
            port=config['PGPORT'],
            database=config['PGDATABASE'])
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.cur.close()
        self.conn.close()

    def get_parts(self):
        self.connect()

        query = """SELECT * FROM namegen.parts
                   JOIN namegen.collection_parts USING(part_id)
                   JOIN namegen.collections USING(col_id)
                   JOIN namegen.part_properties USING(cp_id)
                   JOIN namegen.properties USING(prop_id);"""   
        self.cur.execute(query)
        records = self.cur.fetchall() 

        self.disconnect()
        print(records)
        

    def insert_part(self, part, category):
        self.connect()

        insert_part = """INSERT INTO namegen.parts (part, category)
                            SELECT %s, %s
                            WHERE NOT EXISTS (SELECT 1 FROM namegen.parts
                                              WHERE part = %s
                                                AND category = %s);"""
       
        try:
            self.cur.execute(insert_part, (part, category, part, category,))
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            sql_file_path = base_path / 'sql' / 'maintenance' / 'serial_resets.sql'
            with open(sql_file_path) as sql_file:
                sql_as_string = sql_file.read()
            self.cur.execute(sql_as_string)
        finally:
            if self.conn is not None:
                self.conn.close()

        self.disconnect()

    def get_part_id_if_exists(self, part, category):
        self.connect()

        part_id_if_exists = """SELECT part_id FROM namegen.parts
                                WHERE part = %s
                                  AND category = %s;"""
       
        self.cur.execute(part_id_if_exists, (part, category,))
        result = self.cur.fetchone()
        self.disconnect()
        return result

    def get_col_id_if_exists(self, collection):
        self.connect()

        col_id_if_exists = """SELECT col_id FROM namegen.collections
                                WHERE collection = %s;"""
       
        self.cur.execute(col_id_if_exists, (collection,))
        result = self.cur.fetchone()
        self.disconnect()
        return result

    def get_prop_id_if_exists(self, prop):
        self.connect()

        prop_id_if_exists = """SELECT prop_id FROM namegen.properties
                                WHERE property = %s;"""
       
        self.cur.execute(prop_id_if_exists, (prop,))
        result = self.cur.fetchone()
        self.disconnect()
        return result

    def get_cp_id_if_exists(self, part, category, collection):
        self.connect()

        cp_id_if_exists = """SELECT cp_id FROM namegen.collection_parts
                                JOIN namegen.collections USING(col_id)
                                JOIN namegen.parts USING(part_id)
                                WHERE part = %s
                                  AND category = %s
                                  AND collection = %s;"""
       
        self.cur.execute(cp_id_if_exists, (part, category, collection,))
        result = self.cur.fetchone()
        self.disconnect()
        return result

    def get_pp_id_if_exists(self, part, category, collection, prop):
        self.connect()

        pp_id_if_exists = """SELECT pp_id FROM namegen.part_properties
                                JOIN namegen.properties USING(prop_id)
                                JOIN namegen.collection_parts USING(cp_id)
                                JOIN namegen.collections USINg(col_id)
                                JOIN namegen.parts USING(part_id)
                                WHERE part = %s
                                  AND category = %s
                                  AND collection = %s
                                  AND property = %s;"""
       
        self.cur.execute(pp_id_if_exists, (part, category, collection, prop,))
        result = self.cur.fetchone()
        self.disconnect()
        return result

    def add_part_to_collection(self, part, category, collection):
        if self.get_cp_id_if_exists(part, category, collection) is None:
            part_id = self.get_part_id_if_exists(part, category)
            col_id = self.get_col_id_if_exists(collection)
            print('part_id: ', part_id)
            print('col_id: ', col_id)

            self.connect()

            add_part_to_col = """INSERT INTO namegen.collection_parts (col_id, part_id)
                                 VALUES (%s, %s);"""
        
            try:
                self.cur.execute(add_part_to_col, (col_id, part_id,))
                self.conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                sql_file_path = base_path / 'sql' / 'maintenance' / 'serial_resets.sql'
                with open(sql_file_path) as sql_file:
                    sql_as_string = sql_file.read()
                self.cur.execute(sql_as_string)
            finally:
                if self.conn is not None:
                    self.conn.close()

            self.disconnect()

    def add_prop_to_part(self, part, category, collection, prop):
        if self.get_pp_id_if_exists(part, category, collection, prop) is None:
            cp_id = self.get_cp_id_if_exists(part, category, collection)
            prop_id = self.get_prop_id_if_exists(prop)

            self.connect()

            add_prop_to_part = """INSERT INTO namegen.part_properties (cp_id, prop_id)
                                 VALUES (%s, %s);"""
        
            try:
                self.cur.execute(add_prop_to_part, (cp_id, prop_id,))
                self.conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                sql_file_path = base_path / 'sql' / 'maintenance' / 'serial_resets.sql'
                with open(sql_file_path) as sql_file:
                    sql_as_string = sql_file.read()
                self.cur.execute(sql_as_string)
            finally:
                if self.conn is not None:
                    self.conn.close()

            self.disconnect()