import psycopg2
from psycopg2 import pool
import os
from dotenv import load_dotenv

load_dotenv()

connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dbname="wwii_missions",
            user=os.getenv('POSTGRES_USER_NAME'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host="localhost",
            port="5432"
        )

def get_db_connection():
    if connection_pool:
        conn = connection_pool.getconn()
        return conn

def release_db_connection(conn):
    connection_pool.putconn(conn)