import cv2
import numpy as np
from pyzbar.pyzbar import decode
import PySimpleGUI as sg
import pyperclip, time
from pyautogui import hotkey

def show_data(data):
    sg.theme('DarkAmber')

    layout = [ [sg.Text('Output: '+data, font=("Fira Sans", 12), justification='center')],
                [sg.Button('Copy'), sg.Button('Open/Search')] ]
    window = sg.Window('QR Scan', layout)

    while True:
        event, value = window.read()
        if event == 'Copy':
            pyperclip.copy(data)
            break;

        if event == 'Open/Search':
            pyperclip.copy(data)
            time.sleep(1)
            hotkey('shift', 'ctrl', 'alt', 'v')
            break;

        if event == sg.WIN_CLOSED:
            break

    window.close()

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeType = obj.type
        if barcodeType is not None:
            barcodeData = obj.data.decode("utf-8")
            string = str(barcodeData)
            return string
            # show_data(string)
            

        # string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
        # cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        # print("Barcode: "+barcodeData +" | Type: "+barcodeType)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    scanned = decoder(frame)
    if scanned is not None:
        show_data(scanned)
        break
    cv2.imshow('Scan QR Code', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
