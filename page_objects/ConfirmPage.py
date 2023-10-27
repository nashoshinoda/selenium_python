from selenium.webdriver.common.by import By

class ConfirmPage:
    success_btn = (By.XPATH, "//button[@class='btn btn-success']")
    country_field = (By.ID, "country")
    
    def __init__(self, driver):
        self.driver = driver
    
    def get_success_btn(self):
        return self.driver.find_element(*ConfirmPage.success_btn)
    
    def get_country_field(self):
        return self.driver.find_elements(*ConfirmPage.country_field)
