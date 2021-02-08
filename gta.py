import pyautogui
import time

klicks = 800


time.sleep(5)

while klicks > 0:
    time.sleep(15)
    pyautogui.press('w', presses=3)
    klicks -= 