#!/bin/python3
import mariadb as connector

# import time
# import os

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


# def os_clear():
#    if os.name == "nt":
#        os.system("cls")
#    else:
#        os.system("clear")


def main():
    query = "SELECT * FROM main"
    execute(query)
    result = cursor.fetchall()
    print("+" + "-" * 18 + "+" + "-" * 10 + "+")
    print("|" + " Parking Slot No." + " |", end="")
    print(" Status" + "   |")
    print("+" + "-" * 18 + "+" + "-" * 10 + "+")
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
    print("+" + "-" * 18 + "+" + "-" * 10 + "+")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cnx.close()
        print("\nExited.")
        exit(0)
