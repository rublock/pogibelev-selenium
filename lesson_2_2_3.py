import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    num = browser.find_element(By.ID, "input_value")
    res = calc(int(num.text))

    select = browser.find_element(By.ID, "answer")
    select.send_keys(res)

    browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    time.sleep(10)
    browser.quit()
