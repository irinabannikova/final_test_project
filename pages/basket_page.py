from .base_page import BasePage
from .locators import *
from selenium.webdriver import *


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        message_empty = self.browser.find_element(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET).text
        assert 'пуста'  in message_empty, "basket is not empty"

