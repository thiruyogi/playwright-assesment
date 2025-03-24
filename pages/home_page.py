from playwright.sync_api import expect


class HomePage():

    def __init__(self, page):
        self.page = page

        #Elements in the navigation menu
        self.solutions_link = self.page.get_by_text("Solutions")
        self.about_us_link = self.page.locator("#headerPanel").get_by_role("link", name="About Us")
        self.services_link = self.page.locator("#headerPanel").get_by_role("link", name="Services")
        self.products_link = self.page.locator("#headerPanel").get_by_role("link", name="Products")
        self.locations_link = self.page.locator("#headerPanel").get_by_role("link", name="Locations")
        self.admin_page_link = self.page.get_by_role("link", name="Admin Page")

        #Elements for headers of the navigation menu pages
        self.about_us_heading = self.page.get_by_role("heading", name="ParaSoft Demo Website")
        self.services_heading = self.page.get_by_text("Available Bookstore SOAP")
        # self.products_page_link = "/products"
        # self.locations_page_link = "/solutions"
        self.parasoft_logo_image = self.page.get_by_role("banner").get_by_role("link", name="Parasoft logo")
        self.admin_page_heading = self.page.get_by_role("heading", name="Administration")

        #Elements in the secondary menu
        self.open_new_account_link = self.page.get_by_role("link", name="Open New Account")
        self.open_new_account_heading = self.page.get_by_role("heading", name="Open New Account")
        self.accounts_overview_link = self.page.get_by_role("link", name="Accounts Overview")
        self.accounts_overview_page_heading = self.page.get_by_role("heading", name="Accounts Overview")
        self.transfer_funds_link = self.page.get_by_role("link", name="Transfer Funds")
        self.transfer_fund_page_heading = self.page.get_by_role("heading", name="Transfer Funds")
        self.bill_pay_link = self.page.get_by_role("link", name="Bill Pay")
        self.bill_pay_page_heading = self.page.get_by_role("heading", name="Bill Payment Service")

    def verify_about_us_link(self):
        self.about_us_link.click()
        expect(self.about_us_heading, 'Verifying About us header in about us page').to_be_visible()

    def verify_services_link(self):
        self.services_link.click()
        expect(self.services_heading, 'Verifying Services header in Services page').to_be_visible()

    def verify_admin_page_link(self):
        self.admin_page_link.click()
        expect(self.admin_page_heading, 'Verifying Administration header in about us page').to_be_visible()

    def verify_products_link(self):
        self.products_link.click()
        # expect(self.page).to_have_url(lambda url: self.products_page_link in url)
        expect(self.parasoft_logo_image, 'Verifying Parasoft logo in products page').to_be_visible()
        self.page.go_back()

    def verify_locations_link(self):
        self.locations_link.click()
        # expect(self.page).to_have_url(lambda url: self.locations_page_link in url)
        expect(self.parasoft_logo_image, 'Verifying Parasoft logo in locations page').to_be_visible()
        self.page.go_back()

    def click_on_open_new_account_link(self):
        self.open_new_account_link.click()
        expect(self.open_new_account_heading, 'Verifying Account open header').to_be_visible()

    def click_on_accounts_overview_link(self):
        self.accounts_overview_link.click()
        expect(self.accounts_overview_page_heading, 'Verifying accounts overview heading').to_be_visible()

    def click_on_transfer_funds_link(self):
        self.transfer_funds_link.click()
        expect(self.transfer_fund_page_heading, 'Verifying transfer funds page heading').to_be_visible()

    def click_on_bill_pay_link(self):
        self.bill_pay_link.click()
        expect(self.bill_pay_page_heading, 'Verifying bill pay page heading').to_be_visible()