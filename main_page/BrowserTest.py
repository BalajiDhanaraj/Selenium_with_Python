from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

driver.get("http://way2automation.com")

driver.maximize_window()

title = driver.title

getphonetxt = driver.find_element_by_xpath("//span[text()='+919711-111-558']")
print(getphonetxt)

print(title)

assert "Selenium" in title

driver.close()
driver.quit()






















