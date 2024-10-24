import pymysql
import pymysql.cursors
from flask import g


def get_db():
    if 'db' not in g or not is_connection_open(g.db):
        print("Re-establishing closed database connection.")
        g.db = pymysql.connect(
            # Database configuration
            # Configure MySQL
            host = 'thh2lzgakldp794r.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            user = 'wttfe8xvz9drzwmx',
            password = 'nqwredy849iyplfv',
            database = 'h4yqzjc11nj0p562',
            cursorclass=pymysql.cursors.DictCursor  # Set the default cursor class to DictCursor
        )
    return g.db

def is_connection_open(conn):
    try:
        conn.ping(reconnect=True)  # PyMySQL's way to check connection health
        return True
    except:
        return False

def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None and not db._closed:
        print("Closing database connection.")
        db.close()



