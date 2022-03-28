from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver as driver
import pytest

# parallel test

def get_data():
    return [

        ("trainer@way2automation.com", "kjsdfbksdf"),
        ("java@way2automation.com", "sdf"),
        ("info@way2automation.com", "sdfsdf")

    ]

def setup_function():
    global driver
    driver = webdriver.Chrome(
        executable_path="/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")
    driver.get("http://facebook.com")


def teardown_function():
    driver.quit()


@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password, get_browser):
    driver = get_browser
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)