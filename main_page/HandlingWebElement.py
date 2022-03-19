from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

# driver.get("https://echoecho.com/htmlforms11.htm")

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

wait = WebDriverWait(driver,10)
#
# driver.find_element(by=By.NAME,value="dropdownmenu").send_keys("Milk")

## use to select the dropdown list
dropdown = driver.find_element(by=By.ID,value="searchLanguage")
select = Select(dropdown)
select.select_by_value("pl")

option = driver.find_elements(by=By.TAG_NAME,value="option")

for op in option:
    print("Text is :",op.text,"Lang is :"+op.get_attribute("lang"))

# print("Total dropdown values are,",len(option))

print("------------------------------------------------------------")

## find the link by use the tag name
links = driver.find_elements(by=By.TAG_NAME,value="a")
print(len(links))
for link in links:
    print("Text is:",link.text," --URL is :"+link.get_attribute("href"))

## get the value from specfiy block
print("---------------------------------------------")
block = driver.find_element(by=By.XPATH,value="//*[@class='other-projects']/div[1]")

print(block.find_elements(by=By.TAG_NAME,value="a").__getitem__(0).text)


time.sleep(1)

driver.quit()
driver.close()
















