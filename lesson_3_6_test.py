import pytest
import math
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv

load_dotenv()

stepik_login = os.environ.get("STEPIK_LOGIN")
stepik_password = os.environ.get("STEPIK_PASSWORD")

urls = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]


class TestMainPage1():

    @pytest.mark.parametrize("url", urls)
    def test_login_into_stepik(self, browser, url):
        browser.implicitly_wait(10)
        browser.get(url)
        button_login_in = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "navbar__auth_login"))
        )
        button_login_in.click()

        browser.find_element(By.ID, "id_login_email").send_keys(stepik_login)
        browser.find_element(By.ID, "id_login_password").send_keys(stepik_password)
        browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

        time.sleep(3)
        textarea_math = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area"))
        )
        textarea_math.send_keys(str(math.log(int(time.time()))))

        button_submit = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button_submit.click()

        result_text = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )

        assert result_text.text == 'Correct!', 'not Correct! str'

if __name__ == "__main__":
    pytest.main()
