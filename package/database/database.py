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

        query = "SELECT * FROM namegen.parts;"   
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
                self.cur.executescript(sql_as_string)
        finally:
            if self.conn is not None:
                self.conn.close()

        self.disconnect()

    def get_col_part_if_exists(self, part, category, collection):
        self.connect()

        col_part_if_exists = """SELECT part_id, col_id FROM namegen.collection_parts
                                JOIN namegen.collections USING(col_id)
                                JOIN namegen.parts USING(part_id)
                                WHERE part = %s
                                  AND category = %s
                                  AND collection = %s;"""
       
        self.cur.execute(col_part_if_exists, (part, category, collection,))
        
        result = self.cur.fetchone()
        self.disconnect()
        return result

    def add_part_to_collection(self, part, category, collection):
        self.connect()

        check_if_exists = """SELECT part_id, col_id FROM namegen.collection_parts
                             """

        add_part_to_col = """INSERT INTO namegen.parts (col_id, part_id)
                              SELECT %s, %s
                              WHERE NOT EXISTS (
                                  SELECT 1 FROM namegen.collection_parts
                                  JOIN 
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
                self.cur.executescript(sql_as_string)
        finally:
            if self.conn is not None:
                self.conn.close()

        self.disconnect()