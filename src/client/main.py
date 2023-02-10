#!/bin/python3
import mariadb as connector
import pandas

# MariaDB configuration
sqlhost = "Ark-Pi"
sqluser = "client"
sqlpasswd = "guest"
cnx = connector.connect(
    user=sqluser, passwd=sqlpasswd, host=sqlhost, autocommit=True, database="uic_project"
)
cursor = cnx.cursor()
def execute(arg):
    cursor.execute(arg)
    cursor.close()

def main():
    while True:
        query = "SELECT * FROM main"
        execute(query)
        result = cursor.fetchall()
        print(result)