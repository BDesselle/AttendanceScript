#Import Selenium webdrive
from selenium import webdriver;
import pyautogui;
import time;
import datetime;

#Setup browser
driver = webdriver.Chrome(executable_path= r'chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
driver.maximize_window()

#Go To "URL"
driver.get("https://airtable.com/shrEawWXvMldYbm5Q")

#Other Variables | Cursor Coordinates - Run CursorPosition.py with the cursor over what needs to be clicked to get the coordinates
projectManager = pyautogui.position(x=1701, y=591)
section = pyautogui.position(x=1701, y=766)
date = pyautogui.position(x=1701, y=908)
present = pyautogui.position(x=1701, y=1025)
submit = pyautogui.position(x=1701, y=1760)
clickAway = pyautogui.position(x=622, y=741)
today = datetime.datetime.now()


#PyAutoGUI
#Project Manager - Adds the Project Manager
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(projectManager) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite('Brandon Desselle') #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.press('enter') #Enter

#Section
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(section) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite('WEBPT5') #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.press('enter') #Enter

#Date
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(date) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite(today.strftime("%m") + "/" + today.strftime("%d") + "/" + today.strftime("%Y")) #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(clickAway)

#Present
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(x=1668, y=1025) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite('Alan Lemasney') #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.press('enter') #Enter

time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(x=1668, y=1025) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite('Alejandro Baez Torres') #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.press('enter') #Enter

time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(x=1668, y=1025) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite('Brandy Rimes') #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.press('enter') #Enter

time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(x=1668, y=1025) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite('Christian MacDonald') #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.press('enter') #Enter

time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(x=1668, y=1025) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite('Gaetano Daidone') #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.press('enter') #Enter

time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(x=1668, y=1025) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite('Jason Barr') #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.press('enter') #Enter

time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(x=1668, y=1025) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite('Oscar Lopez') #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.press('enter') #Enter

time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.click(x=1668, y=1025) #Click
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.typewrite('Sammy Chang') #Types String
time.sleep(2) #Sleep because Airtable is a slow F U C K
pyautogui.press('enter') #Enter

#Submit
time.sleep(2) #Sleep because Airtable is a slow F U C K
#pyautogui.click(submit) #Click
pyautogui.moveTo(submit) #Move To - Testing | To have the ability to remove non-present students
time.sleep(2) #Sleep because Airtable is a slow F U C K