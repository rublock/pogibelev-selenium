import math
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

try:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    browser.find_element(By.ID, "book").click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    num = browser.find_element(By.ID, "input_value")
    res = calc(int(num.text))

    browser.find_element(By.ID, "answer").send_keys(res)
    browser.find_element(By.ID, "solve").click()

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    time.sleep(5)
    browser.quit()
