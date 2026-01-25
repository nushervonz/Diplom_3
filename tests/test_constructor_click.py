from url import main_site
from pages.main_page import MainPage

class TestConstructorClick:
    
    def test_click_on_constructor_section_goes_to_expected_url(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_constructor_section()
        expected_url = main_site
        assert main_page.is_on_main_page(expected_url)

        