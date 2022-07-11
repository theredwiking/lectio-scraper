import time
import os
from utils import saveData
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

load_dotenv()

# Runs firefox in headless mode
options = FirefoxOptions()
options.add_argument("--headless")

browser = webdriver.Firefox(options=options, executable_path=r'./geckodriver')
browser.get("%s/login.aspx"%os.getenv('BASEURL'))

# Logges into lectio
browser.find_element(By.ID, "username").send_keys(os.getenv('STUDENT'))
browser.find_element(By.ID, "password").send_keys(os.getenv('PASSWD'))
browser.find_element(By.ID, "m_Content_submitbtn2").click()

# Makes sure website is loaded get_url = driver.current_url
time.sleep(1)

# Goes to url of this weeks classes &week=272022
browser.get("%s/SkemaNy.aspx?type=elev&elevid=%s&week=262022"%(os.getenv('BASEURL'), os.getenv('STUDENTID')))

time.sleep(1)

for days in range(2, 7):
    week = browser.find_element(By.XPATH, "/html/body/div[1]/form[2]/section/div[3]/div[2]/table/tbody/tr[1]/td").text
    day = "/html/body/div[1]/form[2]/section/div[3]/div[2]/table/tbody/tr[4]/td[%d]"%days
    try:
        browser.find_element(By.XPATH, day)
        for lessons in range(1, 10):
            lesson = "%s/div[1]/a[%d]"%(day, lessons)
            try:
                data = browser.find_element(By.XPATH, lesson).get_attribute("data-additionalinfo")
                saveData(data, week)
            except:
                print("Lesson not found")
                pass
    except:
        print("Day not found")
        pass
    
time.sleep(1)

browser.quit()