import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("имя")
    browser.find_element(By.NAME, "lastname").send_keys("фамилия")
    browser.find_element(By.NAME, "email").send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    browser.find_element(By.NAME, "file").send_keys(file_path)

    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    time.sleep(5)
    browser.quit()
