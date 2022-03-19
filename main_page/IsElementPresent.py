from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")


### this is the check is element present
"""
driver.get("https://www.wikipedia.org/")


def is_element_present(locator,path):
    try:
        driver.find_element(by=locator,value=path)
        return True
    except NoSuchElementException:
        return False

print(is_element_present(By.XPATH,"//input[@id='searchInput']"))

"""

driver.get("https://echoecho.com/htmlforms09.htm")

driver.implicitly_wait(700)

# driver.find_element(by=By.XPATH,value="//td[@class='table8']//input[1]").click()

for n in range(1,4):
    driver.find_element(by=By.XPATH, value="//td[@class='table8']//input["+str(n)+"]").click()


driver.quit()
# driver.close()










