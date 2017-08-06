
"""Page Object of the sign up page."""

from letskodeitpop.base.base_setup import BaseSetup
from letskodeitpop.base.webdriver_custom_class import WebDriverCustomClass


class SignUpPage(BaseSetup, WebDriverCustomClass):

    # locators
    _locate_sign_up_title = '//h1[contains(text(), "Sign Up to Let\'s Kode It")]'
    _full_name = 'user_name'
    _email_address = 'user_email'
    _password = 'user_password'
    _confirm_password = 'user_password_confirmation'
    _terms_of_use_checkbox = 'user_agreed_to_terms'
    _sign_up_button = 'commit'
    _no_credentials_main_massage = '//p[contains(text(), "Oops! Please fix the following:")]'
    _no_credentials_list = '//div[@class="alert alert-danger alert-registration-page"]//ul//li'

    # verifications
    def verify_if_page_is_visible(self):
        self.is_element_visible(self._locate_sign_up_title, locator_type='xpath')

    def verify_if_element_is_selected(self):
        self.is_element_selected(self._terms_of_use_checkbox)

    def verify_if_error_title_is_visible(self):
        self.is_element_visible(self._no_credentials_main_massage, locator_type='xpath')

    # actions
    def full_name_send_keys(self, data=''):
        self.send_keys_to(self._full_name, data)

    def address_email_send_keys(self, data=''):
        self.send_keys_to(self._email_address, data)

    def password_send_keys(self, data=''):
        self.send_keys_to(self._password, data)

    def confirm_password_send_keys(self, data=''):
        self.send_keys_to(self._confirm_password, data)

    def terms_of_use_checkbox_click_on(self):
        self.click_on_element(self._terms_of_use_checkbox)

    def sign_up_click_on(self):
        self.click_on_element(self._sign_up_button, locator_type='name')

    def error_messages_print_to_console(self):
        list_errors = self.get_elements(self._no_credentials_list, locator_type='xpath')
        for error in list_errors:
            print(error.text)
