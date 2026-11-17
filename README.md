# Environmental Data Logging and Monitoring System

## Project Overview

The Environmental Data Logging and Monitoring System is an embedded systems simulation project designed to monitor environmental parameters such as temperature and humidity.
The project uses an Arduino UNO with DS1621 and DHT11 sensor models in SimulIDE. Arduino code is used to interface with the sensors and display readings through serial communication. Python is used for data logging, timestamp generation, CSV file storage, and graphical visualization.

## Objectives

- Monitor environmental temperature and humidity.
- Interface digital sensors with Arduino UNO.
- Simulate the embedded system using SimulIDE.
- Display sensor readings through serial communication.
- Store environmental readings in CSV format using Python.
- Visualize temperature and humidity variations through graphs.

## Hardware Components (Simulated)

- Arduino UNO
- DS1621 Digital Temperature Sensor
- DHT11 Temperature and Humidity Sensor
- Connecting wires
- Pull-up resistors for I2C communication

## Software Requirements

- Arduino IDE 1.8.19
- SimulIDE
- Python 3.11
- Python IDLE
- Adafruit DHT Sensor Library
- Adafruit Unified Sensor Library

## System Architecture

DS1621 and DHT11 Sensors  
↓  
Arduino UNO  
↓  
Serial Output  
↓  
Python Data Logging  
↓  
CSV File Storage  
↓  
Temperature and Humidity Visualization

**Note:** Automatic Arduino-to-Python serial data transfer is not implemented in the current version. Python currently accepts manually entered readings for CSV storage.


## Project Implementation

 1. Sensor Interfacing- The Arduino UNO communicates with the DS1621 using I2C communication and reads temperature and humidity from the DHT11 using its digital interface.
 2. Arduino Programming- The Arduino program reads sensor parameters and displays the readings through the Serial Monitor at 9600 baud.
 3. Python Data Logging- Python IDLE is used to create a CSV data logger. The program accepts temperature and humidity values, adds date and time information, and stores the readings in a CSV file.
 4. Data Visualization- A Python graphical interface displays temperature and humidity variations using the recorded CSV data.

## Sample Output

| Date | DS1621 Temperature | DHT11 Temperature | Humidity |

| 2026-11-17 | 28°C | 28°C | 65% |
| 2026-11-17 | 29°C | 29°C | 60% |
| 2026-11-17 | 30°C | 30°C | 58% |

*These are illustrative sample values.*

## Applications

- Environmental monitoring systems
- Weather data logging
- Indoor temperature and humidity monitoring
- Climate observation
- Smart agriculture monitoring


## Conclusion

This project demonstrates the integration of embedded systems simulation, digital sensor interfacing, Python programming, CSV data logging, and graphical data visualization. It provides a foundation for developing automated environmental monitoring and IoT-based applications.

Developed as an Embedded Systems Simulation Project.

**Technologies:** Arduino UNO | Embedded C/C++ | Python | SimulIDE | CSV | Data Visualization
