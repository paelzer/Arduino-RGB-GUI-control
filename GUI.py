import serial
import PySimpleGUIQt as sg

ser = serial.Serial('COM5', 9600)

# **************************************** Defines the GUI *****************************************************************************************************
#
layout = [

            [sg.Text('Select case illumination color...')],        
            [sg.Button('RED', button_color = ("white", "red"), key='red', size=(207,40)), sg.Button('GREEN', button_color = ("white", "green"), key='green', size=(207,40))],
            [sg.Button('BLUE', button_color = ("white", "blue"), key='blue', size=(207,40)), sg.Button('PURPLE', button_color = ("white", "purple"), key='purple', size=(207,40))],
            [sg.ColorChooserButton("", button_color=sg.TRANSPARENT_BUTTON, image_filename="rgb.png", image_subsample=2, size=(207, 40), border_width=0, key="rgbSelect"), sg.Button('All off', size=(207,40), key='allOff')],
            [sg.Button('Apply to case', size=(207,40), key="apply"), sg.Button('Exit', size=(207,40), key='exit')],

          ]

window = sg.Window('CASE ILLUMINATION - v:0.9 -', no_titlebar=False).Layout(layout)

# **************************************** Runs the GUI ********************************************************************************************************
#

while True:
    event, values = window.Read()
    
    if event is None or event == 'exit':
        ser.write("allOff".encode())
        print("Exit!")
        break

    elif event  == 'red':
        print("Rot!")
        ser.write("red".encode())

    elif event  == 'green':
        print("Grün!")
        ser.write("green".encode())

    elif event  == 'blue':
        print("Blau!")
        ser.write("blue".encode())

    elif event  == 'purple':
        print("Violett!")
        ser.write("purple".encode())

    elif event  == 'allOff':
        print("All off!")
        ser.write("allOff".encode())

    elif event  == 'apply':
        print("Apply RGB to case!")
        rgbSelectValue = values["rgbSelect"]
        print("First rgbSelectValue:", rgbSelectValue)
        rgbSelectValue = rgbSelectValue[1:]
        rgbSelectValue = str(int(rgbSelectValue, 16))
        rgbSelectValue = "#" + rgbSelectValue
        print("RGB: ", rgbSelectValue)
        ser.write(rgbSelectValue.encode())

window.Close()
ser.close()
