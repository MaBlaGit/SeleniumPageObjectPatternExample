
"""Module to run all tests"""

from letskodeitpop.tests.test_search_courses.search_courses import SearchCourses
from letskodeitpop.tests.test_sign_up.sign_up import SignUp
import unittest


class TestSuiteRunner(object):

    def __init__(self):
        self.test_find_course = unittest.TestLoader().loadTestsFromTestCase(SearchCourses)
        self.test_sign_up = unittest.TestLoader().loadTestsFromTestCase(SignUp)

    def run_all_tests(self):
        return unittest.TestSuite([self.test_sign_up, self.test_find_course])

if __name__ == '__main__':
    test_suite = TestSuiteRunner()
    unittest.TextTestRunner(verbosity=2).run(test_suite.run_all_tests())
