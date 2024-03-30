import sys
import os
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from Pages.fb_login import LoginPage
from Pages.fb_header import Navigate

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)

driver = webdriver.Chrome(options=option)

class TestStringMethods(unittest.TestCase):

    def test_logging_into_fb(self):
        loginpage = LoginPage(driver)
        loginpage.login("supak00l@hotmail.com","N94?uecfZkiS8n05")
        navigate = Navigate(driver)
        navigate.navigate_to_events()
        sleep(10)


if __name__ == '__main__':
    unittest.main()