# Project for Ureckon Innovation Challenge 2023
![](https://img.shields.io/badge/license-MIT-blue)
![](https://img.shields.io/badge/languages-arduino%2C%20python%2C%20sql-blue)
### Made by:
* Sankalpa Dutta, 1st Year, CSE (IoT)
* Dhruba Dutta Banik, 1st Year, CSE (IoT)
* Disha Laskar, 1st Year, CST
* Arkapravo Ghosh, 1st Year, CSE (IoT)
* Mahak Gupta, 2nd Year, CST

# Hardware
<details>
    <summary>Using Arduino Uno and Raspberry Pi</summary>

## Raspberry Pi
Configure the Raspberry Pi to run [this file](src/server/main.py) on boot. This file will capture data from Serial
Monitor and store it in a MariaDB Database.
## Arduino Uno
Upload the [Source Code](src/arduino/main) to Arduino Uno Board, then create the circuit as shown below:
<!--
![](src/arduino/circuit_diagram.png)
--->
<p align="center"><a><img height="500" src="https://raw.githubusercontent.com/Arkapravo-Ghosh/UIC-Project/main/src/arduino/circuit_diagram.png?token=GHSAT0AAAAAAB2RG62I6P4SJHPG74VOMBFCY7ITOVQ"></a>&nbsp;&nbsp;</p>

> This circuit will read the data from the IR sensors and send it to the Raspberry Pi via Serial Monitor.

</details>

<details>
    <summary>Using Raspberry Pi only</summary>

## Raspberry Pi
Configure the Raspberry Pi to run [this file](src/alternate/main.py) on boot. This file will capture data from the
IR sensors via GPIO Pins and store it in a MariaDB Database.

Refer to the following diagram for Rasberry Pi 4 Model B to understand GPIO Pins
<p align="center"><a><img height="500" src="https://raw.githubusercontent.com/Arkapravo-Ghosh/UIC-Project/main/src/alternate/GPIO-Pinout-Diagram-2.png?token=GHSAT0AAAAAAB2RG62I4ORLOWJWA5FS4FV2Y7ITVXQ"></a>&nbsp;&nbsp;</p>

* Connect Ground Pin of Raspberry Pi to the GND Pins of both the IR Sensors
* Similarly, connect any of the 5V Power pins of Raspberry Pi to the VCC Pins of both the IR Sensors
* Connect GPIO 22 (Pin 15) of Raspberry Pi to OUT Pin of the IR Sensor at Parking Slot 1
* Similarly, connect GPIO 23 (Pin 16) of Raspberry Pi to OUT Pin of the IR Sensor at Parking Slot 2

</details>
