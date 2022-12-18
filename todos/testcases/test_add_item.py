import pytest

from pageobjects.todos_page import TodoPage


class TestAddItem:
    # add one item
    @pytest.mark.parametrize('item_name, total',[("task_01","1 items")])
    def test_add_one_item(self, manage_browser,item_name, total):
        driver = manage_browser
        self.driver = TodoPage(driver)
        self.driver.input_item(item_name)
        assert self.driver.get_item_num() == total

    # add two items with different name
    @pytest.mark.parametrize('item_name, total', [(("task_01","task_02"), "2 items")])
    def test_add_two_item(self, manage_browser,item_name, total):
        driver = manage_browser
        self.driver = TodoPage(driver)
        self.driver.input_item(item_name[0])
        self.driver.input_item(item_name[1])
        assert self.driver.get_item_num() == total

    # add two items which have the same name
    @pytest.mark.parametrize('item_name, total', [(("task_01", "task_01"), "2 items")])
    def test_add_same_name(self, manage_browser,item_name, total):
        driver = manage_browser
        self.driver = TodoPage(driver)
        self.driver.input_item(item_name[0])
        self.driver.input_item(item_name[1])
        assert self.driver.get_item_num() == total