# ************************************************************************************************
#
#    A GUI built with the amazing PySimpleGUI to control an RGB LED connected to an Arduino UNO
#
# ************************************************************************************************

import serial
import serial.tools.list_ports
import PySimpleGUIQt as sg

# Default state for the while loop that connects to the Arduino COM port
arduinoConnected = False

# List the available COM ports will be added to
comPorts = [], []

# Color codes for the 4 predefined colors in the gui
red    = "ff0000"
green  = "00ff00"
blue   = "0000ff"
purple = "9e0083"

# Turns the RGB LED pins off
off    = "000000"

# Lenght for the 2 horizontal lines in the gui
lineLength = 59


# Function to send the color value as decimal via serial port to the Arduino
#
def requestColor(color):
    rgbSelectValue = str(int(color, 16)) # puts the color hex value as decimal in a string
    ser.write(("#" + rgbSelectValue).encode())


# Function to return available hardware serial ports and (if possible) detect current Arduino COM port
#
def getSerialPorts():
    ports = serial.tools.list_ports.comports(include_links=False)
    for i, e in enumerate(ports):
        # Trying to automatically detect Arduino COM port by looking for "Arduino" string in information of all available hardware serial ports
        if "Arduino" in e[1]:
            comPort = e[0]
        comPorts[0].append(e[0])
        comPorts[1].append(e[1])
    return comPorts, comPort


# Sets the COM port the Arduino is connected to automatically or requests manual COM port input from user if not working
#
while(not arduinoConnected):
    try:
        comPorts, comPort = getSerialPorts()
        ser = serial.Serial(comPort, 9600)
        arduinoConnected = True
    except:
        # Automatic Arduino COM port detection failed so giving the user the possibility to manually enter the COM port
        comPort = sg.PopupGetText(('Connect your Arduino and enter Arduino COM port!\nAvailable hardware COM ports are:\n' + str(comPorts[0])), 'Enter COM port')
        comPorts = [], []
        if comPort == "Cancel" or comPort is None:
            exit()
        try:
            # Try to connect to the manually specified COM port
            ser = serial.Serial(comPort, 9600)
            arduinoConnected = True
        except:
            # Manual input of the COM port failed so giving the user the possibility to try again or leave
            decision = sg.PopupOKCancel("The COM port you entered is not available.\nClick OK to try again or Cancel to exit!")
            if decision == "Cancel" or decision is None:
                exit()
            

# **************************************** Defines the GUI *****************************************************************************************************
#
layout = [

            [sg.Text('Select RGB LED color...')],        
            [sg.Button('RED', button_color = ("white", "red"), key='red', size=(207,40)), sg.Button('GREEN', button_color = ("white", "green"), key='green', size=(207,40))],
            [sg.Button('BLUE', button_color = ("white", "blue"), key='blue', size=(207,40)), sg.Button('PURPLE', button_color = ("white", "purple"), key='purple', size=(207,40))],
            [sg.Text('_'  * lineLength)],
            [sg.ColorChooserButton("", button_color=sg.TRANSPARENT_BUTTON, image_filename="rgb.png", image_subsample=2, size=(207, 40), border_width=0, key="rgbSelect"), sg.Button('Apply selected color', size=(207,40), key="apply"), ],
            [sg.Text('_'  * lineLength)],
            [sg.Button('LEDs off', size=(207,40), key='Off'), sg.Button('Exit', size=(207,40), key='exit')],
            [sg.Text("...currently connected to " + comPort), sg.Text((" " * 39) + "p43lz3r", text_color="blue")]

          ]

window = sg.Window('RGB Color Selector', no_titlebar=False).Layout(layout)


# **************************************** Runs the GUI ********************************************************************************************************
#
while True:
    event, values = window.Read()
    
    # Checks which of the buttons has been clicked and calls the requestColor function with the according value
    if event is None or event == 'exit':
        requestColor(off)
        break
    
    elif event  == 'red':
        requestColor(red)

    elif event  == 'green':
        requestColor(green)

    elif event  == 'blue':
        requestColor(blue)

    elif event  == 'purple':
        requestColor(purple)

    elif event  == 'Off':
        requestColor(off)

    elif event  == 'apply':
        if values["rgbSelect"] != None:
            requestColor((values["rgbSelect"])[1:])
        else:
            sg.Popup("Select a color first!", no_titlebar=True)

window.Close() # Exits from the gui loop
ser.close() # Closes the serial connection
