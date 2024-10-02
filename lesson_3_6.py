import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


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
            login.send_keys('e-mail')

            browser.find_element(By.ID, "id_login_password").send_keys('password')
            browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

        except Exception as e:
            print(f"Произошла ошибка: {e}")

        finally:
            time.sleep(5)
            browser.quit()
