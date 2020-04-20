import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None
def create_table(conn, table, column):
    cursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS {} ({}) ".format(table, column)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        conn.commit()
        print("A Table created successfully")

def select_rows(conn, table, condition, order_by, fetchall):
    cursor = conn.cursor()
    query = "SELECT * FROM {} ".format(table)
    if condition is not None:
        query += "WHERE {}".format(condition)
    if order_by is not None:
        query += "ORDER BY {}".format(order_by)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        if fetchall == True:
            return cursor.fetchall()
        else:
            return cursor.fetchone()

def num_rows(conn, table, condition):
    cursor = conn.cursor()
    query = "SELECT * FROM {} ".format(table)
    if condition is not None:
        query += "WHERE {}".format(condition)
    try:
        cursor.execute(query)
        return len(cursor.fetchall())
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))

def insert_row(conn, table, column, value):
    cursor = conn.cursor()
    query = "INSERT INTO {} ({}) VALUES ({}) ".format(table, column, value)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        conn.commit()
        print("A row has been inserted successfully")

def update_row(conn, table, column, condition=None):
    cursor = conn.cursor()
    query = 'UPDATE {} SET {} ' .format(table,column)
    if condition is not None:
        query+='WHERE {}'.format(condition)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        conn.commit()
        print("A row has been updated successfully")
def delete_row(conn, table, condition):
    cursor = conn.cursor()
    query = 'DELETE FROM {} WHERE {}'.format(table, condition)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        conn.commit()
        print("A row has been deleted successfully")
def delete_table(conn, table):
    cursor = conn.cursor()
    query = 'DROP TABLE {}'.format(table)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        conn.commit()
