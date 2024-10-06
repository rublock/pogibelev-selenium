import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    num = browser.find_element(By.ID, "treasure").get_attribute("valuex")

    browser.find_element(By.ID, "answer").send_keys(calc(int(num)))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    time.sleep(10)
    browser.quit()
