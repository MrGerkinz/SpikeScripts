from Pages.base_page import BasePage
from Resources.locators import NavigationLocators

class Navigate(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.facebook.com/events?source=46&action_history=null')
    
    def navigate_to_events(self):
        self.click(NavigationLocators.events_drop_down)