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