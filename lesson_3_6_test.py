import math
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv

load_dotenv()

stepik_login = os.environ.get('STEPIK_LOGIN')
stepik_password = os.environ.get('STEPIK_PASSWORD')

class TestMainPage1():
    def test_login_into_stepik(self, browser):
        try:
            browser.get('https://stepik.org/lesson/236895/step/1')
            button = (WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'navbar__auth_login'))
            ))
            button.click()

            login = (WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.ID, "id_login_email"))
            ))
            login.send_keys(stepik_login)

            browser.find_element(By.ID, "id_login_password").send_keys(stepik_password)
            browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

            answer = math.log(int(time.time()))

            textarea = (WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area"))
            ))
            textarea.clear()
            textarea.send_keys(answer)

            browser.find_element(By.CLASS_NAME, "submit-submission").click()

            result_text = (WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
            ))

            print(result_text.text())

        except Exception as e:
            print(f"Произошла ошибка: {e}")

        finally:
            time.sleep(5)
            browser.quit()
