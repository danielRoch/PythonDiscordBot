import datetime
import subprocess
import time
import cv2
import keyboard
import pyautogui
import schedule
import win32api
import win32con
import win32gui
import pandas as pd
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Users\droc1\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# CLICKING AT AN X, Y POINT ON THE SCREEN:
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.25)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# OPENING MC:
def openMC():
    subprocess.Popen([r'C:\Users\droc1\Twitch\Minecraft\Install\minecraft.exe'])
    screen_width, screen_height = pyautogui.size()

    # FINDING MC LAUNCHER AND CLICKING THE PLAY BUTTON:
    while True:
        mcLauncher = win32gui.FindWindow(None, "Minecraft Launcher")
        if mcLauncher != 0:
            win32gui.SetForegroundWindow(mcLauncher)
            x, y = pyautogui.locateCenterOnScreen(r"../PlayButton.png")
            click(x, y)
            break

    joinPvpwars()

# CLOSING MC:
def closeMC():
    mc = win32gui.FindWindow(None, "Minecraft 1.12.2")
    if mc != 0:
        win32gui.ShowWindow(mc, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(mc)
        x, y = pyautogui.locateCenterOnScreen(r"../CloseButton.png")
        click(x, y)

# FINDING MC AND CLICKING THE PVPWARS BUTTON:
def joinPvpwars():
    while True:
        mc = win32gui.FindWindow(None, "Minecraft 1.12.2")
        if mc != 0:
            win32gui.ShowWindow(mc, win32con.SW_MAXIMIZE)
            win32gui.SetForegroundWindow(mc)
            x, y = pyautogui.locateCenterOnScreen(r"../PvPWarsButton.png")
            click(x, y)
            break

    serverRetro()

# JOINING SKYBLOCK RETRO:
def serverRetro():
    while True:
        if pyautogui.locateOnScreen(r"../PvPWarsHub.png") is not None:
            pyautogui.press('t')
            keyboard.write('/server retro')
            keyboard.press('enter')
            break
    checkIsTop()

def checkIsTop():
    while True:
        if pyautogui.locateOnScreen(r"../PvPWarsLeaderBoard.png") is not None:
            pyautogui.press('t')
            keyboard.write('/is top')
            keyboard.press('enter')
            break

    while True:
        if pyautogui.locateOnScreen(r"../IsTopScreen.png") is not None:
            x, y = pyautogui.locateCenterOnScreen(r"../istopGlassPane.png")
            startx = x
            endy = y + 72
            endx = x + 324

            # Cycling through the island top tooltips
            for y in range(y + 36, endy + 36, 36):
                x = startx
                if y == endy:
                    x = x + 36
                    endx = endx - 36
                for x in range(x, endx, 36):
                    time.sleep(.5)

                    win32api.SetCursorPos((x, y))
                    time.sleep(0.25)
                    img = pyautogui.screenshot(region=(x + 16, y - 30, 378, 496))
                    img.save(r"../isTopInfo.png")

                    img = cv2.imread(r"../isTopInfo.png")
                    custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz0123456789$._#ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6'

                    text = tess.image_to_data(img, config=custom_config, output_type='data.frame')
                    df = pd.DataFrame(text)
                    df = df.drop(
                        columns=['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width',
                                 'height', 'conf']).dropna()
                    df = df.drop(df.tail(1).index)
                    df = df.reindex(
                        columns=df.columns.tolist() + ['date', 'time', 'island_leader', 'place', 'worth', 'moderators', 'members'])
                    df = df.astype({'moderators': object, 'members': object})
                    df.reset_index(drop=True, inplace=True)

                    # ENTERING DATE AND HOUR
                    dateAndTime = datetime.datetime.now()
                    date = dateAndTime.strftime("%x")
                    hour = dateAndTime.strftime("%H:00")

                    df.iloc[df['date'].count(), df.columns.get_loc('date')] = date
                    df.iloc[df['hour'].count(), df.columns.get_loc('hour')] = hour

                    # Moving the data to the correct columns
                    for z in range(0, df['text'].count(), 1):
                        value = df['text'].iloc[z]

                        if z == 0:
                            value = value.split('ISLAND')[-1]
                            value = value.split('#')[0]
                            if value == 'axiy':
                                value = 'qxiy'
                            elif value == '_noonie2005':
                                value = 'noonie2005'
                            df.iloc[df['island_leader'].count(), df.columns.get_loc('island_leader')] = value

                        if z == 1:
                            # value = value[-1:12]
                            value = value.split('#')[-1]
                            df.iloc[df['place'].count(), df.columns.get_loc('place')] = value

                        if z == 2:
                            value = value[6:16]
                            df.iloc[df['worth'].count(), df.columns.get_loc('worth')] = value

                            # CHANGING VALUE TO FLOAT VALUE
                            # if value[-1] == 'M':
                            #     floatWorth = float(value[:-1])
                            #     floatWorth = floatWorth * 1000000
                            #
                            # if value[-1] == 'B':
                            #     floatWorth = float(value[:-1])
                            #     floatWorth = floatWorth * 1000000000
                            #
                            # if value[-1] == 'T':
                            #     floatWorth = float(value[:-1])
                            #     floatWorth = floatWorth * 1000000000000
                            #
                            # df.iloc[df['worth_reported'].count(), df.columns.get_loc('worth_reported')] = floatWorth

                        if value == 'MODERATORS':
                            i = z + 1
                            Moderators = []
                            for i in range(i, df['text'].count(), 1):
                                if df['text'].iloc[i] == 'MEMBERS':
                                    break
                                else:
                                    Moderators.append(df['text'].iloc[i])
                            df.iat[df['moderators'].count(), df.columns.get_loc('moderators')] = Moderators

                        if value == 'MEMBERS':
                            i = z + 1
                            Members = []
                            for i in range(i, df['text'].count(), 1):
                                Members.append(df['text'].iloc[i])
                            df.iat[df['members'].count(), df.columns.get_loc('members')] = Members

                    # Dropping the text column and resetting the index
                    df = df.drop(columns=['text']).dropna(axis='index', how='all')
                    df.reset_index(drop=True, inplace=True)

                    df.to_csv(r"../output.csv")

                    df_retroIsTop = pd.concat([df_retroIsTop, df]).reset_index(drop=True)
                    df_retroIsTop.to_csv(r"../retroIsTop.csv")
                    print(df_retroIsTop)

            pyautogui.press("escape")
            break


# JOBS:
schedule.every().day.at("00:20").do(closeMC())  # CLOSE MC AT 12:20 AM EVERY DAY
schedule.every().day.at("00:30").do(openMC())  # OPEN MC AT 12:30 AM EVERY DAY
schedule.every().hour.at(':00').do(checkIsTop())  # CHECK IS TOP EVERY HOUR ON THE HOUR

while True:
    schedule.run_pending()
    time.sleep(1)
