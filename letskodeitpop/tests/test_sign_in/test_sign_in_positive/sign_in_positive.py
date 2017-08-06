
"""Log in test - positive scenario."""

from letskodeitpop.base.base_setup import BaseSetup
from letskodeitpop.pages.home_page.home import HomePage
from letskodeitpop.pages.log_in_page.log_in import LogInPage
from letskodeitpop.base.credentials_setup import credentials
import unittest


class LogInPositiveScenario(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(LogInPositiveScenario, self).setUp()
        self.home_page = HomePage(self.driver)
        self.log_in_page = LogInPage(self.driver)

    def test_log_in_into_account(self):
        self.home_page.log_in_button_click_to()
        self.log_in_page.verify_if_log_in_page_is_visible()
        self.log_in_page.email_address_send_keys(data=credentials.get('email'))
        self.log_in_page.password_send_keys(data=credentials.get('password'))
        self.log_in_page.log_in_button_click_on()
        self.home_page.verify_if_user_is_logged()

    def tearDown(self):
        super(LogInPositiveScenario, self).tearDown()

if __name__ == '__main__':
    unittest.main()
