from Pages.base_page import BasePage
from Resources.locators import FbLoginLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.facebook.com/')
    
    def login(self, email_adress,password):
        self.enter_text(FbLoginLocators.fb_email_field, email_adress)
        self.enter_text(FbLoginLocators.fb_pass_field, password)
        self.click(FbLoginLocators.fb_login_button)