import sys
import mysql.connector

#SQL connection credentials
mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin123',
        port='3306',
        database='animedb'
    )
mycursor = mydb.cursor()