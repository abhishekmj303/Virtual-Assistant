import PySimpleGUI as sg
import qrcode, pyperclip

clpb = pyperclip.paste()
img = qrcode.make(clpb)
file = "./temp_qr.png"
img.save(file)

sg.theme('DarkAmber')

layout = [ [sg.Text(clpb, font=("Fira Sans", 12), justification='center')],
             [sg.Image(filename=file)] ]
window = sg.Window('QRCode', layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()