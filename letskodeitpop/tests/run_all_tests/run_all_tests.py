
"""Module to run all tests"""

import unittest

from letskodeitpop.tests.test_search_courses.search_courses import SearchCourses
from letskodeitpop.tests.test_sign_in.test_sign_in_negative.sign_in_negative import LogInNegativeScenario
from letskodeitpop.tests.test_sign_in.test_sign_in_positive.sign_in_positive import LogInPositiveScenario
from letskodeitpop.tests.test_sign_up.test_sign_up_positive.sign_up_positive import SignUpPositive


class TestSuiteRunner(object):

    def __init__(self):
        self.test_find_course = unittest.TestLoader().loadTestsFromTestCase(SearchCourses)
        self.test_sign_up = unittest.TestLoader().loadTestsFromTestCase(SignUpPositive)
        self.test_log_in_positive_scenario = unittest.TestLoader().loadTestsFromTestCase(LogInPositiveScenario)
        self.test_log_in_negative_scenario = unittest.TestLoader().loadTestsFromTestCase(LogInNegativeScenario)

    def run_all_tests(self):
        return unittest.TestSuite([self.test_sign_up,
                                   self.test_log_in_positive_scenario,
                                   self.test_log_in_negative_scenario,
                                   self.test_find_course])

if __name__ == '__main__':
    test_suite = TestSuiteRunner()
    unittest.TextTestRunner(verbosity=2).run(test_suite.run_all_tests())
