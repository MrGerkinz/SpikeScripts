from time import sleep
from Pages.base_page import BasePage
from Resources.locators import NavigationLocators

class Navigate(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.facebook.com/')
    
    def navigate_to_events(self):
        self.click(NavigationLocators.account_drop_down)
        sleep(1)
        self.click(NavigationLocators.spike_account)