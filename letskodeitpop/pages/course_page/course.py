
"""Page object of course page"""

from letskodeitpop.base.base_setup import BaseSetup
from letskodeitpop.base.webdriver_custom_class import WebDriverCustomClass


class CoursePage(BaseSetup, WebDriverCustomClass):

    # locators
    _enroll_button = 'enroll-button-top' # id

    # verification
    def verify_if_page_is_visible(self):
        self.is_element_visible(self._enroll_button)

    # actions
