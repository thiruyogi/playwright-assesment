from playwright.sync_api import Page, Playwright, expect

class LoginPage():

    def __init__(self, page):
        self.page = page

        self.username = self.page.locator("input[name=\"username\"]")
        self.password = self.page.locator("input[name=\"password\"]")
        self.login_button = self.page.get_by_role("button", name="Log In")
        self.register_link = self.page.get_by_role("link", name="Register")
        self.accounts_overview_heading = self.page.get_by_role("heading", name="Accounts Overview")
        self.sign_in_easy_heading = self.page.get_by_role("heading", name="Signing up is easy!")

    def login(self, username, password):

        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def verify_successful_login(self):
        expect(self.accounts_overview_heading, 'Verifying Accounts overview Heading presence').to_be_visible()


    def click_on_register_link(self):
        self.register_link.click()
        expect(self.sign_in_easy_heading,'Verifying Sign in page heading').to_be_visible()

    def get_session_id(self):
        cookies = self.page.context.cookies()
        # Extract JSESSIONID
        jsessionid = next((cookie["value"] for cookie in cookies if cookie["name"] == "JSESSIONID"), None)
        return jsessionid