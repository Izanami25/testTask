import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_fields import TestForm
import time

@pytest.fixture
def browser():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Test Form Automation")
@pytest.mark.usefixtures("browser")
class TestDemoQAForm:

    @allure.title("Отправка формы со всеми обязательными полями")
    def test_fill_form_with_valid_data(self, browser):
        demoqa_page = TestForm(browser)
        demoqa_page.load()
        demoqa_page.fill_form("Ulan", "Zhukush", "ulan@example.com", "Male", "77079567256")
        time.sleep(3)

        # Проверки успешного заполнения формы
        assert demoqa_page.is_form_submission_successful()

    @allure.title("Отправка формы без заполнения всех полей")
    def test_fill_form_with_empty_data(self, browser):
        demoqa_page = TestForm(browser)
        demoqa_page.load()
        demoqa_page.fill_form("", "", "", "", "")

        # Проверки ошибок при заполнении формы c пустыми полями
        assert demoqa_page.is_fields_error_displayed()
    
    @allure.title("Отправка формы без заполнения FirstName")
    def test_fill_form_with_empty_first_name(self, browser):
        demoqa_page = TestForm(browser)
        demoqa_page.load()
        demoqa_page.fill_form("", "Zhukush", "ulan@example.com", "Male", "77079567256")

        # Проверки ошибок при заполнении формы с пустым именем
        assert demoqa_page.is_name_error_displayed()
        
    @allure.title("Отправка формы c некорректным заполнением MObile Phone")
    def test_fill_form_with_invalid_phone(self, browser):
        demoqa_page = TestForm(browser)
        demoqa_page.load()
        demoqa_page.fill_form("Ulan", "Zhukush", "ulan@example.com", "Male", "0000000000")

        # Проверки ошибок при заполнении формы с невалидным номером телефона
        assert demoqa_page.is_phone_error_displayed()
        
    @allure.title("Отправка формы c пустым полем Gender")
    def test_fill_form_with_empty_gender(self, browser):
        demoqa_page = TestForm(browser)
        demoqa_page.load()
        demoqa_page.fill_form("Ulan", "Zhukush", "ulan@example.com", "", "0000000000")

        # Проверки ошибок при заполнении формы с пустым полом
        assert demoqa_page.is_gender_error_displayed()
