#!/bin/python3
import RPi.GPIO as GPIO
import time
import mariadb as connector

# MariaDB configuration
sqlhost = "localhost"
sqluser = "uicprojserver"
with open("mysqlpasswd", "r") as passfile:
    sqlpasswd = passfile.read()
cnx = connector.connect(
    user=sqluser,
    passwd=sqlpasswd,
    host=sqlhost,
    autocommit=True,
    database="uic_project",
)

# Pin Config
ir1 = 15
ir2 = 16

# Pinmode Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ir1, GPIO.IN)
GPIO.setup(ir2, GPIO.IN)


def execute(arg):
    cursor = cnx.cursor()
    cursor.execute(arg)
    cursor.close()


def main():
    while True:
        if GPIO.input(ir1):
            x = 0
        else:
            x = 1
        query = f"UPDATE main SET full = {x} WHERE id = 1"
        execute(query)
        if GPIO.input(ir2):
            y = 0
        else:
            y = 1
        query = f"UPDATE main SET full = {y} WHERE id = 2"
        execute(query)
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nExited.")
        exit(0)
