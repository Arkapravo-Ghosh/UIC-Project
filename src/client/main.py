#!/bin/python3
import mariadb as connector
import time
import pandas
from IPython.display import display

# MariaDB configuration
sqlhost = "Ark-Pi"
sqluser = "client"
sqlpasswd = "guest"
cnx = connector.connect(
    user=sqluser,
    passwd=sqlpasswd,
    host=sqlhost,
    autocommit=True,
    database="uic_project",
)
cursor = cnx.cursor()


def execute(arg):
    cursor.execute(arg)


def main():
    query = "SELECT * FROM main"
    execute(query)
    result = cursor.fetchall()
    print(result)
    data = {"Parking Slot Number": result[1], "Parking Slot Status": result[0]}
    # Result using pandas table
    df = pandas.DataFrame(data)
    display(df)
    time.sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cnx.close()
        print("\nExited.")
