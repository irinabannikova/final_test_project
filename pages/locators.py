from selenium.webdriver.common.by import By


class LoginPageLocators():
     LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
     REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
     REGISTR_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
     REGISTR_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
     REGISTR_FORM_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
     REGISTR_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
     REGISTR_MASSEGE = (By.CSS_SELECTOR, "#messages > div")
     BUTTON_LOGOUT = (By.CSS_SELECTOR, "#logout_link")

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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
      SEE_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn")
      TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
