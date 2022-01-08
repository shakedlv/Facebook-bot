from selenium import webdriver
from selenium.webdriver import Keys
from  selenium.webdriver.common.by import  By
from time import  sleep
import datetime
import random

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get("https://www.facebook.com")


_input = input("Press enter after login")

driver.get("https://www.facebook.com/189917291362525/posts/1608121936208713/")

_input = input("Press enter after replay box clicked")

while True:
    time = datetime.datetime.now()
    if 7 <= time.hour < 12 or 13 <= time.hour < 17 or 18 <= time.hour <= 21:
        try:
            box = "//*[@aria-label='Reply to Shaked Levy']"
            replyBox = driver.find_element(By.XPATH, box)
            emoj = driver.find_elements(By.XPATH, "//*[@aria-label='Insert an emoji']")
            emoj[1].click()
            sleep(1)
            animal = driver.find_element(By.XPATH, "//*[@aria-label='Animals & Nature']")
            animal.click()
            sleep(1)
            meat = driver.find_element(By.XPATH,
                                       "//*[@src='https://static.xx.fbcdn.net/images/emoji.php/v9/tb5/1/28/1f969.png']")
            meat.click()
            replyBox.send_keys(Keys.ENTER)

        except Exception as e:
            print("[ERROR]" + e)
        nextTime = random.randint(60 * 2, 60 * 5)
        sleep(nextTime)
