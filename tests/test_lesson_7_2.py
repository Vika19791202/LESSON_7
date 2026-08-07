import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tests.data.login_page import LoginPage
from tests.data.inventory_page import InventoryPage
from tests.data.cart_page import CartPage
from pages.checkout_page import CheckoutPage

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    options = FirefoxOptions()
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_purchase_three_items_and_verify_total(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_product_to_cart("Sauce Labs Onesie")

    inventory_page.go_to_cart()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Ivan")
    checkout_page.enter_last_name("Ivanov")
    checkout_page.enter_postal_code("123456")
    checkout_page.click_continue()

    total_text = checkout_page.get_total_text()

    assert "$58.29" in total_text, f"Ожидалось $58.29, но получено: {total_text}"
