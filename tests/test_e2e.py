from page_objects.HomePage import HomePage
from page_objects.CheckoutPage import CheckoutPage
from page_objects.ConfirmPage import ConfirmPage
from pytest import mark
from selenium.webdriver.common.by import By
from utils.Base import BaseClass
import time


@mark.e2e
class E2ETests(BaseClass):
    def test_e2e(self):
        home_page = HomePage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        confirm_page = ConfirmPage(self.driver)

        home_page.get_shop_item().click()
        time.sleep(3)
        cards = checkout_page.get_card_titles()
        i = -1

        time.sleep(3)

        for card in cards:
            i = i + 1
            card_text = card.text
            
            print(card_text)
            
            if card_text == "Blackberry":
                time.sleep(3)
                checkout_page.get_card_footer()[i].click()
        time.sleep(3)
        checkout_page.get_checkout_btn().click()
        time.sleep(3)
        confirm_page.get_success_btn().click()
        time.sleep(3)
        self.driver.find_element(By.ID, "country").send_keys("ind")
        time.sleep(3)
        self.verify_link_is_presence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(3)
        text_match = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        
        assert "Success! Thank you!" in text_match
        
        time.sleep(5)
