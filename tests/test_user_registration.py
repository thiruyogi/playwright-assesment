import pdb

from playwright.sync_api import expect

from api.transcation_api import TransactionsApi
from base.test_base import BaseClass
from pages.account_overview_page import AccountOverviewPage
from pages.bill_pay_page import BillPayPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
import pytest

from pages.new_account_page import NewAccountPage
from pages.transfer_funds_page import TransferFundsPage
from pages.user_registration_page import UserRegistrationPage
from utils.data_utils import DataUtils


class TestUserRegistration(BaseClass):

    new_account_number = None

    @pytest.fixture(scope='class', autouse=True)
    def class_setup(self, setup):
        self.__class__.login_page = LoginPage(self.page)
        self.__class__.registration_page = UserRegistrationPage(self.page)
        self.login_page.click_on_register_link()
        user_data = DataUtils.generate_user_data()
        self.registration_page.register_new_user(user_data)
        self.registration_page.verify_registration_successful()
        # To get the session ID from UI and to add it to the api request context
        self.session_id = self.login_page.get_session_id()
        # self.request_context.set_extra_http_headers({"Cookie": f"JSESSIONID={session_id}"})
        self.__class__.home_page = HomePage(self.page)
        self.__class__.new_account_page = NewAccountPage(self.page)
        self.__class__.accounts_overview_page = AccountOverviewPage(self.page)
        self.__class__.transfer_funds_page = TransferFundsPage(self.page)
        self.__class__.bill_pay_page = BillPayPage(self.page)
        self.__class__.transactions_api = TransactionsApi(self.request_context, self.base_url, self.session_id)

    def test_global_navigation_links(self):
        self.home_page.verify_about_us_link()
        self.home_page.verify_services_link()
        self.home_page.verify_admin_page_link()
        self.home_page.verify_products_link()
        self.home_page.verify_locations_link()

    @pytest.mark.debug
    def test_create_savings_account(self):
        self.home_page.click_on_open_new_account_link()
        self.new_account_page.create_new_savings_account()
        TestUserRegistration.new_account_number = self.new_account_page.get_newly_created_account_number()
        self.home_page.click_on_accounts_overview_link()
        self.accounts_overview_page.verify_balance_in_an_account(TestUserRegistration.new_account_number, "$100.00")


    def test_transfer_funds(self):
        self.home_page.click_on_transfer_funds_link()
        self.transfer_funds_page.transfer_funds('5',TestUserRegistration.new_account_number)
        self.home_page.click_on_accounts_overview_link()
        self.accounts_overview_page.verify_balance_in_an_account(TestUserRegistration.new_account_number, "$95.00")

    @pytest.mark.debug
    def test_bill_payment_functionality(self):
        self.home_page.click_on_accounts_overview_link()
        before_balance_str = self.accounts_overview_page.balance_in_an_account(TestUserRegistration.new_account_number).text_content()
        before_balance = float(before_balance_str.replace('$', ''))
        payment_amount = 10
        expected_balance = before_balance - payment_amount
        expected_balance_str = f"${expected_balance:.2f}"
        self.home_page.click_on_bill_pay_link()
        payee_data = DataUtils.generate_payee_data()
        self.bill_pay_page.make_bill_payment(payee_data, str(payment_amount), TestUserRegistration.new_account_number)
        self.bill_pay_page.verify_successful_bill_payment()
        self.home_page.click_on_accounts_overview_link()
        self.accounts_overview_page.verify_balance_in_an_account(TestUserRegistration.new_account_number, expected_balance_str)
        response = self.transactions_api.get_all_transactions(TestUserRegistration.new_account_number, str(payment_amount))[0]
        assert response['accountId'] == int(TestUserRegistration.new_account_number)
        assert response['type'] == 'Debit'
        assert response['amount'] == float(payment_amount)




