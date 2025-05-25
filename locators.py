from selenium.webdriver.common.by import By

LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

EMAIL_FIELD = (By.NAME, "email")
PASSWORD_FIELD = (By.NAME, "password")
CONFIRM_PASSWORD_FIELD = (By.NAME, "submitPassword")

USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")

POST_AD_BUTTON = (By.XPATH, "//*[text()='Разместить объявление']")

MODAL_TITLE = (By.XPATH, "//*[text()='Чтобы разместить объявление, авторизуйтесь']")

AD_TITLE_FIELD = (By.NAME, "name")
AD_DESCRIPTION_FIELD = (By.XPATH, "//textarea[@placeholder='Описание товара']")
AD_PRICE_FIELD = (By.NAME, "price")

AD_CATEGORY_DROPDOWN = (By.XPATH, "(//*[contains(@class, 'dropDownMenu_arrowDown')])[1]")
AD_CITY_DROPDOWN = (By.XPATH, "(//*[contains(@class, 'dropDownMenu_arrowDown')])[2]")


AD_CONDITION_NEW = (
    By.XPATH,
    "//label[normalize-space(text())='Новый']"
)

AD_CONDITION_USED = (
    By.XPATH,
    "//label[normalize-space(text())='Б/У']"
)


PUBLISH_BUTTON = (By.XPATH, "//*[text()='Опубликовать']")
PROFILE_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")

MY_ADS_TITLES = (By.CSS_SELECTOR, "div[class*='card'] h2")

