from .base_page import BasePage
from .locators import *
from selenium.webdriver import *
from .main_page import *
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no Login form"
        

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM), "There is no Regist form"
    
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTR_FORM_EMAIL)
        email = str(time.time()) + email
        input_email.send_keys(email)
        time.sleep(4)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTR_FORM_PASSWORD)
        input_password.send_keys(password)
        time.sleep(4)
        input_password_repeat =  self.browser.find_element(*LoginPageLocators.REGISTR_FORM_PASSWORD_REPEAT)
        input_password_repeat.send_keys(password)
        time.sleep(4)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTR_BUTTON)
        reg_button.click()
        time.sleep(10)
        assert self.browser.find_element(*LoginPageLocators.BUTTON_LOGOUT)
        
        



        

        