
"""Base setup - defined fixtures which are launched for every tests."""

from selenium import webdriver
from letskodeitpop.base.browser_setup import browser_setup


class BaseSetup(object):

    def setUp(self):
        if browser_setup['browser'] == "firefox":
            self.driver = webdriver.Firefox()
        elif browser_setup['browser'] == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            raise Exception("Not supported browser!")
        self.driver.maximize_window()
        self.driver.get(browser_setup['url'])

    def tearDown(self):
        self.driver.quit()
