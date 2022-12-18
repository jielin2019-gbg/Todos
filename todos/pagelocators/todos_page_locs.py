from selenium.webdriver.common.by import By


add_item = (By.XPATH,'//a[contains(@class,"button add")]')

input_name = (By.XPATH,'//input[contains(@class, "add-todo")]')

search_item = (By.XPATH,'//a[contains(@class,"button search")]')

item_num = (By.XPATH,'//div[@class="pull-left"]')

login_button = (By.XPATH,'//input[@value="登录"]')

item_01 = (By.XPATH,'//input[contains(@type, "checkbox")]')

clear_completed = (By.XPATH,'//a[contains(text(),"Clear completed")]')