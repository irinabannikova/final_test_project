from .base_page import BasePage
from .locators import *
from selenium.webdriver import *


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