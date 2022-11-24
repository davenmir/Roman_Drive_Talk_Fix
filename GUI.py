import PySimpleGUI as psg
import subprocess as sp
import os as os

layout = [[psg.Button(button_text='Go To Talking', size=(
    300, 300), button_color=('black', 'white'))]]

psg.SetOptions(window_location=(100, 100))

window = psg.Window('', layout, grab_anywhere=False, no_titlebar=True,
                    size=(300, 200), margins=(0,0), keep_on_top=True, finalize=True)

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
        taskkill = os.system("taskkill /im notepad.exe") # change to driving exe
        if taskkill == '128': #change notepad to ability drive exe 
            print('hit')
        if response != 'INFO: No tasks are running which match the specified criteria.':
            sp.call(['C:\\WINDOWS\\system32\\Notepad.exe', 'text.txt'])
        window.Reappear()
        print('hi')
window.close()
