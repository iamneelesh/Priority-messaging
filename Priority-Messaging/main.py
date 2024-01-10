import time
from pyautogui import(
    hotkey,
    press,
    typewrite,
)
from webbrowser import open as openpage


message = open("message.txt", "r").read().split("\n")


openpage("https://web.whatsapp.com/")
time.sleep(10)


groups_list = open("group.txt", "r").read().split("\n")


for group_name in groups_list:
    hotkey("ctrl", "alt", "/")

    typewrite(group_name)

    time.sleep(1)
    hotkey("enter")

    time.sleep(1)
    for char in message:
            typewrite(char)
            hotkey("shift", "enter")

    time.sleep(1)
    
    hotkey("enter")
    time.sleep(1)