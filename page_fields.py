from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestForm:

    URL = "https://demoqa.com/automation-practice-form"

    # Локаторы 
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    GENDER_RADIO_BUTTONS = (By.NAME, "gender")
    MOBILE_PHONE = (By.ID, "userNumber")
    SUBJECTS = (By.ID, "subjectsContainer")
    COUNTRY_DROPDOWN = (By.ID, "countries")
    time.sleep(3)
    SUBMIT_BUTTON = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[11]/div/button")


    def __init__(self, driver):
        self.driver = driver


    def load(self):
        self.driver.get(self.URL)
        
    def get_gender_radio_buttons_locator(self, gender):

        gender_locators = {
            'Male': (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[1]/label"),
            'Female': (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[2]/label"),
            'Other': (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[3]/label")
           
        }
    
        # Проверяем, есть ли переданное значение gender в словаре gender_locators
        if gender in gender_locators:
            return gender_locators[gender]
        elif gender == "":
            return
        else:
            raise ValueError(f"Invalid gender: {gender}. Please provide a valid gender.")

    # Метод заполнения формы
    def fill_form(self, first_name, last_name, email, gender, phone):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        gender_locator = self.get_gender_radio_buttons_locator(gender)
        if gender_locator is not None:
            self.driver.find_element(*gender_locator).click()
        else:
            print("Gender is not selected.")

        self.driver.find_element(*self.MOBILE_PHONE).send_keys(phone)

        time.sleep(3)
        submit_button = self.driver.find_element(By.ID, 'submit')

        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

        submit_button.click()
        
        

    def is_form_submission_successful(self):
        return "Thanks for submitting the form" in self.driver.page_source



    
    def is_name_error_displayed(self):
        return "Please enter your firstname" in self.driver.page_source


    def is_email_error_displayed(self):
        return "Please enter a valid email address" in self.driver.page_source
    
    def is_fields_error_displayed(self):
        return "Please enter all fields" in self.driver.page_source
    
    def is_phone_error_displayed(self):
        return "Thanks for submitting the form" in self.driver.page_source
    
    def is_gender_error_displayed(self):
        return "Please select a gender" in self.driver.page_source
    

