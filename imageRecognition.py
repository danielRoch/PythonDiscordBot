from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import win32gui

# while 1:
#     if pyautogui.locateOnScreen('PlayButton.png', region=(1120, 935, 260, 75), grayscale=True, confidence=0.8) != None:
#         print("I can see it")
#         time.sleep(0.5)
#     else:
#         print("I am unable to see it")
#         time.sleep(0.5)

x, y = pyautogui.locateCenterOnScreen("PlayButton.png")
print("x: " + str(x) + ", y: " + str(y))
click(x, y)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
