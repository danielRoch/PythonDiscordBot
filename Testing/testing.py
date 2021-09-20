import datetime
import json

import pandas as pd
import subprocess
import pyautogui
import time
import keyboard
import random

import schedule as schedule
import win32api, win32con, win32gui
import os
import numpy as np
import pytesseract as tess
from pytesseract import Output
from timeloop import Timeloop
from datetime import timedelta

tess.pytesseract.tesseract_cmd = r'C:\Users\droc1\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
import cv2

screen_width, screen_height = pyautogui.size()

# time.sleep(5)

### FINDING MINECRAFT WINDOW
# hwnd = win32gui.FindWindow(None, "Minecraft 1.8.9")
# win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
# win32gui.SetForegroundWindow(hwnd)

# ISSUING COMMANDS TO MC
# pyautogui.press('t')
# keyboard.write('/server retro')
# keyboard.press('enter')

# GOING TO IS TOP AND SEEING THE RANKINGS
# pyautogui.press('t')
# keyboard.write('/is top')
# keyboard.press('enter')

# time.sleep(1)
#
# win32api.SetCursorPos((1170, 594))

# x, y = pyautogui.locateCenterOnScreen(r"../istopGlassPane.png")
# print("Start: " + str(x) + "," + str(y))
# startx = x
# endy = y+72
# endx = x+324
# county = 0
# countx = 0
# for y in range(y+36, endy+36, 36):
#     county = county+1
#     x = startx
#     print("Y: " + str(y))
#     if y == endy:
#         x = x+36
#         endx = endx-36
#         print(str(x) + "," + str(endx))
#     for x in range(x, endx, 36):
#         time.sleep(.5)
#         countx = countx + 1
#         win32api.SetCursorPos((x, y))
#         print(str(x) + "," + str(y))
# print(str(countx) + "," + str(county))

### TAKING A SCREENSHOT OF THE IS TOP ISLAND INFO
# x, y = pyautogui.locateCenterOnScreen(r"../istopGlassPane.png")
# win32api.SetCursorPos((x, y+36))
# time.sleep(0.25)
# im1 = pyautogui.screenshot(region=(x+16, y+5, 378, 496))
# im1.save(r"isTopInfo.png")

## GETTING BOUNDING BOXES AROUND TEXT ##
# d = tess.image_to_data(img, output_type=Output.DICT)
# n_boxes = len(d['level'])
# for i in range(n_boxes):
#     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)

# img = cv2.imread('isTopInfo.png')
# custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789$._#ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6'
#
# text = tess.image_to_data(img, config=custom_config, output_type='data.frame')
# df = pd.DataFrame(text)
# df = df.drop(
#     columns=['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height',
#              'conf']).dropna()
# df = df.drop(df.tail(1).index)
# df = df.reindex(
#     columns=df.columns.tolist() + ['island_leader', 'place', 'worth_reported', 'worth_actual', 'moderators', 'members'])
# df = df.astype({'moderators': object, 'members': object})
# df.reset_index(drop=True, inplace=True)
#
# print(df)
#
# for x in range(0, df['text'].count(), 1):
#     value = df['text'].iloc[x]
#
#     if x == 0:
#         value = value[7:-2]
#         df.iloc[df['island_leader'].count(), df.columns.get_loc('island_leader')] = value
#
#     if x == 1:
#         value = value[-1:12]
#         df.iloc[df['place'].count(), df.columns.get_loc('place')] = value
#
#     if x == 2:
#         value = value[6:16]
#         df.iloc[df['worth_reported'].count(), df.columns.get_loc('worth_reported')] = value
#
#         # CHANGING VALUE TO FLOAT VALUE
#         # if value[-1] == 'M':
#         #     floatWorth = float(value[:-1])
#         #     floatWorth = floatWorth * 1000000
#         #
#         # if value[-1] == 'B':
#         #     floatWorth = float(value[:-1])
#         #     floatWorth = floatWorth * 1000000000
#         #
#         # if value[-1] == 'T':
#         #     floatWorth = float(value[:-1])
#         #     floatWorth = floatWorth * 1000000000000
#         #
#         # df.iloc[df['worth_reported'].count(), df.columns.get_loc('worth_reported')] = floatWorth
#
#     if value == 'MODERATORS':
#         y = x + 1
#         Moderators = []
#         for y in range(y, df['text'].count(), 1):
#             if df['text'].iloc[y] == 'MEMBERS':
#                 break
#             else:
#                 Moderators.append(df['text'].iloc[y])
#         df.iat[df['moderators'].count(), df.columns.get_loc('moderators')] = Moderators
#
#     if value == 'MEMBERS':
#         y = x + 1
#         Members = []
#         for y in range(y, df['text'].count(), 1):
#             Members.append(df['text'].iloc[y])
#         df.iat[df['members'].count(), df.columns.get_loc('members')] = Members
#
# df = df.drop(columns=['text']).dropna(axis='index', how='all')
# df.reset_index(drop=True, inplace=True)
#
# print(df)


# print(tess.image_to_data(img, config=custom_config))


