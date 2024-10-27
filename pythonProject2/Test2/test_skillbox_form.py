from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page_objects import SkillBoxPage

def test_skillbox_form():
    # Настройка драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Открытие страницы Skillbox
        skill_box_page = SkillBoxPage(driver)
        driver.get("https://skillbox.ru/")

        # Ввод имени и номера телефона
        skill_box_page.enter_name("Test")
        skill_box_page.enter_phone("111 111 11 11")
        skill_box_page.enter_email("test.ru")

        # Нажатие кнопки
        skill_box_page.click_submit_button()

        # Проверка появления сообщений об ошибках
        skill_box_page.check_phone_error()
        skill_box_page.check_email_error()

    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "__main__":
    test_skillbox_form()
