import psycopg2
import os

def db_connection():
    connection = psycopg2.connect(os.environ.get("DATABASE_URL"))
    return connection

#print(db_connection)