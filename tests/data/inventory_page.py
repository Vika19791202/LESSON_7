from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self, product_name):
        locator = (
            By.XPATH,
            f"//div[contains(@class, 'inventory_item') and .//div[text()='{product_name}']]"
            f"//button[contains(@class, 'btn_inventory')]"
        )
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
