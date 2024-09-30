import math
import time
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    res = int(num1) + int(num2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(res))

    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

finally:
    time.sleep(10)
    browser.quit()
