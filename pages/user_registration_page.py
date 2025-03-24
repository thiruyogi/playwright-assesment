import pdb

from playwright.sync_api import expect


class UserRegistrationPage():

    def __init__(self, page):
        self.page = page

        self.user_first_name_textbox = self.page.locator("[id=\"customer\\.firstName\"]")
        self.user_last_name_textbox = self.page.locator("[id=\"customer\\.lastName\"]")
        self.user_address_textbox = self.page.locator("[id=\"customer\\.address\\.street\"]")
        self.user_city_textbox = self.page.locator("[id=\"customer\\.address\\.city\"]")
        self.user_state_textbox = self.page.locator("[id=\"customer\\.address\\.state\"]")
        self.user_zip_code_textbox = self.page.locator("[id=\"customer\\.address\\.zipCode\"]")
        self.user_phone_textbox = self.page.locator("[id=\"customer\\.phoneNumber\"]")
        self.user_ssn_textbox = self.page.locator("[id=\"customer\\.ssn\"]")
        self.user_username_textbox = self.page.locator("[id=\"customer\\.username\"]")
        self.user_password_textbox = self.page.locator("[id=\"customer\\.password\"]")
        self.user_confirm_password_textbox = self.page.locator("#repeatedPassword")
        self.register_button = self.page.get_by_role("button", name="Register")
        self.registration_successful_message = self.page.get_by_text(text='Your account was created successfully. You are now logged in.')


    def register_new_user(self, user_data):
        """

        :param dict user_data: All necessary values for creating a user
        :return:
        """
        self.user_first_name_textbox.fill(user_data['firstname'])
        self.user_last_name_textbox.fill(user_data['lastname'])
        self.user_address_textbox.fill(user_data['address'])
        self.user_city_textbox.fill(user_data['city'])
        self.user_state_textbox.fill(user_data['state'])
        self.user_zip_code_textbox.fill(user_data['zipcode'])
        self.user_phone_textbox.fill(user_data['phone'])
        self.user_ssn_textbox.fill(user_data['ssn'])
        self.user_username_textbox.fill(user_data['username'])
        self.user_password_textbox.fill(user_data['password'])
        self.user_confirm_password_textbox.fill(user_data['confirm_password'])
        self.register_button.click()

    def verify_registration_successful(self):
        expect(self.registration_successful_message, 'Checking registration successful message').to_be_visible()

