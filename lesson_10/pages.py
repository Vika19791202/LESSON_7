from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url: str) -> None:
        """Открывает страницу по указанному URL."""
        self.driver.get(url)

    def find_element(self, locator: tuple) -> WebElement:
        """Находит элемент на странице по локатору."""
        return self.driver.find_element(*locator)
