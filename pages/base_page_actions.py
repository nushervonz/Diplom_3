import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
class BasePageActions:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=25):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать, пока элемент будет кликабелен")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        element.click()

    def click_element_when_clickable(self, locator, timeout=10):
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    @allure.step("Проверить, что элемент отображается")
    def element_is_displayed(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.is_displayed()

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получить текст элемента")
    def get_text_of_element(self, locator, timeout=20):
        element = self.wait_for_element(locator, timeout)
        return element.text
    
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
    
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)
    
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
     
    

