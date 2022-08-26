""" Inventory Page Module """
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class InventoryPage(BaseDriver):
    """ Inventory Page Class """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ Inventory Page Locators """
    PAGE_TITLE_ELEMENT = ".title"

    """ Locator Functions """

    def get_page_title_text(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.PAGE_TITLE_ELEMENT).text
