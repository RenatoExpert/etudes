import keyboard
import time

time.sleep(5)       #   Giving you enough time to select input box with mouse pointer
while True:
    keyboard.press_and_release("ctrl+v,enter")
    time.sleep(1)   #   Turning sleep time too short or zero makes your PC freeze!


