""" Login Page Module """
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from pages.inventory_page import InventoryPage


class LoginPage(BaseDriver):
    """ Login Page Class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ Login Page Locators """
    USERNAME_FIELD = "user-name"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = 'login-button'
    ERROR_MESSAGE_ELEMENT = '.error-message-container.error h3'

    """ Constants """
    MISSING_USERNAME_ERROR = "Epic sadface: Username is required"
    MISSING_PASSWORD_ERROR = "Epic sadface: Password is required"
    INVALID_USERNAME_PASSWORD_ERROR = "Epic sadface: Username and password do not match any user in this service"
    LOCKED_OUT_USER_ERROR = "Epic sadface: Sorry, this user has been locked out."

    """ Locator Functions """

    def get_username_field(self):
        return self.wait_for_element_to_be_clickable(By.ID, self.USERNAME_FIELD)

    def get_password_field(self):
        return self.wait_for_element_to_be_clickable(By.ID, self.PASSWORD_FIELD)

    def get_login_button(self):
        return self.wait_for_element_to_be_clickable(By.ID, self.LOGIN_BUTTON)

    def error_message_exits(self):
        """ Returns True if error message exists """
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.ERROR_MESSAGE_ELEMENT).is_displayed()

    def get_error_message_text(self):
        """ Returns the text of the error message """
        if self.error_message_exits():
            return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.ERROR_MESSAGE_ELEMENT).text

    def enter_username(self, username):
        """ Enters Username in username field """
        self.get_username_field().send_keys(username)

    def enter_password(self, password):
        """ Enters Password in password field """
        self.get_password_field().send_keys(password)

    def click_login_button(self):
        """ Clicks Login Button """
        self.get_login_button().click()

    def perform_complete_login(self, username, password):
        """ Complete Login action """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_login_successful(self):
        """ Returns True if Login is successful """
        try:
            inventory_page = InventoryPage(self.driver)
            return inventory_page.get_page_title_text() == "PRODUCTS"
        except:
            return False
