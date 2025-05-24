import random
import string
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
from selenium.webdriver.common.by import By

def generate_unique_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{username}@example.com"

def test_successful_registration(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    wait = WebDriverWait(driver, 10)

    # Переход к форме регистрации
    login_register_button = wait.until(EC.element_to_be_clickable(locators.LOGIN_REGISTER_BUTTON))
    login_register_button.click()

    no_account_button = wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON))
    no_account_button.click()

    # Заполнение формы регистрации
    email = generate_unique_email()
    password = "TestPassword123"

    email_field = wait.until(EC.visibility_of_element_located(locators.EMAIL_FIELD))
    email_field.send_keys(email)

    password_field = wait.until(EC.visibility_of_element_located(locators.PASSWORD_FIELD))
    password_field.send_keys(password)

    confirm_password_field = wait.until(EC.visibility_of_element_located(locators.CONFIRM_PASSWORD_FIELD))
    confirm_password_field.send_keys(password)

    create_account_button = wait.until(EC.element_to_be_clickable(locators.CREATE_ACCOUNT_BUTTON))
    create_account_button.click()

    # Проверка успешной регистрации
    user_avatar = wait.until(EC.presence_of_element_located(locators.USER_AVATAR))
    user_name = wait.until(EC.visibility_of_element_located(locators.USER_NAME))
    assert "User" in user_name.text
