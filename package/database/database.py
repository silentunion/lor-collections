import os
import psycopg2
import json

__location__ = os.path.realpath(
os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'config.json')) as f:
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

    def get_projects(self, view):
        self.connect()

        items = vd[view]['columns']
        query = vd[view]['query']   
        self.cur.execute(query)
        records = self.cur.fetchall()

        self.disconnect()
        return records, items

    def input_project(self, project_num, project_name, phase_num, client):
        self.connect()


        query_project = """INSERT INTO aco.projects (project_num, project_name, client)
                        VALUES (%s, %s, %s) RETURNING project_id;"""

        query_phase = """INSERT INTO aco.projectphases (project_id, phase_num, status_project)
                        VALUES (%s, 1, 'Proposed');"""

        project_id = None

        try:
            self.cur.execute(query_project, (project_num, project_name, client,))
            project_id = self.cur.fetchone()[0]
            self.conn.commit()
            self.cur.execute(query_phase, (project_id,))
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            sql_file = open("sql/maintenance/sequence_resets.sql")
            sql_as_string = sql_file.read()
            cur.executescript(sql_as_string)
        finally:
            if self.conn is not None:
                self.conn.close()

        self.disconnect()

    def update_field(self, column, old_info, new_info, project_id):
        self.connect()

        table = cd[column]['table']
        column_type = cd[column]['type']

        if column_type == 'num':
            query = f"""UPDATE {table}
                        SET {column} = {int(new_info)}
                        WHERE project_id = {int(project_id)};"""
        else:
            query = f"""UPDATE {table}
                        SET {column} = '{new_info}'
                        WHERE project_id = {int(project_id)};"""

        # print(query)

        try:
            self.cur.execute(query)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

        self.disconnect()


def get_projects():
    conn = psycopg2.connect(
        user=config['PGUSER'], 
        password=config['PGPASSWORD'],
        host=config['PGHOST'],
        port=config['PGPORT'],
        database=config['PGDATABASE'])
    cur = conn.cursor()

    query = "SELECT project_num, project_name FROM projects;"   
    cur.execute(query)
    records = cur.fetchall()     

    cur.close()
    conn.close()

    return records

def input_project(project_num, project_name):
    conn = psycopg2.connect(
        user=config['PGUSER'], 
        password=config['PGPASSWORD'],
        host=config['PGHOST'],
        port=config['PGPORT'],
        database=config['PGDATABASE'])
    cur = conn.cursor()


    query_project = """INSERT INTO projects (project_num, project_name)
                    VALUES (%s, %s) RETURNING project_id;"""

    query_phase = """INSERT INTO phases (project_id, phase_num)
                    VALUES (%s, 1);"""

    project_id = None

    try:
        cur.execute(query_project, (project_num, project_name,))
        project_id = cur.fetchone()[0]
        conn.commit()
        cur.execute(query_phase, (project_id,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    cur.close()
    conn.close()

# input_project('20-4102', 'Treeville')