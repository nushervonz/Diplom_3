import allure
from url import main_site
from pages.main_page import MainPage
from locators import MainPageLocators
from data import UserData
class TestConstructorClick:
    
    @allure.title("Тест переход по клику на «Конструктор»")
    def test_click_on_constructor_section_by_text(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_lenta_section()
        main_page.click_on_constructor_section()
        assert main_page.get_burger_inscription_text() == "Соберите бургер"

    @allure.title("Тест переход по клику на раздел «Лента заказов»")
    def test_lenta_section_by_url(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_lenta_section()
        assert main_page.get_current_url() == main_site + "feed"
    
    @allure.title("Тест открытия всплывающего окна по клику на ингредиент")    
    def test_ingredient_click_opens_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient_icon()
        assert main_page.ingredient_popup_is_displayed() == True
    
    @allure.title("Тест закрытия всплывающего окна ингредиента")
    def test_close_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient_icon()
        main_page.close_ingredient_popup()
        assert main_page.get_burger_inscription_text() == "Соберите бургер"
    
    @allure.title("Тест перетаскивания ингредиента в конструктор")
    def test_drag_and_drop_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        assert main_page.get_ingredient_counter_text() == "1"
    
    @allure.title("Тест увеличения счётчика заказов при создании нового заказа")
    def test_new_order_increases_order_counter(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_lenta_section()
        initial_counter = int(main_page.get_lenta_all_time_order_counter_text())
        main_page.click_on_constructor_section()
        main_page.click_on_user_account_button()
        main_page.fill_email_field(UserData.existing_user_email)
        main_page.fill_password_field(UserData.existing_user_password)
        main_page.click_on_enter_button()
        main_page.drag_bun_to_constructor()
        main_page.drag_sauce_to_constructor()
        main_page.drag_filling_to_constructor()
        main_page.click_on_order_button()
        main_page.wait_for_close_order_popup_button()
        assert main_page.all_time_order_counter_is_displayed() == True
    