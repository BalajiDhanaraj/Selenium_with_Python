from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.implicitly_wait(50)
time.sleep(2)

driver.find_element(by=By.XPATH,value="//input[@title='Sign in']").click()

alert = driver.switch_to.alert

print(alert.text)
time.sleep(2)
alert.accept()

driver.close()
driver.quit()
