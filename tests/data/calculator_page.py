from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        element = self.driver.find_element(By.ID, "delay")
        element.clear()
        element.send_keys(str(delay))

    def click_button(self, text):
        locator = (By.XPATH, f"//span[normalize-space()='{text}']")
        button = self.wait.until(lambda d: d.find_element(*locator))
        button.click()

    def get_result(self):
        locator = (By.CSS_SELECTOR, "#calculator .screen")
        self.wait.until(lambda d: d.find_element(*locator).text.strip() == "15")
        return self.driver.find_element(*locator).text.strip()