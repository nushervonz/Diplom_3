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
    
    @allure.step("Кликнуть на секцию Лента заказов")
    def click_on_lenta_section(self):
        self.click_element(MainPageLocators.LENTA_SECTION)
    
    @allure.step("Получить текст надписи 'Соберите бургер'")
    def get_burger_inscription_text(self):
        return self.get_text_of_element(MainPageLocators.BURGER_INSCRIPTION)
    
    @allure.step("Получить текст надписи 'Лента заказов'")
    def get_lenta_inscription_text(self):
        return self.get_text_of_element(MainPageLocators.LENTA_INSCRIPTION)
    
    @allure.step("Кликнуть на иконку ингредиента")
    def click_on_ingredient_icon(self):
        self.click_element(MainPageLocators.INGREDIENT_ICON)
    
    @allure.step("Проверить, что всплывающее окно ингредиента отображается")
    def ingredient_popup_is_displayed(self):
        return self.element_is_displayed(MainPageLocators.INGREDIENTS_POPUP)
    
    @allure.step("Закрыть всплывающее окно ингредиента")
    def close_ingredient_popup(self):
        self.click_element(MainPageLocators.CLOSE_POPUP_BUTTON)
    
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_and_drop_ingredient(self):
        self.drag_and_drop(MainPageLocators.DRAG_FROM_SAUSE, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    @allure.step("Получить текст счётчика ингредиента")
    def get_ingredient_counter_text(self):
        return self.get_text_of_element(MainPageLocators.COUNTER)
    
    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_on_user_account_button(self):
        self.click_element(MainPageLocators.USER_ACC_BUTTON)
    
    @allure.step("Заполнить поле Email")
    def fill_email_field(self, email):
        self.send_keys_to_input(MainPageLocators.EMAIL_FIELD, email)
    
    @allure.step("Заполнить поле Пароль")
    def fill_password_field(self, password):
        self.send_keys_to_input(MainPageLocators.PASSWORD_FIELD, password)
    
    @allure.step("Кликнуть на кнопку Войти")
    def click_on_enter_button(self):
        self.click_element(MainPageLocators.ENTER_BUTTON)
    
    @allure.step("Кликнуть на кнопку Оформить заказ")
    def oreder_button_click(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)
    
    @allure.step("Перетащить булку в конструктор")
    def drag_bun_to_constructor(self):
        self.drag_and_drop(MainPageLocators.BUN_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    @allure.step("Перетащить соус в конструктор")
    def drag_sauce_to_constructor(self):
        self.drag_and_drop(MainPageLocators.SAUCE_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    @allure.step("Перетащить начинку в конструктор")
    def drag_filling_to_constructor(self):
        self.scroll_to_element(MainPageLocators.FILLING_ICON)
        self.drag_and_drop(MainPageLocators.FILLING_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    @allure.step("Кликнуть на кнопку Оформить заказ")
    def click_on_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)
    
    @allure.step("Получить текст общего счётчика заказов на странице Лента заказов")
    def get_lenta_all_time_order_counter_text(self):
        return self.get_text_of_element(MainPageLocators.ALL_TIME_ORDER_COUNTER_ON_LENTA_PAGE)
    
    @allure.step("Получить текст общего счётчика заказов")
    def get_all_time_order_counter_text(self):
        return self.get_text_of_element(MainPageLocators.ALL_TIME_ORDER_COUNTER)
    
    @allure.step("Подождать появления всплывающего окна подтверждения заказа")
    def wait_for_order_confirmation_popup(self):
        self.wait_for_element(MainPageLocators.ALL_TIME_ORDER_COUNTER, timeout=30)

    @allure.step("Подождать появления кнопки закрытия окна заказа")
    def wait_for_close_order_popup_button(self):
        self.wait_for_clickable(MainPageLocators.ORDER_POPUP_CLOSE_BUTTON, timeout=30)
    
    @allure.step("Проверить, что кнопка закрытия окна заказа отображается")
    def close_order_popup_button_is_displayed(self):
        return self.element_is_displayed(MainPageLocators.ORDER_POPUP_CLOSE_BUTTON)
    
    @allure.step("Кликнуть на кнопку закрытия окна заказа")
    def click_close_order_popup_button(self):
        self.click_element(MainPageLocators.ORDER_POPUP_CLOSE_BUTTON)
    
    @allure.step("Проверить, что общий счётчик заказов отображается")
    def all_time_order_counter_is_displayed(self):
        return self.element_is_displayed(MainPageLocators.ORDER_POPUP_CLOSE_BUTTON)
    
    @allure.step("Подождать появления контентной области")
    def wait_for_content_box(self):
        self.wait_for_element(MainPageLocators.CONTENT_BOX)
    
    