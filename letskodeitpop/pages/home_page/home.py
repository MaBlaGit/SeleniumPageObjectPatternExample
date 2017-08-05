
"""Page Object of the home page."""

from letskodeitpop.base.base_setup import BaseSetup
from letskodeitpop.base.webdriver_custom_class import WebDriverCustomClass


class HomePage(BaseSetup, WebDriverCustomClass):

    # locators
    _view_more_courses_button = '//a[@class="btn btn-md btn-primary"]'
    _web_page_title = '//h2[contains(text(), "Welcome to Let\'s Kode It")]'
    _enrol_button = '//a[@class="btn-primary btn-hg text-center"]'
    _verify_logged_user = '//img[@class="gravatar"]'

    # verifications
    def verify_if_page_is_visible(self):
        self.is_element_visible(self._web_page_title, locator_type='xpath')

    def verify_if_user_is_logged(self):
        self.is_element_visible(self._verify_logged_user, locator_type='xpath')

    # actions
    def button_scroll_to(self):
        self.scroll_to_element(self._view_more_courses_button, locator_type='xpath')

    def enroll_now_button_click_on(self):
        self.click_on_element(self._enrol_button, locator_type='xpath')

    def view_all_courses_button_click_on(self):
        self.click_on_element(self._view_more_courses_button, locator_type='xpath')