###Reading Image to text
# custom_config = r'-c tessedit_char_blacklist=*+>»[!]() --psm 6'
# img = cv2.imread(r'../istop2.png')
# text = tess.image_to_string(img, config=custom_config)
# print(text)


### MULTIPLE IS TOP ###
## WORKS GOOD TO GO INTO MAIN BOT ##

# df_retroIsTop = pd.DataFrame(columns=['date', 'time', 'island_leader', 'place', 'worth_reported', 'worth_actual', 'moderators', 'members'])
# df_retroIsTop.to_csv('retroIsTop.csv')
# print(df_retroIsTop)
# x, y = pyautogui.locateCenterOnScreen("../istopGlassPane.png")
# startx = x
# endy = y + 72
#
# # Testing edny
# # endy = y + 36
#
# endx = x + 324
# # Testing endx
# # endx = x + 216
#
# # Cycling through the island top tooltips
# for y in range(y + 36, endy + 36, 36):
#     x = startx
#     if y == endy:
#         x = x + 36
#         endx = endx - 36
#     for x in range(x, endx, 36):
#         time.sleep(.5)
#
#         win32api.SetCursorPos((x, y))
#         time.sleep(0.25)
#         img = pyautogui.screenshot(region=(x + 16, y - 30, 378, 496))
#         img.save(r"isTopInfo.png")
#
#         img = cv2.imread('isTopInfo.png')
#         custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789$._#ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6'
#
#         text = tess.image_to_data(img, config=custom_config, output_type='data.frame')
#         df = pd.DataFrame(text)
#         df = df.drop(
#             columns=['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width',
#                      'height', 'conf']).dropna()
#         df = df.drop(df.tail(1).index)
#         df = df.reindex(
#             columns=df.columns.tolist() + ['date', 'time', 'island_leader', 'place', 'worth_reported', 'worth_actual', 'moderators', 'members'])
#         df = df.astype({'moderators': object, 'members': object})
#         df.reset_index(drop=True, inplace=True)
#
#         # Moving the data to the correct columns
#         for z in range(0, df['text'].count(), 1):
#             value = df['text'].iloc[z]
#
#             if z == 0:
#                 value = value.split('ISLAND')[-1]
#                 value = value.split('#')[0]
#                 if value == 'axiy':
#                     value = 'qxiy'
#                 elif value == '_noonie2005':
#                     value = 'noonie2005'
#                 df.iloc[df['island_leader'].count(), df.columns.get_loc('island_leader')] = value
#
#             if z == 1:
#                 # value = value[-1:12]
#                 value = value.split('#')[-1]
#                 df.iloc[df['place'].count(), df.columns.get_loc('place')] = value
#
#             if z == 2:
#                 value = value[6:16]
#                 df.iloc[df['worth_reported'].count(), df.columns.get_loc('worth_reported')] = value
#
#                 # CHANGING VALUE TO FLOAT VALUE
#                 # if value[-1] == 'M':
#                 #     floatWorth = float(value[:-1])
#                 #     floatWorth = floatWorth * 1000000
#                 #
#                 # if value[-1] == 'B':
#                 #     floatWorth = float(value[:-1])
#                 #     floatWorth = floatWorth * 1000000000
#                 #
#                 # if value[-1] == 'T':
#                 #     floatWorth = float(value[:-1])
#                 #     floatWorth = floatWorth * 1000000000000
#                 #
#                 # df.iloc[df['worth_reported'].count(), df.columns.get_loc('worth_reported')] = floatWorth
#
#             if value == 'MODERATORS':
#                 i = z + 1
#                 Moderators = []
#                 for i in range(i, df['text'].count(), 1):
#                     if df['text'].iloc[i] == 'MEMBERS':
#                         break
#                     else:
#                         Moderators.append(df['text'].iloc[i])
#                 df.iat[df['moderators'].count(), df.columns.get_loc('moderators')] = Moderators
#
#             if value == 'MEMBERS':
#                 i = z + 1
#                 Members = []
#                 for i in range(i, df['text'].count(), 1):
#                     Members.append(df['text'].iloc[i])
#                 df.iat[df['members'].count(), df.columns.get_loc('members')] = Members
#
#         # Dropping the text column and resetting the index
#         df = df.drop(columns=['text']).dropna(axis='index', how='all')
#         df.reset_index(drop=True, inplace=True)
#
#         df.to_csv('output.csv')
#
#         df_retroIsTop = pd.concat([df_retroIsTop, df]).reset_index(drop=True)
#         df_retroIsTop.to_csv('retroIsTop.csv')
#         print(df_retroIsTop)


### ACTIVATING SOMETHING AT A CERTAIN TIME OF DAY ###

# def job():
#     print("Current time is:" + time.ctime())
#
#
# schedule.every().hour.at(':00').do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# dateAndTime = datetime.datetime.now()
# date = dateAndTime.strftime("%x")
# hour = dateAndTime.strftime("%H:00")
#
# print(date)
# print(hour)

time.sleep(2)

with open("testing.json", "r") as f:
    _dict = json.load(f)

print(_dict)

if "784260313167298561" in _dict:
    print("Found it")
else:
    print("No luck")

# with open("testing.json", "w") as f:
#     json.dump(_dict, f, indent=4)



