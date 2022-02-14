# Auto Shiny Hunter
# Written by: Wyatt Johnson
# Specifically for Drifloon

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

from PIL import Image, ImageGrab
import numpy as np
from matplotlib import pyplot as plt

import pyautogui
import win32gui

import cv2

chrome_options = Options()
# chrome_options.add_argument('--headless')
def reset():
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="m:\\nxbt\\chromedriver.exe")
    driver.get("http://localhost:8000/bot")
    print('loading page...')
    delay = 9999
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'MacroDone')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too long!")

    driver.close()

def screenshot(file, window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(0, 'DroidCam')
        if hwnd:
            # win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x + 200, y, x1 - 200, y1 - 100))
            im.save(file)
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im

def checkShiny(file):
    img = cv2.imread(file)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask1 = cv2.inRange(img_hsv, (3, 170, 215), (7,190, 235))
    mask2 = cv2.inRange(img_hsv, (145, 85, 80), (190, 160, 190))
    mask3 = cv2.inRange(img_hsv, (155, 65, 160), (180, 100, 225))
    mask4 = cv2.inRange(img_hsv, (0, 85, 180), (8, 150, 220))
    mask5 = cv2.inRange(img_hsv, (0, 0, 0), (10, 10, 10))
    mask_1 = cv2.bitwise_or(mask1, mask2)
    mask_2 = cv2.bitwise_or(mask3, mask4)
    mask = cv2.bitwise_or(mask_1, mask_2)
    mask = cv2.bitwise_or(mask, mask5)
    return mask

def run():
    counter = 0
    while True:
        counter += 1
        reset()
        print('running macro')
        print("You've reset " + str(counter) + " times.")
        time.sleep(51.5) #wait for macro to run
        im = screenshot(r"C:\Users\wyatt\Desktop\screenshots\drifloon" + str(counter) + ".png", 'DroidCam')
        print('took screenshot')
        mask = checkShiny("C:\\Users\\wyatt\\Desktop\\screenshots\\drifloon" + str(counter) + ".png")
        print(np.sum(mask))
        if(np.sum(mask) < 125000):
            print('Unsure... might be a shiny, checking again...')
            time.sleep(10.5)
            im = screenshot(r"C:\Users\wyatt\Desktop\screenshots\drifloon-check-" + str(counter) + ".png", "DroidCam")
            print("took a second screenshot")
            mask = checkShiny("C:\\Users\\wyatt\\Desktop\\screenshots\\drifloon-check-" + str(counter) + ".png")
            if (np.sum(mask) < 125000):
                print("Good chance that it's a shiny!!! Stopping...")
                break
            else:
                print("second check wasn't shiny :( resetting...")
        else:
            print('not shiny resetting...')
    return counter

def test(file):
    mask = checkShiny(file)
    cv2.imshow("mask", mask)
    print(np.sum(mask))
    cv2.waitKey(0)
    quit()

# test("C:\\Users\\wyatt\\Desktop\\screenshots\\drifloon-check-253.png")
counter = run()
print("Times reset: " + str(counter))


