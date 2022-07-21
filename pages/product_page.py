from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def should_be_same_name_in_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT)
        assert product_name.text == product_name_alert.text, 'Product\'s name in alert isn\'t same'

    def should_be_same_price_in_alert(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT)
        assert product_price.text == product_price_alert.text, 'Product\'s price in alerts isn\'t same'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_dissapeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message isn't dissapeared"