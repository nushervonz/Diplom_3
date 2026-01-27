import allure
from pages.base_page_actions import BasePageActions
from locators import MainPageLocators

class MainPage(BasePageActions):

    @allure.step("Кликнуть на секцию Конструктор")
    def click_on_constructor_section(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_SECTION)
    
    @allure.step("Кликнуть на секцию Лента заказов")
    def click_on_lenta_section(self):
        self.click_element(MainPageLocators.LENTA_SECTION)
    
    @allure.step("Получить текст надписи 'Соберите бургер'")
    def get_burger_inscription_text(self):
        return self.get_text_of_element(MainPageLocators.BURGER_INSCRIPTION)
    
    
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
    
    @allure.step("Перетащить ингредиент в конструктор (Firefox)")
    def drag_and_drop_ingredient_firefox(self):
        self.drag_and_drop_firefox(MainPageLocators.DRAG_FROM_SAUSE, MainPageLocators.DROP_TO_CONSTRUCOR)
    
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
    
    @allure.step("Перетащить булку в конструктор")
    def drag_bun_to_constructor(self):
        self.drag_and_drop(MainPageLocators.BUN_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    @allure.step("Перетащить булку в конструктор (Firefox)")
    def drag_bun_to_constructor_firefox(self):
        self.drag_and_drop_firefox(MainPageLocators.BUN_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    @allure.step("Перетащить соус в конструктор")
    def drag_sauce_to_constructor(self):
        self.drag_and_drop(MainPageLocators.SAUCE_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    @allure.step("Перетащить соус в конструктор (Firefox)")
    def drag_sauce_to_constructor_firefox(self):
        self.drag_and_drop_firefox(MainPageLocators.SAUCE_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    @allure.step("Перетащить начинку в конструктор")
    def drag_filling_to_constructor(self):
        self.scroll_to_element(MainPageLocators.FILLING_ICON)
        self.drag_and_drop(MainPageLocators.FILLING_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)
    
    @allure.step("Перетащить начинку в конструктор (Firefox)")
    def drag_filling_to_constructor_firefox(self):
        self.scroll_to_element(MainPageLocators.FILLING_ICON)
        self.drag_and_drop_firefox(MainPageLocators.FILLING_ICON, MainPageLocators.DROP_TO_CONSTRUCOR)

    @allure.step("Кликнуть на кнопку Оформить заказ")
    def click_on_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)
    
    @allure.step("Получить текст общего счётчика заказов на странице Лента заказов")
    def get_lenta_all_time_order_counter_text(self):
        return self.get_text_of_element(MainPageLocators.ALL_TIME_ORDER_COUNTER_ON_LENTA_PAGE)
    
    @allure.step("Кликнуть на кнопку закрытия окна заказа")
    def click_close_order_popup_button(self):
        self.click_element(MainPageLocators.ORDER_POPUP_CLOSE_BUTTON)
    
    @allure.step("Подождать секцию Лента заказов")
    def wait_for_lenta_section(self):
        self.wait_for_element(MainPageLocators.LENTA_SECTION, timeout=20)
    
    @allure.step("Подождать счётчик «Выполнено за всё время» на странице Лента заказов")
    def wait_for_lenta_all_time_order_counter_text(self):
        self.wait_for_element(MainPageLocators.ALL_TIME_ORDER_COUNTER_ON_LENTA_PAGE, timeout=20)
    
    @allure.step("Получить текст счётчика «Выполнено за всё время» во всплывающем окне")
    def get_popup_counter_text(self):
        return self.get_text_of_element(MainPageLocators.POPUP_COUNTER)
    
    @allure.step("Подождать изменения текста во всплывающем окне, пока он не станет отличен от 9999")
    def wait_until_popup_counter_text_is_not_9999(self, previous_text):
        self.wait_until_text_changes(MainPageLocators.POPUP_COUNTER, previous_text, timeout=30)
    
    @allure.step("Подождать изменения текста табло 'В работе'")
    def wait_until_tab_text_changes(self, previous_text):
        self.wait_until_text_changes(MainPageLocators.IN_PROGRESS_TAB, previous_text, timeout=20)
    
    @allure.step("Получить текст счётчика 'Выполнено за сегодня'")
    def get_today_order_counter_text(self):
        return self.get_text_of_element(MainPageLocators.TODAY_ORDER_COUNTER)
    
    @allure.step("Получить текст табло 'В работе'")
    def get_in_progress_tab_text(self):
        return self.get_text_of_element(MainPageLocators.IN_PROGRESS_TAB)
    