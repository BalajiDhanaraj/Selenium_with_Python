from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

"""## Switch to alert 
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.implicitly_wait(50)
time.sleep(2)

driver.find_element(by=By.XPATH,value="//input[@title='Sign in']").click()

alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()

driver.close()
driver.quit()"""

"""## Switch to Iframes

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")

driver.implicitly_wait(50)
time.sleep(2)

driver.switch_to.frame("iframeResult")
driver.find_element(by=By.XPATH,value="//input[@id='mySubmit']").click()

driver.switch_to.default_content()

frames = driver.find_elements(by=By.TAG_NAME,value="iframe")

for frame in frames:
    print(frame.get_attribute("id"))


driver.close()
driver.quit()"""

## Switch to another tab

driver.get("http://www.way2automation.com/")

driver.implicitly_wait(50)
time.sleep(2)



driver.close()
driver.quit()






