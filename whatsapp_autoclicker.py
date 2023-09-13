import pyautogui as gui
import time

message = input("Enter a message: ")
number = input("How many times do you want to send the entered message?: ")

messaget_time = input("How much time do you want to leave between each message (in seconds): ")

time.sleep(messaget_time)

for i in range(int(number)):
    gui.typewrite(message)
    gui.press('Enter')
