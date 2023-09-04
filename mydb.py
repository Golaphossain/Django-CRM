import mysql.connector
database=mysql.connector.connect(
    host='localhost',
    user='root',
    password='golap123'
)
#prepare a cursor object
cursorObject=database.cursor()
# create database
cursorObject.execute("CREATE DATABASE crmproject")
print("All done!")