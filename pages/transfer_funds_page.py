import pdb

from playwright.sync_api import expect


class TransferFundsPage():

    def __init__(self, page):
        self.page = page

        self.from_account_dropdown = self.page.locator("#fromAccountId")
        self.to_account_dropdown = self.page.locator("#toAccountId")
        self.amount_textbox = self.page.locator("#amount")
        self.transfer_button = self.page.get_by_role("button", name="Transfer")
        self.transfer_complete_message = self.page.get_by_role("heading", name="Transfer Complete!")


    def get_initial_account_id(self):
        return self.from_account_dropdown.input_value()

    def select_from_account(self, account_id):
        """

        :param string account_id: Account ID from which money to be sent
        :return:
        """
        self.from_account_dropdown.select_option(account_id)

    def select_to_account(self, account_id):
        """
        :param string account_id: Account ID to which monaey to be sent
        :return:
        """

        self.to_account_dropdown.select_option(account_id)

    def transfer_funds(self, amount, from_account):
        """

        :param string amount: Amount to be sent
        :param from_account: Account ID from which money has to be sent.
        :return:
        """
        self.amount_textbox.fill(amount)
        self.select_from_account(from_account)
        self.transfer_button.click()
        expect(self.transfer_complete_message, 'Verifying whether transfer complete message is displayed').to_be_visible()

