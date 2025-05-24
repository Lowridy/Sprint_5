import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
from selenium.webdriver.common.by import By

def test_post_ad_unauthorized(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    driver.find_element(*locators.POST_AD_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locators.MODAL_TITLE))
    assert driver.find_element(*locators.MODAL_TITLE).text == "Чтобы разместить объявление, авторизуйтесь"


def test_post_ad_authorized(driver): 
    wait = WebDriverWait(driver, 10)
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    # Авторизация
    wait.until(EC.element_to_be_clickable(locators.LOGIN_REGISTER_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(locators.EMAIL_FIELD)).send_keys("testirovanye3@test.ru")
    wait.until(EC.visibility_of_element_located(locators.PASSWORD_FIELD)).send_keys("12345")
    wait.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON)).click()
    wait.until(EC.presence_of_element_located(locators.USER_AVATAR))

    # Ждём появления аватара — сигнал, что авторизация завершена
    wait.until(EC.presence_of_element_located(locators.POST_AD_BUTTON))
    post_ad_button = driver.find_element(*locators.POST_AD_BUTTON)
    wait.until(lambda d: post_ad_button.is_displayed() and post_ad_button.is_enabled())
    post_ad_button.click()

    # Заполнение объявления
    wait.until(EC.visibility_of_element_located(locators.AD_TITLE_FIELD)).send_keys("Продам гараж")

    # Выбор категории
    wait.until(EC.element_to_be_clickable(locators.AD_CATEGORY_DROPDOWN)).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Книги')]"))).click()

    # Город
    wait.until(EC.element_to_be_clickable(locators.AD_CITY_DROPDOWN)).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Новосибирск')]"))).click()

    # Описание товара
    wait.until(EC.presence_of_element_located(locators.AD_DESCRIPTION_FIELD))
    desc_field = driver.find_element(*locators.AD_DESCRIPTION_FIELD)
    desc_field.send_keys("Здесь может быть ваша реклама")

    # Ждём и повторно получаем input "Стоимость"
    wait.until(EC.presence_of_element_located(locators.AD_PRICE_FIELD))
    price_field = driver.find_element(*locators.AD_PRICE_FIELD)
    driver.execute_script("arguments[0].scrollIntoView(true);", price_field)
    price_field.send_keys("1000")

    # Состояние товара
    wait.until(EC.element_to_be_clickable(locators.AD_CONDITION_USED)).click()

    # Публикация объявления
    wait.until(EC.element_to_be_clickable(locators.PUBLISH_BUTTON)).click()

    # Ждём, что публикация завершена и страница обновилась
    wait.until(EC.staleness_of(driver.find_element(*locators.USER_AVATAR)))

    # Переход в профиль
    wait.until(EC.presence_of_element_located(locators.USER_AVATAR))
    profile_btn = wait.until(EC.element_to_be_clickable(locators.USER_AVATAR))
    profile_btn.click()


    # Теперь ждём, что заголовки объявлений отрисуются
    ad_titles = wait.until(EC.presence_of_all_elements_located(locators.MY_ADS_TITLES))

    # Проверка, что хотя бы одно объявление присутствует
    assert any("Продам гараж" in el.text for el in ad_titles)
