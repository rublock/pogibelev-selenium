import time
from os import times

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager




def test_exception1():
    try:
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.get("http://selenium1py.pythonanywhere.com/")
        time.sleep(5) # human read
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.get("http://selenium1py.pythonanywhere.com/")
        time.sleep(5) # human read
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally: 
        browser.quit()
