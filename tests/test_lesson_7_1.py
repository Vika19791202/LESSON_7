import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from tests.data.calculator_page import CalculatorPage

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator_with_page_object(driver):
    calculator = CalculatorPage(driver)
    calculator.open()
    calculator.set_delay(45)
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    result = calculator.get_result()
    assert result == "15", f"Ожидалось '15', но получено: '{result}'"