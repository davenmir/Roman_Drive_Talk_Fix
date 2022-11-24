# helloworld

import PySimpleGUI as psg
import subprocess as sp


layout = [[psg.Button(button_text='Go To Talking', size=(
    200, 200), button_color='white', )]]

psg.SetOptions(window_location=(100, 100))

window = psg.Window('Hello world', layout, grab_anywhere=False,
                    size=(200, 100), keep_on_top=True, finalize=True, titlebar_background_color='white')

response = sp.getoutput('tasklist /FI \"IMAGENAME eq notepad.exe\"')
#print(response)
while (response == 'INFO: No tasks are running which match the specified criteria.'):
    response = sp.getoutput('tasklist /FI \"IMAGENAME eq notepad.exe\"')
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    if event == 'Go To Talking':
        window.Disappear()
        # go to talking software path
        sp.call(['C:\\WINDOWS\\system32\\Notepad.exe'])
        # sp.call(['D:\Coding\Roman_Drive_Talk_Fix\GUI.py'])
        if response != 'INFO: No tasks are running which match the specified criteria.':
            sp.call(['C:\\WINDOWS\\system32\\Notepad.exe', 'text.txt'])
        window.Reappear()
        print('hi')
window.close()
