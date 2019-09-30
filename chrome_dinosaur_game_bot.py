import mss
from PIL import Image
import time
import keyboard
from pynput.keyboard import Key, Controller
import pyautogui as gui
keyboardy = Controller()
gui.hotkey("alt", "tab")
time.sleep(1)
wasblack = False
gui.press("space")
num = 0
rand = 0.3
ok = time.time()
def timing(seconds, delay):
    if start - ok > seconds:
        global rand
        rand = delay
def get_screenshot(monitor_num):
    sct_img = sct.grab(monitor_num)
    global img
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
def pixel_colour(x1, x2, y):
    r, g, b = img.getpixel((x1 - x2, y))
    return r + g + b
with mss.mss() as sct:
    monitor = {"top": 150, "left": 570, "width": 130, "height": 150}
    monitor2 = {"top": 260, "left": 608, "width": 47, "height": 28}
    while True:
        if num > 65:
            something = 2
            if monitor["left"] > 705:
                something = 0
            monitor["left"] = monitor["left"] + something
            num = 0
        get_screenshot(monitor)
        num += 1
        top = pixel_colour(monitor["width"], 1, 105)
        med = pixel_colour(monitor["width"], 1, 120)
        bottom = pixel_colour(monitor["width"], 1, 140)
        top1 = pixel_colour(monitor["width"], 30, 105)
        med1 = pixel_colour(monitor["width"], 35, 120)
        bottom1 = pixel_colour(monitor["width"], 35, 140)
        colour = pixel_colour(1, 0, 1)

        if top != colour or med != colour or bottom != colour or top1 != colour or med1 != colour or bottom1 != colour:
            keyboardy.press(Key.space)
            while True:
                time.sleep(0.014)
                if True:
                    start = time.time()
                    while time.time() - start < rand:
                        timing(60, 0.27)
                        timing(120, 0.24)
                    keyboardy.press(Key.down)
                    if monitor["left"] < 630:
                        time.sleep(0.40 - rand + 0.02)
                    else:
                        time.sleep(0.40 - rand)
                    keyboardy.release(Key.down)
                break
        if keyboard.is_pressed("q"):
            quit()
