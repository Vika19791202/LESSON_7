import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.ID, "flash")

    @allure.step("Ввод логина: {username}")
    def enter_username(self, username: str) -> None:
        self.find_element(self.USERNAME_FIELD).send_keys(username)

    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password: str) -> None:
        self.find_element(self.PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажатие кнопки Войти")
    def click_login(self) -> None:
        self.find_element(self.LOGIN_BUTTON).click()

    @allure.step("Проверка отображения сообщения об ошибке")
    def is_error_displayed(self) -> bool:
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return True
        except Exception:
            return False


@allure.title("Успешный вход пользователя в систему")
@allure.description("Пользователь вводит валидные данные и попадает в личный кабинет")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_login(driver):
    page = LoginPage(driver)
    page.open_page("https://the-internet.herokuapp.com/login")

    with allure.step("Ввод данных и попытка входа"):
        page.enter_username("tomsmith")
        page.enter_password("SuperSecretPassword!")
        page.click_login()

    with allure.step("Проверка успешного входа"):
        WebDriverWait(driver, 5).until(
            EC.url_contains("/secure")
        )
        assert (
            "/secure" in driver.current_url
        ), (
            "URL не содержит /secure"
        )


@allure.title("Вход с неверным паролем")
@allure.description(
    "Пользователь вводит неверный пароль, видит сообщение об ошибке"
)
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.NORMAL)
def test_login_with_wrong_password(driver):
    page = LoginPage(driver)
    page.open_page("https://the-internet.herokuapp.com/login")

    page.enter_username("tomsmith")
    page.enter_password("wrong")
    page.click_login()

    assert (
        page.is_error_displayed()
    ), (
        "Сообщение об ошибке не отображается"
    )
