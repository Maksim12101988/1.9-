from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SkillBoxPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://skillbox.ru/")

    def click_catalog_button(self):
        catalog_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/header/div[1]/div/button'))
        )
        catalog_button.click()

    def click_search_input(self):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/header/div[2]/div[2]/div[1]/button'))
        )
        search_input.click()

    def enter_search_text(self, text):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div/div[3]/section/div/div/div/label/input'))
        )
        search_input.clear()
        search_input.send_keys(text)

    def check_hints_presence(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/section/div/div/ul'))
        ) is not None

    def get_hints_content(self):
        hints = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/section/div/div/ul/li'))
        )
        return [hint.text for hint in hints]
