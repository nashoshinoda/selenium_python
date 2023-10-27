from selenium.webdriver.common.by import By

class HomePage:
    shop_btn = (By.XPATH, "//a[text()='Shop']")
    
    def __init__(self, driver):
        self.driver = driver
    
    def get_shop_item(self):
        return self.driver.find_element(*HomePage.shop_btn)
