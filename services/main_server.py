# TODO: change file name
import psycopg2

from db_postgres import get_db_connection, release_db_connection
from services.logger import log_info, log_error


def select_all_with_psycopg2(request_info):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        query = "SELECT * FROM test"
        log_info(f"{request_info}. executing query: {query}")
        cur.execute(query)
        result = cur.fetchall()
        return result
    except psycopg2.Error as e:
        log_error(f"{request_info}. Error: {e}")
        print(f'Error is: {e}')
    finally:
        release_db_connection(conn)