import pyautogui

screen_width, screen_height = pyautogui.size()
im1 = pyautogui.screenshot(region=(screen_width*.85, screen_height*.3, screen_width*.15, screen_height*.5))
im1.save(r"C:\Users\droc1\Desktop\Python\Discord Bot\savedimage.png")
