import pyautogui as pg
import time

print("starting in 5 seconds...")
time.sleep(5)

for i in range(5):
    pg.write("hello")
    pg.press("Enter")
    time.sleep(1)
