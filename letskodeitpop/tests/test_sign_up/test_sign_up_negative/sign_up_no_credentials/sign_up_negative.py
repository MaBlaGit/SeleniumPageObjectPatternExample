
"""Sign up test - negative scenario."""

from letskodeitpop.base.base_setup import BaseSetup
from letskodeitpop.pages.home_page.home import HomePage
from letskodeitpop.pages.sign_up_page.sign_up import SignUpPage
import unittest


class SignUpNegative(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(SignUpNegative, self).setUp()
        self.home_page = HomePage(self.driver)
        self.sign_up_page = SignUpPage(self.driver)

    def test_sign_up(self):
        self.home_page.verify_if_page_is_visible()
        self.home_page.enroll_now_button_click_on()
        self.sign_up_page.verify_if_page_is_visible()
        self.sign_up_page.verify_if_element_is_selected()
        self.sign_up_page.full_name_send_keys(data='')
        self.sign_up_page.address_email_send_keys(data='')
        self.sign_up_page.password_send_keys(data='')
        self.sign_up_page.confirm_password_send_keys(data='')
        self.sign_up_page.sign_up_click_on()
        self.sign_up_page.verify_if_error_title_is_visible()
        self.sign_up_page.error_messages_print_to_console()

    def tearDown(self):
        super(SignUpNegative, self).tearDown()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
