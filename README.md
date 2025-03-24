# Parabank Automation Suite
    This is an automation test suite to run regression tests on the Parabank web application
## Tools Used:
    1. Playwright
    2. Python
    3. Pytest
    4. Design Pattern: Page Object Model
## Test Scenarios:
    1. Create a new user from the registration page and log in using that user.
    2. Navigate to the global navigation pages and verify them.
    3. Create a new savings account for the new user.
    4. Transfer funds from the new account and verify the balance amount from the Accounts Overview screen.
    5. Make a bill payment from the new account and verify the balance from the Accounts Overview screen.

### API Scenarios:
    1. Assert the response from transaction API for the bill payment done on Scenario 5.

## Folder Structure
    1. tests - Contains all the test files in the suite
    2. pages - Contains all the page object files in the suite
    3. api - Contains all API-related files in the suite
    4. utils - Contains all utility and helper files for the suite
    5. base - Contains test Base and API base files.
    6. reports - Where the pytest HTML report is stored.
    7. configs - Contains different config files for different environments.

## Getting Started:
### Prerequisites:
    1. Python 3.x
    2. Pip
    3. IDE or any text editor
### Local Setup:
    1. Clone this repository using "git clone https://github.com/thiruyogi/playwright-assesment.git".
    2. Navigate to the directory in the terminal and run "pip install -r requirements.txt". This will install all required dependencies including pytest and playwright.
    3. Run the test cases by running "pytest" command.
    4. HTML report will created and stored in the reports folder.

## Key Highlights:
    1. This suite can be run in all the browsers that are supported by playwright. Add "--browser-name <browser>" to pytest command.
    2. Tests are driver from yml config files. By default local.yml will be considered. Add "--config <filename.yml> with pytest command to select a different yml file.
    3. base_url and browser_name can be passed from the command line as well. Values passed in the command line will be given preference.
    4. A light-weight HTML report is integrated which can used for communicating the results.
    5. Playwright tracer is on for failed test cases to help in debugging.

## Further Enhancements:
    1. Add a wrapper file for page-related functions to enhance easy maintenance.
    2. Integrate the Allure report for catchy and informative reporting.

## Sample Execution Result:
<img width="1512" alt="image" src="https://github.com/user-attachments/assets/9ac42240-d86f-436c-9dd7-a46549bb7688" />
