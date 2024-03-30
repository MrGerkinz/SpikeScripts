from selenium.webdriver.common.by import By

class FbLoginLocators():
    fb_email_field = (By.NAME,'email')
    fb_pass_field = (By.NAME,'pass')
    fb_login_button = (By.NAME,'login')

class EbLoginLocators():
    eb_email_field = (By.NAME,'username')
    eb_pass_field = (By.NAME,'password')
    eb_continue_button = (By.NAME,'action')
    eb_login_button = (By.NAME,'action')
    eb_hompage_banner = (By.CLASS_NAME,"eds-structure__header")

class EbOrganizationLocators():
    organization = (By.XPATH,"//p[.='Angelo Alcantara']")
    welcome_text = (By.CLASS_NAME,"welcome-banner--title")

class NavigationLocators():
    account_drop_down = (By.XPATH,'.//*[@class="x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z"]')
    spike_account = (By.XPATH,'.//*[@class="x9f619 x1n2onr6 x1ja2u2z x1qjc9v5 x78zum5 xdt5ytf x1iyjqo2 xl56j7k xeuugli x1sxyh0 xurb0ha xsag5q8 xz9dl7a xykv574 xbmpl8g x4cne27 xifccgj"]')
    events_drop_down = (By.XPATH,'.//*[@class="x1emribx"]')