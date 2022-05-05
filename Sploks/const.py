import mysql.connector

# TODO: Replace "..." with your own SQL config
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dengesvd1993",
    database="sploks",
    auth_plugin='mysql_native_password'
)