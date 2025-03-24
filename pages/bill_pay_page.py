import time

from playwright.sync_api import expect


class BillPayPage():

    def __init__(self, page):
        self.page = page

        self.payee_name_textbox = self.page.locator("input[name=\"payee\\.name\"]")
        self.payee_address_textbox = self.page.locator("input[name=\"payee\\.address\\.street\"]")
        self.payee_city_textbox = self.page.locator("input[name=\"payee\\.address\\.city\"]")
        self.payee_state_textbox = self.page.locator("input[name=\"payee\\.address\\.state\"]")
        self.payee_zip_code_textbox = self.page.locator("input[name=\"payee\\.address\\.zipCode\"]")
        self.payee_phone_textbox = self.page.locator("input[name=\"payee\\.phoneNumber\"]")
        self.payee_account_number_textbox = self.page.locator("input[name=\"payee\\.accountNumber\"]")
        self.confirm_payee_account_number_textbox = self.page.locator("input[name=\"verifyAccount\"]")
        self.payee_amount_textbox = self.page.locator("input[name=\"amount\"]")
        self.pay_from_account_dropdown = self.page.get_by_role("combobox")
        self.send_payment_button = self.page.get_by_role("button", name="Send Payment")
        self.bill_payment_completed_message = self.page.get_by_role("heading", name="Bill Payment Complete")

    def make_bill_payment(self, payee_data, amount, from_account):
        """

        :param dict payee_data: All necessary payee field values
        :param string amount: Amount to be paid
        :param string from_account: Account number from which amount should be paid
        :return:
        """
        self.payee_name_textbox.fill(payee_data['name'])
        self.payee_address_textbox.fill(payee_data['address'])
        self.payee_city_textbox.fill(payee_data['city'])
        self.payee_state_textbox.fill(payee_data['state'])
        self.payee_zip_code_textbox.fill(payee_data['zipcode'])
        self.payee_phone_textbox.fill(payee_data['phone'])
        self.payee_account_number_textbox.fill(payee_data['account_number'])
        self.confirm_payee_account_number_textbox.fill(payee_data['account_number'])
        self.payee_amount_textbox.fill(amount)
        self.pay_from_account_dropdown.select_option(from_account)
        time.sleep(2)
        self.send_payment_button.click()

    def verify_successful_bill_payment(self):
        expect(self.bill_payment_completed_message, 'Verifying whether bill payment success message is displayed or not').to_be_visible()
