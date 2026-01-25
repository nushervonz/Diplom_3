from selenium.webdriver.common.by import By

class MainPageLocators:

    CONSTRUCTOR_SECTION = (By.XPATH, "//nav/ul/li[1]/a/p")
    LENTA_SECTION = (By.XPATH, "//nav/ul/li[2]/a/p")
    BURGER_INSCRIPTION = (By.XPATH, "//div/main/section[1]/h1")
    LENTA_INSCRIPTION = (By.XPATH, "//div/main/section[2]/h1")  