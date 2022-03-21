from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")


""" ### Mouse Handover
driver.get("https://www.way2automation.com/")
driver.implicitly_wait(50)


menu = driver.find_element(by=By.XPATH,value="//li[@id='menu-item-27580']//span[contains(text(),'All Courses')]")
time.sleep(2)
action = ActionChains(driver)
action.move_to_element(menu).perform()
time.sleep(2)
driver.find_element(by=By.XPATH,value="//li[@id='menu-item-27595']//span[contains(text(),'Robot Framework')]")

driver.quit()
# driver.close() """



"""### Moving Sliders

driver.get("http://demo.automationtesting.in/Slider.html")
driver.implicitly_wait(60)

slider = driver.find_element(by=By.XPATH,value="//a[@class='ui-slider-handle ui-state-default ui-corner-all']")
   ## getting the location and size of the slider
location = slider.location
size = slider.size

w,h = size['width'],size['height']
print(location,size)
print(w,h)


ActionChains(driver).drag_and_drop_by_offset(slider,w/2,0).perform()
driver.quit()
driver.close()
"""

"""### Resizable

driver.get("https://jqueryui.com/resources/demos/resizable/default.html")
driver.implicitly_wait(60)

resizable = driver.find_element(by=By.XPATH,value="//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")

ActionChains(driver).drag_and_drop_by_offset(resizable,500,500).perform()

driver.quit()
driver.close()"""


##
























