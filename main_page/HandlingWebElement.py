from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

print("Total dropdown values are,",len(option))
# driver.close()
# driver.quit()





















