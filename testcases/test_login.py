"""Test cases for the login page of www.saucedemo.com """
import pytest

from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestAndVerifyLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)

    def test_login_valid_credentials(self):
        """ Login with valid credentials """
        self.lp.perform_complete_login("standard_user", "secret_sauce")
        assert self.lp.is_login_successful()
        print("Login with valid credentials successful")

    def test_login_missing_username(self):
        """ Login with missing username """
        self.lp.perform_complete_login("", "secret_sauce")
        self.lp.error_message_exits()
        error_message = self.lp.get_error_message_text()
        print(error_message)
        assert error_message == self.lp.MISSING_USERNAME_ERROR

    def test_login_missing_password(self):
        """ Login with missing password """
        self.lp.perform_complete_login("standard_user", "")
        self.lp.error_message_exits()
        error_message = self.lp.get_error_message_text()
        print(error_message)
        assert error_message == self.lp.MISSING_PASSWORD_ERROR

    @pytest.mark.parametrize('username, password', [("standard_user", "xyz"), ("abc", "secret_sauce"), ("abc", "xyz")])
    def test_login_invalid_credentials(self, username, password):
        """
        Login with invalid credentials:
            Case 01: incorrect password
            Case 02: incorrect username
            Case 03: incorrect username & password
        """
        self.lp.perform_complete_login(username, password)
        self.lp.error_message_exits()
        error_message = self.lp.get_error_message_text()
        print(error_message)
        assert error_message == self.lp.INVALID_USERNAME_PASSWORD_ERROR

    def test_login_user_locked_out(self):
        """ Login with Locked Out User """
        self.lp.perform_complete_login("locked_out_user", "secret_sauce")
        if not self.lp.is_login_successful():
            error_message = self.lp.get_error_message_text()
            print(error_message)
            assert error_message == self.lp.LOCKED_OUT_USER_ERROR

    def test_login_failure(self):
        """ Failing Test Case for Demonstration purposes for Test Report
        """
        self.lp.perform_complete_login("standard_user", "secret_sau")
        assert self.lp.is_login_successful()
