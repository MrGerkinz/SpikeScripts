from Pages.base_page import BasePage
from Resources.locators import EbLoginLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://id.auth.eventbrite.com/u/login/')
    
    def login(self, email_address,password):
        self.enter_text(EbLoginLocators.eb_email_field, email_address)
        self.click(EbLoginLocators.eb_continue_button)
        self.enter_text(EbLoginLocators.eb_pass_field, password)
        self.click(EbLoginLocators.eb_login_button)
        self.wait_for_page_to_load(EbLoginLocators.eb_hompage_banner)