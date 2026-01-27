import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from url import main_site
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    service = Service(r"C:\Users\nushe\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(main_site)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def driver_firefox():
    options = FirefoxOptions()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Firefox(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()
 