from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pagelocators.todos_page_locs import input_name, item_num, item_01, clear_completed

class TodoPage:

    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def input_item(self,item_name):
        self.driver.find_element(*input_name).send_keys(item_name,Keys.ENTER)

    def get_item_num(self):
        return self.driver.find_element(*item_num).text

    def click_item_01(self):
        self.driver.find_element(*item_01).click()

    def click_clear_completed(self):
        self.driver.find_element(*clear_completed).click()