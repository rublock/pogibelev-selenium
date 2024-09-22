import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

try:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get("http://suninjuly.github.io/wait1.html")

    browser.implicitly_wait(5)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    time.sleep(5)
    browser.quit()
