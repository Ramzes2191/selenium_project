import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Selenium Manager will auto-download the appropriate driver
    options = Options()
    options.add_argument("--headless")  # run without UI
    options.add_argument("--no-sandbox")  # required in many CI environments
    options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm size on Linux

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_successful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    input_login = driver.find_element(By.ID, "username")
    input_login.clear()
    input_login.send_keys("tomsmith")

    input_password = driver.find_element(By.ID, "password")
    input_password.clear()
    input_password.send_keys("SuperSecretPassword!")

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    alert = driver.find_element(By.ID, "flash")
    if alert.text == "You logged into a secure area!\n×":
        print("Успешная авторизация")
        assert alert.text == "You logged into a secure area!\n×"

def test_unsuccessful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    input_login = driver.find_element(By.ID, "username")
    input_login.clear()
    input_login.send_keys(123)

    input_password = driver.find_element(By.ID, "password")
    input_password.clear()
    input_password.send_keys(123)

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    alert = driver.find_element(By.ID, "flash")
    if alert.text == "Your username is invalid!\n×":
        print("Неуспешная авторизация")
        assert alert.text == "Your username is invalid!\n×"