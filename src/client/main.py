#!/bin/python3
import mariadb as connector
import time

# MariaDB configuration
sqlhost = "Ark-Pi"
sqluser = "client"
sqlpasswd = "guest"
try:
    cnx = connector.connect(
        user=sqluser,
        passwd=sqlpasswd,
        host=sqlhost,
        autocommit=True,
        database="uic_project",
    )
except connector.OperationalError:
    print("Connection to database failed.")
    exit(1)
cursor = cnx.cursor()


def execute(arg):
    cursor.execute(arg)


def main():
    query = "SELECT * FROM main"
    execute(query)
    result = cursor.fetchall()
    print("-" * 31)
    print("|" + " Parking Slot No." + " |", end="")
    print(" Status" + "   |")
    print("-" * 31)
    print("| 1                |", end="")
    if result[0][1] == 1:
        print(" " + "Occupied" + " |")
    else:
        print(" " + "Free" + "     |")
    print("| 2                |", end="")
    if result[1][1] == 1:
        print(" " + "Occupied" + " |")
    else:
        print(" " + "Free" + "     |")
    print("-" * 31)
    time.sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cnx.close()
        print("\nExited.")
        exit(0)
