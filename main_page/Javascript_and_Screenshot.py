from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome("/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

"""## Execute the javascript function directly

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")

driver.implicitly_wait(50)
time.sleep(2)


## This is custom methond for screenshot.

def capture_screenshot(d, name):
    file_name = "/Volumes/Macintosh HD/For Mac/python project/Selenium_with_Python/main_page/screenshot/Test_" + name + "_" + time.asctime().replace(
        ":", "_") + ".png"
    d.save_screenshot(file_name)


driver.switch_to.frame("iframeResult")
print("In iframe ")
# driver.find_element(by=By.XPATH,value="//input[@id='mySubmit']").click()

driver.execute_script("myFunction()")

driver.switch_to.default_content()

# elem = driver.find_element(by=By.ID,value="mySubmit")
# driver.execute_script("arguments[0].style.border='3px solid red' ",elem)

capture_screenshot(driver, "Test2")

print("Out of iframes ")
driver.close()
driver.quit()
"""

## Taking the full screenshot of the website

driver.get("https://www.w3schools.com/")
driver.maximize_window()
driver.implicitly_wait(50)
time.sleep(2)

chrome_options = webdriver.ChromeOptions()

print(driver.get_window_size())



# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
driver.find_element(by=By.TAG_NAME,value="body").screenshot("/Volumes/Macintosh HD/For Mac/python project/Selenium_with_Python/main_page/screenshot/full.png")

# driver.quit()
# driver.close()




