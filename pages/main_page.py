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