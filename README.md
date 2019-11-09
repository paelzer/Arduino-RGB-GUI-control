# Arduino-RGB-GUI-control
This project allows you to control an RGB - LED attached to an Arduino UNO from your PC or notebook via a color selector GUI made with Python.

## Prerequisites for the Python GUI:


* Python3 installed (https://www.python.org/downloads/)

* Python package management system up to date (python -m pip install --upgrade pip)

* Python modules installed:

      PySimpleGUIQt (pip install --upgrade PySimpleGUIQt)
      PySide2 (pip install PySide2)


## Prerequisites for the Arduino part of the project

* Arduino IDE installed (https://www.arduino.cc/en/main/software)

## RGB LED hook up

* The RGB LED should be connected to the Arduino UNO as follows:

      LED pin for red connected to Arduino pin 9
      LED pin for green connected to Arduino pin 10
      LED pin for blue connected to Arduino pin 11
      LED ground pin to Arduino GND pin 
