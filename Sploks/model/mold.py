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


def updateOne(table, field, values, params=" "):
    try:
        query = f"UPDATE {table} SET {field}='{values}' {params}"
        cur.execute(query)
        con.commit()
    except mysql.connector.Error as sqlError:
        print(sqlError)
    except:
        "Unknown error"
