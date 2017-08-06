
"""Search course test."""

from letskodeitpop.base.base_setup import BaseSetup
from letskodeitpop.pages.home_page.home import HomePage
from letskodeitpop.pages.courses_page.courses import CoursesPage
from letskodeitpop.pages.course_page.course import CoursePage
import unittest


class SearchCourses(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(SearchCourses, self).setUp()
        self.home_page = HomePage(self.driver)
        self.courses_page = CoursesPage(self.driver)
        self.course_page = CoursePage(self.driver)

    def test_search_courses_with_python(self):
        self.home_page.verify_if_page_is_visible()
        self.home_page.button_scroll_to()
        self.home_page.view_all_courses_button_click_on()
        self.courses_page.input_field_send_keys('Python')
        self.courses_page.search_button_click_on()
        self.courses_page.found_courses_print_to_console()
        self.courses_page.select_course()
        self.course_page.verify_if_page_is_visible()

    def tearDown(self):
        super(SearchCourses, self).tearDown()

if __name__ == '__main__':
    unittest.main()
