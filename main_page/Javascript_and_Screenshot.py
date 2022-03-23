from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

## Execute the javascript function directly

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")

driver.implicitly_wait(50)
time.sleep(2)

driver.switch_to.frame("iframeResult")
print("In iframe ")
# driver.find_element(by=By.XPATH,value="//input[@id='mySubmit']").click()

driver.execute_script("myFunction()")
driver.switch_to.default_content()

elem = driver.find_element(by=By.ID,value="mySubmit")
driver.execute_script("arguments[0].style.border='3px solid red' ",elem)


print("Out of iframes ")
driver.close()
driver.quit()















