import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


def get_str_from_link(link):
    browser.get(link)

    browser.find_element(
        By.CSS_SELECTOR, "div.first_block div.first_class input.form-control.first"
    ).send_keys("Ivan")
    browser.find_element(
        By.CSS_SELECTOR, "div.first_block div.second_class input.form-control.second"
    ).send_keys("Petrov")
    browser.find_element(
        By.CSS_SELECTOR, "div.first_block div.third_class input.form-control.third"
    ).send_keys("example@mail.com")
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

    time.sleep(5)

    return browser.find_element(By.TAG_NAME, "h1").accessible_name


def test_link1():
    assert get_str_from_link("http://suninjuly.github.io/registration1.html") == "Congratulations! You have successfully registered!", "registration is failed"

def test_link2():
    assert get_str_from_link("http://suninjuly.github.io/registration2.html") == "Congratulations! You have successfully registered!", "registration is failed"


if __name__ == "__main__":
    pytest.main()
