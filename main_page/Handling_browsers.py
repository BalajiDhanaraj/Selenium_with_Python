import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

driver = webdriver.Chrome("/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

## Handling push notificatons

driver.implicitly_wait(50)
time.sleep(2)

# chrome_options = Options()

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# chrome_options.headless = True
#
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)

driver.get("http://www.google.com")
driver.maximize_window()

print(driver.title)













