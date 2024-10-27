from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SkillBoxPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        input_name = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/section/div/div/div/form/div[1]/div/label/input")
        input_name.send_keys(name)

    def enter_phone(self, phone):
        input_phone = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/section/div/div/div/form/div[2]/div/div/label/div/input")
        input_phone.send_keys(phone)

    def enter_email(self, email):
        input_email = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/section/div/div/div/form/div[3]/div/label/input")
        input_email.send_keys(email)

    def click_submit_button(self):
        button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/section/div/div/div/form/div[4]/div/button")
        button.click()

    def check_phone_error(self):
        phone_error = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/div/div/div/form/div[2]/div/div/span"))
        )
        assert phone_error.text == "Неправильный номер телефона", "Ошибка: Сообщение об ошибке номера телефона не соответствует ожидаемому"

    def check_email_error(self):
        email_error = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/div/div/div/form/div[3]/div/span"))
        )
        assert email_error.text == "Неправильная электронная почта", "Ошибка: Сообщение об ошибке email не соответствует ожидаемому"
