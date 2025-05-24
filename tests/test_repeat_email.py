from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
from selenium.webdriver.common.by import By

def test_registration_repeat_email(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    wait.until(EC.element_to_be_clickable(locators.LOGIN_REGISTER_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()

    # Вводим некорректный email и пароль/подтверждение
    email_field = wait.until(EC.visibility_of_element_located(locators.EMAIL_FIELD))
    email_field.send_keys("testirovanye@test.ru")

    password_field = wait.until(EC.visibility_of_element_located(locators.PASSWORD_FIELD))
    password_field.send_keys("12345")

    confirm_password_field = wait.until(EC.visibility_of_element_located(locators.CONFIRM_PASSWORD_FIELD))
    confirm_password_field.send_keys("12345")

    # Жмём "Создать аккаунт"
    wait.until(EC.element_to_be_clickable(locators.CREATE_ACCOUNT_BUTTON)).click()

    # 1) Проверяем, что под полем Email появилось сообщение "Ошибка"
    error_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Ошибка']"))
    )
    assert "Ошибка" in error_message.text

    # 2) Проверяем, что обёртка поля Email выделена красным
    email_wrapper = email_field.find_element(By.XPATH, "./parent::*")
    border_color = email_wrapper.value_of_css_property("border-color")
    assert border_color.startswith("rgb(255")

    # 3) Аналогично для поля Пароль
    pwd_wrapper = password_field.find_element(By.XPATH, "./parent::*")
    border_color_pwd = pwd_wrapper.value_of_css_property("border-color")
    assert border_color.startswith("rgb(255")

    # 4) И для поля Повторите пароль
    conf_wrapper = confirm_password_field.find_element(By.XPATH, "./parent::*")
    border_color_conf = conf_wrapper.value_of_css_property("border-color")
    assert border_color.startswith("rgb(255")