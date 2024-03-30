from Pages.base_page import BasePage
from Resources.locators import EbOrganizationLocators

class OrganizationsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.eventbrite.com/organizations/')
    
    def selectOrg(self):
        self.click(EbOrganizationLocators.organization)
        self.wait_for_page_to_load(EbOrganizationLocators.welcome_text)