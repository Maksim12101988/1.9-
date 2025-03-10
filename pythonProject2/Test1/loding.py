import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from page_object import SkillBoxPage


def setup():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def teardown(driver):
    time.sleep(5)
    driver.quit()


def test_skill_box_page():
    driver = setup()
    try:
        skill_box_page = SkillBoxPage(driver)

        skill_box_page.open()
        skill_box_page.click_catalog_button()
        skill_box_page.click_search_input()
        skill_box_page.enter_search_text("тестирование")

        if skill_box_page.check_hints_presence():
            print("Подсказки присутствуют")
            print("Содержимое подсказок:", skill_box_page.get_hints_content())
        else:
            print("Подсказки отсутствуют или пустые")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        teardown(driver)


if __name__ == "__main__":
    test_skill_box_page()
