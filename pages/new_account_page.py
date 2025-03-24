import time

from playwright.sync_api import expect


class NewAccountPage():

    def __init__(self, page):
        self.page = page

        self.account_type_dropdown = self.page.locator("#type")
        self.create_new_account_button = self.page.get_by_role("button", name="Open New Account")
        self.account_creation_success_message = self.page.get_by_text("Congratulations, your account")
        self.newly_created_account_number = self.page.locator("#newAccountId")


    def create_new_savings_account(self):
        self.account_type_dropdown.select_option('SAVINGS')
        time.sleep(2)
        self.create_new_account_button.click()
        expect(self.account_creation_success_message, 'Verifying whether account creation message is displayed').to_be_visible()

    def get_newly_created_account_number(self):
        return self.newly_created_account_number.text_content()
