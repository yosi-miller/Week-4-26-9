import psycopg2

from db_postgres import get_db_connection, release_db_connection
from services.logger import log_info, log_error


def select_all_operations(request_info=None):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        query = "SELECT * FROM operations"

        log_info(f"{request_info}. executing query: {query}")
        cur.execute(query)
        result = cur.fetchall()
        return result
    except psycopg2.Error as e:
        log_error(f"{request_info}. Error: {e}")
        print(f'Error is: {e}')
    finally:
        release_db_connection(conn)


def create_tables(request_info=None):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        query1 = """CREATE TABLE target_country
                            (
                                id SERIAL PRIMARY KEY,
                                name CHAR(50)
                            )"""
        log_info(f"{request_info}. executing query: {query1}")
        cur.execute(query1)

        query2 = """CREATE TABLE target(
            id SERIAL PRIMARY KEY,
            country_id INT REFERENCES target_country(id),
            mission_date DATE,
            city CHAR(20),
            target_priority CHAR(20),
            target_latitude CHAR(20),
            target_longitude CHAR(20)
            )"""

        log_info(f"{request_info}. executing query: {query2}")
        cur.execute(query2)

        query3 = """
                CREATE TABLE attack_mission(
                id SERIAL PRIMARY KEY,
                target_id INT REFERENCES target(id),
                mission_date DATE
                );      
                """
        log_info(f"{request_info}. executing query: {query3}")
        cur.execute(query3)
        conn.commit()
        return True
    except psycopg2.Error as e:
        log_error(f"{request_info}. Error: {e}")
        print(f'Error is: {e}')
        return False
    finally:
        release_db_connection(conn)

def insert_target_country(request_info=None):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        query = 'SELECT DISTINCT "Target Country" FROM operations WHERE "Target Country" IS NOT NULL'
        log_info(f"{request_info}. executing query: {query}")
        cur.execute(query)
        result = cur.fetchall()
        for i in result:
            cur.execute("""INSERT INTO target_country (name) VALUES (%s)""", (i[0],))
        conn.commit()
        return result
    except psycopg2.Error as e:
        log_error(f"{request_info}. Error: {e}")
        print(f'Error is: {e}')
    finally:
        release_db_connection(conn)

def insert_target(request_info=None):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        query = """
            SELECT "Target Country", "Mission Date", "Target City", "Target Priority", "Target Latitude", "Target Longitude"
            FROM operations
            WHERE "Target Country" IS NOT NULL
            """
        log_info(f"{request_info}. executing query: {query}")
        cur.execute(query)
        result = cur.fetchall()
        for i in result:
            find_country_id = f'SELECT id FROM target_country WHERE target_country.name = %s'
            cur.execute(find_country_id, (i[0],))
            find_result = cur.fetchall()
            print(find_result)
            cur.execute("""INSERT INTO target (
                            country_id,
                            mission_date,
                            city,
                            target_priority,
                            target_latitude,
                            target_longitude)
                            VALUES (%s, %s, %s, %s, %s, %s)""", (find_result[0][0], i[1], i[2], i[3], i[4], i[5]))
        conn.commit()
        return result
    except psycopg2.Error as e:
        log_error(f"{request_info}. Error: {e}")
        print(f'Error is: {e}')
    finally:
        release_db_connection(conn)


if __name__ == "__main__":
    # result = select_all_operations()
    # for i in range(10):
    #     print(result[i])
    # print(create_tables())
    # print(insert_target_country())
    print(insert_target())