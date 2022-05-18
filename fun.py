import keyboard
import time

keyboard.press_and_release("windows")
time.sleep(.5)
keyboard.write("chrome")
time.sleep(.5)
keyboard.press_and_release("enter")
time.sleep(.5)
keyboard.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
time.sleep(.5)
keyboard.press_and_release("enter")