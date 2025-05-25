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

class TestRegistration:
    def test_successful_registration(driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        

        login_register_button = wait.until(EC.element_to_be_clickable(locators.LOGIN_REGISTER_BUTTON))
        login_register_button.click()

        no_account_button = wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON))
        no_account_button.click()

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

        user_avatar = wait.until(EC.presence_of_element_located(locators.USER_AVATAR))
        user_name = wait.until(EC.visibility_of_element_located(locators.USER_NAME))
        assert "User" in user_name.text

    def test_registration_invalid_email(driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()

        email_field = wait.until(EC.visibility_of_element_located(locators.EMAIL_FIELD))
        email_field.send_keys("*******@*******.***")

        password_field = wait.until(EC.visibility_of_element_located(locators.PASSWORD_FIELD))
        password_field.send_keys("12345")

        confirm_password_field = wait.until(EC.visibility_of_element_located(locators.CONFIRM_PASSWORD_FIELD))
        confirm_password_field.send_keys("12345")

        wait.until(EC.element_to_be_clickable(locators.CREATE_ACCOUNT_BUTTON)).click()
        error_message = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Ошибка']"))
        )
        assert "Ошибка" in error_message.text

        email_wrapper = email_field.find_element(By.XPATH, "./parent::*")
        border_color = email_wrapper.value_of_css_property("border-color")
        assert border_color.startswith("rgb(255")

        pwd_wrapper = password_field.find_element(By.XPATH, "./parent::*")
        border_color_pwd = pwd_wrapper.value_of_css_property("border-color")
        assert border_color.startswith("rgb(255")

        conf_wrapper = confirm_password_field.find_element(By.XPATH, "./parent::*")
        border_color_conf = conf_wrapper.value_of_css_property("border-color")
        assert border_color.startswith("rgb(255")

    def test_registration_repeat_email(driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(locators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()

        email_field = wait.until(EC.visibility_of_element_located(locators.EMAIL_FIELD))
        email_field.send_keys("testirovanye@test.ru")

        password_field = wait.until(EC.visibility_of_element_located(locators.PASSWORD_FIELD))
        password_field.send_keys("12345")

        confirm_password_field = wait.until(EC.visibility_of_element_located(locators.CONFIRM_PASSWORD_FIELD))
        confirm_password_field.send_keys("12345")

        wait.until(EC.element_to_be_clickable(locators.CREATE_ACCOUNT_BUTTON)).click()

        error_message = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Ошибка']"))
        )
        assert "Ошибка" in error_message.text

        email_wrapper = email_field.find_element(By.XPATH, "./parent::*")
        border_color = email_wrapper.value_of_css_property("border-color")
        assert border_color.startswith("rgb(255")

        pwd_wrapper = password_field.find_element(By.XPATH, "./parent::*")
        border_color_pwd = pwd_wrapper.value_of_css_property("border-color")
        assert border_color.startswith("rgb(255")

        conf_wrapper = confirm_password_field.find_element(By.XPATH, "./parent::*")
        border_color_conf = conf_wrapper.value_of_css_property("border-color")
        assert border_color.startswith("rgb(255")