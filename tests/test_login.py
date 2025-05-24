import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators

def test_successful_login(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    wait = WebDriverWait(driver, 10)

    # Переход к форме входа
    login_register_button = wait.until(EC.element_to_be_clickable(locators.LOGIN_REGISTER_BUTTON))
    login_register_button.click()

    # Ввод данных для входа
    email = "testirovanye@test.ru"  # Замените на существующий email
    password = "12345"        # Замените на соответствующий пароль

    email_field = wait.until(EC.visibility_of_element_located(locators.EMAIL_FIELD))
    email_field.send_keys(email)

    password_field = wait.until(EC.visibility_of_element_located(locators.PASSWORD_FIELD))
    password_field.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON))
    login_button.click()

    # Проверка успешного входа
    user_avatar = wait.until(EC.presence_of_element_located(locators.USER_AVATAR))
    user_name = wait.until(EC.visibility_of_element_located(locators.USER_NAME))
    assert "User" in user_name.text
