import allure
from pages.base_page_actions import BasePageActions
from locators import MainPageLocators

class MainPage(BasePageActions):

    @allure.step("Кликнуть на секцию Конструктор")
    def click_on_constructor_section(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_SECTION)
    
    @allure.step("Проверить, что на главной странице")
    def is_on_main_page(self, url):
        return self.get_current_url() == url
    
    def click_on_lenta_section(self):
        self.click_element(MainPageLocators.LENTA_SECTION)
    
    
    def get_burger_inscription_text(self):
        return self.get_text_of_element(MainPageLocators.BURGER_INSCRIPTION)
    
    def get_lenta_inscription_text(self):
        return self.get_text_of_element(MainPageLocators.LENTA_INSCRIPTION)
    
    def click_on_ingredient_icon(self):
        self.click_element(MainPageLocators.INGREDIENT_ICON)

    def ingredient_popup_is_displayed(self):
        return self.element_is_displayed(MainPageLocators.INGREDIENTS_POPUP)
    
    def close_ingredient_popup(self):
        self.click_element(MainPageLocators.CLOSE_POPUP_BUTTON)
    
    def drag_and_drop_ingredient(self):
        self.drag_and_drop(MainPageLocators.DRAG_FROM_SAUSE, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    def get_ingredient_counter_text(self):
        return self.get_text_of_element(MainPageLocators.COUNTER)
    
    def click_on_user_account_button(self):
        self.click_element(MainPageLocators.USER_ACC_BUTTON)
    
    def fill_email_field(self, email):
        self.send_keys_to_input(MainPageLocators.EMAIL_FIELD, email)
    
    def fill_password_field(self, password):
        self.send_keys_to_input(MainPageLocators.PASSWORD_FIELD, password)
    
    def click_on_enter_button(self):
        self.click_element(MainPageLocators.ENTER_BUTTON)
    
    def oreder_button_click(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)
    
    def drag_bun_to_constructor(self):
        self.drag_and_drop(MainPageLocators.BUN_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    def drag_sauce_to_constructor(self):
        self.drag_and_drop(MainPageLocators.SAUCE_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    def drag_filling_to_constructor(self):
        self.scroll_to_element(MainPageLocators.FILLING_ICON)
        self.drag_and_drop(MainPageLocators.FILLING_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    def click_on_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)
    
    def get_lenta_all_time_order_counter_text(self):
        return self.get_text_of_element(MainPageLocators.ALL_TIME_ORDER_COUNTER_ON_LENTA_PAGE)
    
    def wait_for_order_confirmation_popup(self):
        self.wait_for_clickable(MainPageLocators.CLOSE_ORDER_POPUP_BUTTON, timeout=30)

    def click_on_close_order_popup_button(self):
        self.click_element_when_clickable(MainPageLocators.CLOSE_ORDER_POPUP_BUTTON, timeout=20)
    
    def all_time_order_counter_is_displayed(self):
        return self.element_is_displayed(MainPageLocators.ALL_TIME_ORDER_COUNTER)
    
    