from pages.product_page import ProductPage
import time
import pytest
from selenium.webdriver.common.by import By


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open() #открываем страницу
    page.should_not_be_success_message()  #ожидаем, что там нет сообщения об успешном добавлении в корзину
    page.add_to_basket() #добавляем в корзину
    page.solve_quiz_and_get_code() #Посчитать результат математического выражения и ввести ответ
    page.should_be_message_about_adding() #Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили
    page.should_be_message_basket_total() #Цена товара в сообщении должно совпадать с тем товаром, который вы действительно добавили

  