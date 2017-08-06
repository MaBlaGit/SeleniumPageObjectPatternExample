
"""Page object of the Log in page."""

from letskodeitpop.base.base_setup import BaseSetup
from letskodeitpop.base.webdriver_custom_class import WebDriverCustomClass


class LogInPage(BaseSetup, WebDriverCustomClass):

    # locators
    _email_address_input = 'user_email'
    _password_input = 'user_password'
    _log_in_button = 'commit'
    _invalid_log_in_message = '//div[contains(text(), " Invalid email or password")]'

    # verification
    def verify_if_log_in_page_is_visible(self):
        self.is_element_visible(self._log_in_button, locator_type='name')

    def verify_if_invalid_log_in_message_is_visible(self):
        self.is_element_visible(self._invalid_log_in_message, locator_type='xpath')

    # actions
    def email_address_send_keys(self, data=''):
        self.send_keys_to(self._email_address_input, data)

    def password_send_keys(self, data=''):
        self.send_keys_to(self._password_input, data)

    def log_in_button_click_on(self):
        self.click_on_element(self._log_in_button, locator_type='name')
