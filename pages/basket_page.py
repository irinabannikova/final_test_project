from .base_page import BasePage
from .locators import *
from selenium.webdriver import *
from .basket_page import *


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        message_empty = self.browser.find_element(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET).text
        assert 'пуста'  in message_empty, "basket is not empty"
        assert BasePage.is_not_element_present(self, By.CSS_SELECTOR, ".basket-items")
    
    def is_not_message_present(self):
        assert BasePage.is_not_element_present(self, By.CSS_SELECTOR, "div.alertinner "), "there is a message"

    def message_is_disappeared(self):
        assert BasePage.is_disappeared(By.CSS_SELECTOR, "div.alertinner ")

    
    

