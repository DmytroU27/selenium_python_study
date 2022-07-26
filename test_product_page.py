from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


# def test_guest_can_add_product_to_basket(browser):
#     link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
#     page = ProductPage(browser, link2)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_same_name_in_alert()
#     page.should_be_same_price_in_alert()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.should_be_dissapeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_no_items_in_basket()
    page.should_be_empty_message()

