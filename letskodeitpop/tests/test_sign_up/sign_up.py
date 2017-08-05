
"""Sign Up test."""

from letskodeitpop.base.base_setup import BaseSetup
from letskodeitpop.base.webdriver_custom_class import WebDriverCustomClass
from letskodeitpop.pages.home_page.home import HomePage
from letskodeitpop.pages.sign_up_page.sign_up import SignUpPage
import unittest


class SignUp(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(SignUp, self).setUp()
        self.webdriver_custom_class = WebDriverCustomClass(self.driver)
        self.home_page = HomePage(self.driver)
        self.sign_up_page = SignUpPage(self.driver)

    def test_sign_up(self):
        self.home_page.enroll_now_button_click_on()
        self.sign_up_page.verify_if_page_is_visible()
        self.sign_up_page.full_name_send_keys(data='Test TesTT')
        self.sign_up_page.address_email_send_keys(data='test@testtt.us')
        self.sign_up_page.password_send_keys(data='aaaaaaa')
        self.sign_up_page.confirm_password_send_keys(data='aaaaaaa')
        self.sign_up_page.verify_if_element_is_selected()
        self.sign_up_page.terms_of_use_checkbox_click_on()
        self.sign_up_page.sign_up_click_on()
        self.home_page.verify_if_user_is_logged()

    def tearDown(self):
        super(SignUp, self).tearDown()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
