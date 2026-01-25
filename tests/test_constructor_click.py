from url import main_site
from pages.main_page import MainPage
from locators import MainPageLocators
class TestConstructorClick:
    
    def test_click_on_constructor_section_by_text(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_lenta_section()
        main_page.click_on_constructor_section()
        assert main_page.get_burger_inscription_text() == "Соберите бургер"

    
    def test_lenta_section_by_url(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_lenta_section()
        assert main_page.get_current_url() == main_site + "feed"