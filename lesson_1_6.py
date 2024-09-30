from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# установите пакет chromedrivermanager
# pip install chromedrivermanager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

try:
    link_one = "http://suninjuly.github.io/registration1.html"
    link_two = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # замените аргумент, чтобы протестировать другую ссылку
    browser.get(link_one)

    first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input.form-control.first")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input.form-control.second")
    last_name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input.form-control.third")
    email.send_keys("example@mail.com")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
