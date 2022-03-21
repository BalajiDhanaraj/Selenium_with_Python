from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")


### this is the check is element present

driver.get("https://www.way2automation.com/")

driver.implicitly_wait(50)

### Mouse Handover

menu = driver.find_element(by=By.XPATH,value="//li[@id='menu-item-27580']//span[contains(text(),'All Courses')]")

time.sleep(2)

action = ActionChains(driver)
action.move_to_element(menu).perform()
time.sleep(2)
driver.find_element(by=By.XPATH,value="//li[@id='menu-item-27595']//span[contains(text(),'Robot Framework')]")


driver.quit()
# driver.close()


































