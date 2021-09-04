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

# the less pause the more cps so if you want to make this faster keep this in mind

