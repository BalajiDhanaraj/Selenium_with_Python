from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

driver.get("https://echoecho.com/htmlforms11.htm")

driver.maximize_window()

wait = WebDriverWait(driver,10)

driver.find_element(by=By.NAME,value="dropdownmenu").send_keys("Milk")

driver.close()
driver.quit()





















