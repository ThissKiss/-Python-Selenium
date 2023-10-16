""""
Basic test
"""
import pytest
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_smoke():
    """"
    SMK-1. Smoke test
    """
chrome_options = Options()
chrome_options.add_argument("--no sandbox")
chrome_options.add_argument("start-maximized") # открываем на полный экран
chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
chrome_options.add_argument("--disable-extensions") # отключаем расширения
chrome_options.add_argument("--disable-gpu")



service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url='https://testqastudio.me/')

element = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]')
element.click()

sku = driver.find_element(by=By.CSS_SELECTOR, value='[class="sku"]')

assert sku.text == 'C0MSSDSUM7', 'Unexpected sku for "ДИВВИНА Журнальный столик"'