from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(executable_path="/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

driver.get(
    "https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C550525805943%7Ce%7Cfacebook%20sign%20up%7C&placement=&creative=550525805943&keyword=facebook%20sign%20up&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696221832%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-5066597374%26loc_physical_ms%3D1007809%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQjwuMuRBhCJARIsAHXdnqMFDkshlTRxuLnkW-Q1wI0WS_3v5fkHSbCU0BHg_fl9MmHeJV55PQwaAvh0EALw_wcB")

driver.maximize_window()

## implicitly wait is use to delay the website, this tie down with driver not the element
# driver.implicitly_wait(40)

Firstname = driver.find_element(by=By.XPATH,value="//*[@name='firstname']").send_keys("walker")

## explicity wait is use to delay the particular element in web
WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,"//*[@name='lastname']"))).send_keys('walker')

# Lastname = driver.find_element(by=By.XPATH,value="//*[@name='lastname']").send_keys("paul")

Mobileno = driver.find_element(by=By.XPATH,value="//*[contains(@name,'reg_email__')]").send_keys("9839384948")

Password = driver.find_element(by=By.XPATH,value="//*[@type='password']").send_keys("Walker")
#
# Day = driver.find_element_by_xpath("//*[@id='day']/option[17]")
# Month = driver.find_element_by_xpath("//*[@id='month']/option[7]")
# Year = driver.find_element_by_xpath("//*[@id='year']/option[@value='1999']")
Gender = driver.find_element(by=By.XPATH,value="//label[contains(.,'Male')]").click()


# time.sleep(20)
driver.close()
driver.quit()
