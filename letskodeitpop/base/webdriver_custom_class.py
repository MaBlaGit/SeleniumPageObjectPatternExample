
"""Custom WebDriver class with wrapped selenium methods for page object purposes."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverCustomClass(object):

    def __init__(self, driver):
        self.driver = driver

    # localization methods

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        elif locator_type == 'partial link':
            return By.PARTIAL_LINK_TEXT
        elif locator_type == 'tag':
            return By.TAG_NAME
        else:
            raise Exception("Not supported locator!")

    def get_element(self, locator, locator_type='id'):
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            return element
        except:
            raise Exception("Element not found!")

    def get_elements(self, locator, locator_type='id'):
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(lambda driver: self.driver.find_elements(by_type, locator))
            return element
        except:
            raise Exception("Elements weren't found!")

    # action methods

    def click_on_element(self, locator, locator_type='id'):
        element = self.get_element(locator, locator_type)
        element.click()

    def send_keys_to(self, locator, data='', locator_type='id'):
        element = self.get_element(locator, locator_type)
        element.send_keys(data)

    def scroll_to_element(self, locator, locator_type='id'):
        element = self.get_element(locator, locator_type)
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', element)

    # verification methods

    def is_element_visible(self, locator, locator_type='id'):

        try:
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            return element
        except:
            raise Exception('Element {0} is not visible'.format(locator_type))

    def is_element_selected(self, locator, locator_type='id'):
        try:
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            if element.is_selected():
                element.click()
        except:
            raise Exception("Element {0} is not visible".format(locator_type))
