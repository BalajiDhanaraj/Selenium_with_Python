from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

driver.get("http://way2automation.com")

driver.maximize_window()

title = driver.title

print(title)

assert "Selenium" in title

driver.close()
driver.quit()






















