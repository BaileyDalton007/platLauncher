import pydirectinput as pgui
import keyboard
import time
from ctypes import * 

#Hotkey slot and x coord, (y coords are all the same)
hotkeydict = {'1':674, '2':742, '3':816}

while True:
    y = 814
    try:
        key = keyboard.read_key()
        x = hotkeydict[key]
        #blocks mouse input, script must be run as admin to do so
        ok = windll.user32.BlockInput(True) #enable mouse block
        startx, starty = pgui.position()
        pgui.click(startx, starty)
        pgui.click(x, y)
        pgui.click(startx, starty)
        ok = windll.user32.BlockInput(False) #disable mouse block
    except:
        pass