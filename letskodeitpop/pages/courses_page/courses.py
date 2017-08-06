
"""Page Object of the courses page."""

from letskodeitpop.base.base_setup import BaseSetup
from letskodeitpop.base.webdriver_custom_class import WebDriverCustomClass


class CoursesPage(BaseSetup, WebDriverCustomClass):

    # locators
    _search_course_input_field = 'search-courses'
    _search_button = 'search-course-button'
    _course_courses_container = '//div[@class="row course-list list"]'
    _found_courses_listing = '//div[@class="course-listing-title"]'
    _select_python_course = '//div[contains(text(), "Learn Python 3 from scratch")]'

    # verification
    def verify_if_page_is_visible(self):
        self.is_element_visible(self._course_courses_container, locator_type='xpath')

    # actions
    def input_field_send_keys(self, data=''):
        self.send_keys_to(self._search_course_input_field, data)

    def search_button_click_on(self):
        self.click_on_element(self._search_button)

    def found_courses_print_to_console(self):
        courses = self.get_elements(self._found_courses_listing, locator_type='xpath')
        for course in courses:
            print(course.text)

    def select_course(self):
        self.click_on_element(self._select_python_course, locator_type='xpath')
