
"""Search course test."""

from letskodeitpop.base.base_setup import BaseSetup
from letskodeitpop.base.webdriver_custom_class import WebDriverCustomClass
from letskodeitpop.pages.home_page.home import HomePage
from letskodeitpop.pages.course_page.courses import CoursePage
import unittest


class SearchCourses(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(SearchCourses, self).setUp()
        self.webdriver_custom = WebDriverCustomClass(self.driver)
        self.home_page = HomePage(self.driver)
        self.course_page = CoursePage(self.driver)

    def test_search_courses_with_python(self):
        self.home_page.verify_if_page_is_visible()
        self.home_page.button_scroll_to()
        self.home_page.view_all_courses_button_click_on()
        self.course_page.input_field_send_keys('Python')
        self.course_page.search_button_click_on()
        self.course_page.found_courses_print_to_console()

    def tearDown(self):
        super(SearchCourses, self).tearDown()

if __name__ == '__main__':
    unittest.main()
