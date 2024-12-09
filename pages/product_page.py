from .base_page import BasePage
from .locators import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*CatalogPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
    
    def should_be_message_about_adding(self):
        product_name = self.browser.find_element(*CatalogPageLocators.PODUCT_NAME).text
        message = self.browser.find_element(*CatalogPageLocators.TEXT_ADD_TO_BASKET).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert message == product_name, "No product name in the message"
    def should_be_message_basket_total(self):
        message_basket_total = self.browser.find_element(*CatalogPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*CatalogPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert message_basket_total == product_price, "No product price in the message"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CatalogPageLocators.MESSAGE_ABOUT_ADDING), \
       "Success message is presented, but should not be"
    
    
        

  