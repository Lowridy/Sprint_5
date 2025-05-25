import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators

def test_successful_logout(driver, base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)

    login_register_button = wait.until(EC.element_to_be_clickable(locators.LOGIN_REGISTER_BUTTON))
    login_register_button.click()

    email = "testirovanye@test.ru" 
    password = "12345"  

    email_field = wait.until(EC.visibility_of_element_located(locators.EMAIL_FIELD))
    email_field.send_keys(email)

    password_field = wait.until(EC.visibility_of_element_located(locators.PASSWORD_FIELD))
    password_field.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON))
    login_button.click()

    user_avatar = wait.until(EC.presence_of_element_located(locators.USER_AVATAR))
    user_name = wait.until(EC.visibility_of_element_located(locators.USER_NAME))
    assert "User" in user_name.text

    logout_button = wait.until(EC.element_to_be_clickable(locators.LOGOUT_BUTTON))
    logout_button.click()

    login_register_button = wait.until(EC.element_to_be_clickable(locators.LOGIN_REGISTER_BUTTON))
    assert login_register_button.is_displayed()
