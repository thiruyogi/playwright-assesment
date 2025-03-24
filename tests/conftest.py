import pdb
from email.policy import default
from idlelib.rpc import request_queue

import pytest
import yaml

def load_config(config_file):
    config_path = f"./config/{config_file}"
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="local.yml", help="Path to the config file")
    parser.addoption(
        "--browser_name", action="store", default=None, help="browser selection"
    )
    parser.addoption(
        "--url_name", action="store", default=None, help="server selection"
    )


# @pytest.fixture
# def user_credentials(request):
#     return request.param

@pytest.fixture(scope="class")
def setup(playwright, request):
    # Get config file path from command line (default: config.yml)
    config_file = request.config.getoption("--config")
    # Load configuration
    config_data = load_config(config_file)
    pdb.set_trace()
    # Override base_url if passed from command line
    browser_name = request.config.getoption('browser_name') or config_data['browser_name']
    url = request.config.getoption('url_name') or config_data['base_url']
    config_data['base_url'] = url
    config_data['browser_name'] = browser_name

    if browser_name.lower() == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    else:
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    # Create Playwright request context for API tests
    request_context = playwright.request.new_context()

    # Attach both page and API context to the test class
    request.cls.page = page
    request.cls.request_context = request_context
    request.cls.base_url = url
    yield
    context.close()
    browser.close()