import os
import pyautogui
import keyboard
import time
import sys
from mss import mss

clear = lambda: os.system('cls')

def quit(b):
    if keyboard.is_pressed(b):
        sys.exit(0)

def click():
    with mss() as sct:
        while True:
            quit("q")
            bbox = (start_x, start_y, start_x + width + 1, start_y + 1)
            img = sct.grab(bbox)
            for cord in cords_x:
                quit("q")
                if img.pixel(cord, 0)[0] < 90:
                    pyautogui.click(start_x + cord, start_y)
                    break

def mouse_location(b):
    while True:
        start = pyautogui.position()
        if keyboard.is_pressed(b) == True:
            return [start.x,start.y]
            break


clear()



print("Welcome to PianoPy\nHave any piano-tiles game open\nMake sure the tiles from the game are black\nStart by pressing the spacebar")
while True:
    if keyboard.is_pressed('space'):
        break
clear()
print('You can quit the program at any time by just pressing q')
time.sleep(1)
print('\nHover your mouse over the top left corner of the Piano-Tiles window and press space')
time.sleep(0.5)
location_left = mouse_location('space')
print('\nNow do the same for the bottom right corner')
time.sleep(0.5)
location_right = mouse_location('space')
print('\nNow hover over the middle of a tile and press space')
time.sleep(0.5)
tile_y = mouse_location('space')
start_x = location_left[0]
start_y = tile_y[1]
width = location_right[0] - location_left[0]
clear()
time.sleep(0.5)
print("hover over the first lane and press space")
time.sleep(0.5)
h_1 = mouse_location('space')
time.sleep(0.5)
print("hover over the second lane and press space")
h_2 = mouse_location('space')
time.sleep(0.5)
print("hover over the third lane and press space")
h_3 = mouse_location('space')
time.sleep(0.5)
print("hover over the fourth lane and press space")
time.sleep(0.5)
h_4 = mouse_location('space')
cords_x = [h_1[0] - start_x, h_2[0]- start_x, h_3[0]- start_x, h_4[0]- start_x]
print('Now click on the start tile and let the program do the work!')
time.sleep(0.3)
click()






#click()