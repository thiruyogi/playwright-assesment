import pdb

from playwright.sync_api import expect


class AccountOverviewPage():

    def __init__(self, page):
        self.page = page

    def balance_in_an_account(self, account_id):
        """

        :param String account_id: Account ID for which balance has to fetched
        :return String balance: Balance amount for the account_id
        """
        balance = self.page.locator(f"//a[contains(text(),'{account_id}')]/parent::td/following-sibling::td[1]")
        return balance

    def verify_balance_in_an_account(self, account_id, expected_balance):
        expect(self.balance_in_an_account(account_id), f"checking the balance of the account {account_id}").to_have_text(expected_balance)