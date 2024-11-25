from .pages.main_page import MainPage
from selenium.common.exceptions import NoSuchElementException
from .pages.base_page import *



def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()