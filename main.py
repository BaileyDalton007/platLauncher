import win32gui
import win32con
import time
import os

# opens config file with KeysPerSecond (cps.exe) file
# config file must have cps.exe as default 'open with' program
os.popen(r'programs\config.kpsconf3')

# waits for program to actually open
time.sleep(5)

# searches for program named 'KeysPerSecond' and if possible brings it to the foreground
def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'KeysPerSecond' in win32gui.GetWindowText(hwnd):
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            if win32gui.IsWindowVisible(hwnd):
                pass
            else:
                win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

win32gui.EnumWindows(enumHandler, None)

# opens keystrokes (first launch right click on white window to open editor and select the .xml config file)
os.popen(r'programs\Keystrokes.exe')

# opens Minecraft on launch
os.popen(r'explorer.exe shell:appsFolder\Microsoft.MinecraftUWP_8wekyb3d8bbwe!App')



