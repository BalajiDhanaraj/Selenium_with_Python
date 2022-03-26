from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

driver.get("https://www.w3schools.com/")
driver.maximize_window()
driver.implicitly_wait(1)

print(driver.find_element(by=By.XPATH,value="//button[@id='learntocode_searchbtn']").value_of_css_property("font-size"))
print(driver.find_element(by=By.XPATH,value="//button[@id='learntocode_searchbtn']").value_of_css_property("background"))






