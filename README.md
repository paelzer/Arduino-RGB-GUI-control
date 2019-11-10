# Arduino RGB LED GUI control
**This project allows you to control an RGB - LED attached to an Arduino UNO from your PC or notebook via a color selector GUI built with PySimpleGUI.**

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

## Software preparation

* Adjust the COM port number definition in the rgb_control_gui.py file to match the COM port number on your system:
      For example if your COM port has no. 2 adjust the line as follows and save the file:      

            ser = serial.Serial('COM2', 9600)
            
* Flash the rgb_control.ino file to the Arduino Uno
