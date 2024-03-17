import pyautogui
import time

time.sleep(3)

i = 0
while i < 100:
    msg = "test"
    pyautogui.write(msg)
    pyautogui.press("enter")
    i += 1




