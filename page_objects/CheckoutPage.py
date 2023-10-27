from selenium.webdriver.common.by import By

class CheckoutPage:
    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    checkout_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    
    def __init__(self, driver):
        self.driver = driver
    
    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.card_title)
    
    def get_card_footer(self):
        return self.driver.find_elements(*CheckoutPage.card_footer)
    
    def get_checkout_btn(self):
        return self.driver.find_element(*CheckoutPage.checkout_btn)
