import pytest
import allure
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

@allure.epic('Авторизация')
@allure.feature('Авторизация с валидными данными')
@allure.title('Успешная авторизация с валидными данными')
@allure.description('Успешная авторизация при вводе login = tomsmith')
def test_successful_login(driver):
    with allure.step('Отправка запроса'):
        driver.get("https://the-internet.herokuapp.com/login")
    with allure.step('Поиск элемента username'):
        input_login = driver.find_element(By.ID, "username")
    with allure.step('Очистка поля username'):
        input_login.clear()
    with allure.step('Ввод логина tomsmith'):
        input_login.send_keys("tomsmith")

    with allure.step('Поиск элемента password'):
        input_password = driver.find_element(By.ID, "password")
    with allure.step('Очистка поля password'):
        input_password.clear()
    with allure.step('Ввод пароля SuperSecretPassword!'):
        input_password.send_keys("SuperSecretPassword!")

    with allure.step('Поиск кнопки'):
        button = driver.find_element(By.TAG_NAME, "button")
    with allure.step('Нажатие кнопки'):
        button.click()

    with allure.step('Поиск элемента flash'):
        alert = driver.find_element(By.ID, "flash")
    with allure.step('Тест успешной авторизации'):
        assert alert.text == "You logged into a secure area!\n×"


@allure.epic('Авторизация')
@allure.feature('Авторизация с невалидными данными')
@allure.title('Неуспешная авторизация с невалидными данными')
@allure.description('Неуспешная авторизация при вводе login = 123')
def test_unsuccessful_login(driver):
    with allure.step('Отправка запроса'):
        driver.get("https://the-internet.herokuapp.com/login")

    with allure.step('Поиск элемента username'):
        input_login = driver.find_element(By.ID, "username")
    with allure.step('Очистка поля username'):
        input_login.clear()
    with allure.step('Ввод логина 123'):
        input_login.send_keys(123)

    with allure.step('Поиск элемента password'):
        input_password = driver.find_element(By.ID, "password")
    with allure.step('Очистка поля password'):
        input_password.clear()
    with allure.step('Ввод пароля 123'):
        input_password.send_keys(123)

    with allure.step('Поиск кнопки'):
        button = driver.find_element(By.TAG_NAME, "button")
    with allure.step('Нажатие кнопки'):
        button.click()

    with allure.step('Поиск элемента flash'):
        alert = driver.find_element(By.ID, "flash")
    with allure.step('Тест неуспешной авторизации'):
        assert alert.text == "Your username is invalid!\n×"
