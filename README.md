# Arduino RGB LED - GUI control
**This project allows you to control an RGB - LED connected to an Arduino UNO from your PC or notebook via a color selector GUI built with the amazing [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/).**

It has been tested sucessfully with following setup:

* Windows 10 x64

* Python 3

* Arduino IDE 1.8.9

* Arduino UNO (other Arduino boards work as well with some modifications depending on the model)

## Prerequisites for the Python GUI:


* [Python3](https://www.python.org/downloads/) installed 

* Python package management system up to date (python -m pip install --upgrade pip)

* Install the following python modules by opening a command line window and type:

      pip install pyserial
      pip install pysimpleguiqt
      pip install PySide2

## Prerequisites for the Arduino part of the project

* [Arduino IDE](https://www.arduino.cc/reference/en/) installed

* Flash the rgb_control.ino file to the Arduino Uno


* Connect the Arduino via USB to your PC or notebook

## Pinout
Required hardware components:

      3x Resistor 220 Ohm
      RGB LED (common cathode - type)
      Arduino UNO
      
The RGB LED should be connected to the Arduino UNO as follows:

      LED pin for red connected to Arduino pin 9
      LED pin for green connected to Arduino pin 10
      LED pin for blue connected to Arduino pin 11
      LED ground pin to Arduino GND pin       

<b>Click to enlarge:</b> 
</br> </br>
<img src="https://i.imgur.com/NEBTWak.png" width="600">


## Start the Python GUI

* Run the rgb_control_gui.py Python file by typing the following line in a command line window:
      
      python rgb_control_gui.py

* The GUI will start
      
* The COM port your Arduino is connected to should be detected automatically - if this fails you can enter the COM port manually. A list of available hardware serial ports will show up in a popup window.
* Click the buttons in the GUI. The color of the RGB LED should change accordingly.
  
</br>

<img src="https://i.imgur.com/EEbAoNf.jpg">

</br>

<img src="https://i.imgur.com/EXJVYeP.jpg">
  
  
