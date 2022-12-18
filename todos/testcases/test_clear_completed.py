import time
import pytest
from pageobjects.todos_page import TodoPage


class TestClearCompleted:
    # delete one item by using clear completed
    @pytest.mark.parametrize('item_name, total', [(("task_01", "task_02","task_03"), "2 items")])
    def test_clear_completed_01(self, manage_browser,item_name, total):
        driver = manage_browser
        self.driver = TodoPage(driver)
        self.driver.input_item(item_name[0])
        self.driver.input_item(item_name[1])
        self.driver.input_item(item_name[2])
        self.driver.click_item_01()
        self.driver.click_clear_completed()
        assert self.driver.get_item_num() == total

    # delete two item by using clear completed
    @pytest.mark.parametrize('item_name, total', [(("task_01", "task_02", "task_03"), "1 items")])
    def test_clear_completed_02(self, manage_browser,item_name, total):
        driver = manage_browser
        self.driver = TodoPage(driver)
        self.driver.input_item(item_name[0])
        self.driver.input_item(item_name[1])
        self.driver.input_item(item_name[2])
        for i in range(2):
            self.driver.click_item_01()
            self.driver.click_clear_completed()
        assert self.driver.get_item_num() == total