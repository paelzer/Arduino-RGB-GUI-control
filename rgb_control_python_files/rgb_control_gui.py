import serial
import PySimpleGUIQt as sg

# Color codes for the 4 predefined colors in the gui
red    = "ff0000"
green  = "00ff00"
blue   = "0000ff"
purple = "9e0083"

off    = "000000" # Turns the RGB LED pins off

lineLength = 59 # Lenght for the 2 horizontal lines in the gui 

# Find your COM port number in the Arduino IDE and change the line below accordingly 
comPort = 'COM5'
    
# Function to send the color value as decimal via serial port to the Arduino
def requestColor(color):
    rgbSelectValue = str(int(color, 16)) # puts the color hex value as decimal in a string
    print(rgbSelectValue)
    ser.write(("#" + rgbSelectValue).encode())

# **************************************** Defines the GUI *****************************************************************************************************
#
layout = [

            [sg.Text('Select case illumination color...')],        
            [sg.Button('RED', button_color = ("white", "red"), key='red', size=(207,40)), sg.Button('GREEN', button_color = ("white", "green"), key='green', size=(207,40))],
            [sg.Button('BLUE', button_color = ("white", "blue"), key='blue', size=(207,40)), sg.Button('PURPLE', button_color = ("white", "purple"), key='purple', size=(207,40))],
            [sg.Text('_'  * lineLength)],
            [sg.ColorChooserButton("", button_color=sg.TRANSPARENT_BUTTON, image_filename="rgb.png", image_subsample=2, size=(207, 40), border_width=0, key="rgbSelect"), sg.Button('Apply selected color', size=(207,40), key="apply"), ],
            [sg.Text('_'  * lineLength)],
            [sg.Button('LEDs off', size=(207,40), key='Off'), sg.Button('Exit', size=(207,40), key='exit')]

          ]

# Open the serial port or show an error message and exit if not working
#
try:
    ser = serial.Serial(comPort, 9600)
except:
    sg.Popup("Couldn't open the serial port.\nWrong COM port defined or\nArduino not connected?")
    exit()

window = sg.Window('RGB Color Selector - v:1.0 -', no_titlebar=False).Layout(layout)

# **************************************** Runs the GUI ********************************************************************************************************
#
while True:
    event, values = window.Read()
    
    # Checks which of the buttons has been clicked and calls the requestColor function with the according value
    if event is None or event == 'exit':
        requestColor(off)
        print("Exit!")
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
        requestColor((values["rgbSelect"])[1:])

window.Close() # Exits from the gui loop
ser.close() # Closes the serial connection