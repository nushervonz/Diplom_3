import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, WebDriverException
import time


class BasePageActions:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=25):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать, пока элемент будет кликабелен")
    def wait_for_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()
    
    @allure.step("Кликнуть на элемент (Firefox)")
    def click_element_firefox(self, locator, timeout=10):
        attempts = 3
        for attempt in range(1, attempts + 1):
            try:
                element = self.wait_for_clickable(locator, timeout)
                element.click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException, WebDriverException):
                if attempt == attempts:
                    try:
                        
                        el = self.wait_for_element(locator, timeout)
                        self.driver.execute_script("arguments[0].click();", el)
                        return
                    except Exception:
                        raise
                time.sleep(0.5)


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
    
    @allure.step("Перетащить элемент из одного места в другое")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
    
    @allure.step("Перетащить элемент из одного места в другое (Firefox)")
    def drag_and_drop_firefox(self, source_locator, target_locator):
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)        
        js = """
        var src = arguments[0], dest = arguments[1];
        var dataTransfer = null;
        try { dataTransfer = new DataTransfer(); } catch(e) {
            dataTransfer = { data: {}, setData: function(k,v){this.data[k]=v}, getData: function(k){return this.data[k]} };
        }
        function createEvent(type) {
            try {
                return new DragEvent(type, { bubbles: true, cancelable: true, dataTransfer: dataTransfer });
            } catch (e) {
                var evt = document.createEvent('CustomEvent');
                evt.initCustomEvent(type, true, true, null);
                evt.dataTransfer = dataTransfer;
                return evt;
            }
        }
        src.dispatchEvent(createEvent('dragstart'));
        dest.dispatchEvent(createEvent('dragenter'));
        dest.dispatchEvent(createEvent('dragover'));
        dest.dispatchEvent(createEvent('drop'));
        src.dispatchEvent(createEvent('dragend'));
        """
        try:
            self.driver.execute_script(js, source, target)
        except Exception:            
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        
    @allure.step("Отправить текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)
    
    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step("Подождать, пока текст элемента изменится")
    def wait_until_text_changes(self, locator, previous_text, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.get_text_of_element(locator) != previous_text
        )
    

     
    

