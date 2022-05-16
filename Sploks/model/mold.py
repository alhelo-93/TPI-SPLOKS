import mysql
from const import *
from const import con

cur = con.cursor()


def selectOneWithParams(columns, table, params):
    try:
        cur = con.cursor(dictionary=True)
        query = f"SELECT {columns} FROM {table} {params} Order by {table}.id"
        cur.execute(query)
        return cur.fetchone()
    except mysql.connector.Error as sqlError:
        print(sqlError)
    except:
        "Unknown error"


def selectWithParams(columns, table, params=""):
    try:
        query = f"SELECT {columns} FROM {table} {params} Order by {table}.id"
        cur.execute(query)
        return cur.fetchall()
    except mysql.connector.Error as sqlError:
        print(sqlError)
    except:
        "Unknown error"


def selectWithParamsgroupby(columns, table, params=""):
    try:
        query = f"SELECT {columns} FROM {table} {params} GROUP by {table}.id"
        cur.execute(query)
        return cur.fetchall()
    except mysql.connector.Error as sqlError:
        print(sqlError)
    except:
        "Unknown error"


def updateOneField(table, field, values, params=" "):
    try:
        query = f"UPDATE {table} SET {field}='{values}' {params}"
        cur.execute(query)
        con.commit()
        return True
    except mysql.connector.Error as sqlError:
        print(sqlError)
        return False
    except:
        "Unknown error"


def updateOne(table, values, params=""):
    """
    Update a table in the database

    :param table: The name of the table to update
    :param values: The values to be updated
    :param params: The WHERE clause
    """
    try:
        query = f"UPDATE {table} SET {values} {params}"
        cur.execute(query)
        con.commit()
    except mysql.connector.Error as sqlError:
        print(sqlError)
    except:
        "Unknown error"


def createOne(table, columns, values):
    """
    Create a new row in a table

    :param table: The name of the table you want to insert into
    :param columns: The columns to insert into
    :param values: The values to insert into the table
    :return: The last row id of the table.
    """
    try:
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"

        cur.execute(query)
        con.commit()
        return cur.getlastrowid()
    except mysql.connector.Error as sqlError:
        print(sqlError)
    except:
        "Unknown error"
