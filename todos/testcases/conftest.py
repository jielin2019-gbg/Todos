import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def manage_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://todo.scriveqa.com/")
    yield driver
    driver.quit()

