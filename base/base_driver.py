""" Base Driver Module """
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    """ Base class for all other Page classes """

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_clickable(self, locator_type, locator):
        """
        Waits for element to be clickable identified by 'selector'
        :param locator_type: Type of locator i.e; By.ID, By.Name, By.XPath etc.
        :param locator: The locator of the element
        :return: element
        """
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_for_presence_of_all_elements_located(self, locator_type, locator):
        """
        Waits for list of elements to be clickable identified by 'selector'
        :param locator_type: Type of locator i.e; By.ID, By.Name, By.XPath etc.
        :param locator: The locator of the elements list
        :return: list of element
        """
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements
