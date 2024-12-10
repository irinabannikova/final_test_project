from selenium.webdriver.common.by import By


class LoginPageLocators():
     LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
     REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")

class CatalogPageLocators():
     BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form')
     MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
     PODUCT_NAME = (By.CSS_SELECTOR,  'div.col-sm-6.product_main > h1')
     TEXT_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
     MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
     PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

