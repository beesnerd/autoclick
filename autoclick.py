import pyautogui
from pyautogui import time


answer = input("would you like to left click or right click? (Right/Left) (case sensitive)")

if answer == 'Left':
    time.sleep(7)
    while True:
        for i in range(100):
            pyautogui.PAUSE = 0.01
            pyautogui.leftClick()


if answer == 'Right':
    time.sleep(7)
    while True:
        for i in range(100):
            pyautogui.PAUSE = 0.01
            pyautogui.rightClick()

# the higher the number is in for i in range, the more it clicks (the default 100 gives about 30 cps)

