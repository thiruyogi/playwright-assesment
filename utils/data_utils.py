from faker import Faker
import random
import string

class DataUtils():
    faker = Faker()

    @staticmethod
    def get_first_name():
        """Generate a random first name."""
        return DataUtils.faker.first_name()

    @staticmethod
    def get_last_name():
        """Generate a random last name."""
        return DataUtils.faker.last_name()

    @staticmethod
    def get_address():
        """Generate a random street address."""
        return DataUtils.faker.street_address()

    @staticmethod
    def get_city():
        """Generate a random city."""
        return DataUtils.faker.city()

    @staticmethod
    def get_state():
        """Generate a random state abbreviation."""
        return DataUtils.faker.state_abbr()

    @staticmethod
    def get_zip_code():
        """Generate a random ZIP code."""
        return DataUtils.faker.zipcode()

    @staticmethod
    def get_phone_number():
        """Generate a random phone number."""
        return DataUtils.faker.phone_number()

    @staticmethod
    def get_ssn():
        """Generate a random Social Security Number (SSN)."""
        return DataUtils.faker.ssn()

    @staticmethod
    def get_account_number():

        return DataUtils.faker.bban()

    @staticmethod
    def get_random_username():
        """Generate a random username with digits appended to ensure uniqueness."""
        return DataUtils.faker.user_name() + ''.join(random.choices(string.digits, k=4))

    @staticmethod
    def get_password():
        """Generate a secure password (you can modify the logic if needed)."""
        return "Test@123"  # You can also randomize this if required

    @staticmethod
    def get_email():
        """Generate a random email address."""
        return DataUtils.faker.email()

    @staticmethod
    def get_unique_email():
        """Generate a unique email address with a random numeric suffix."""
        return f"{DataUtils.faker.user_name()}{random.randint(1000, 9999)}@example.com"

    @staticmethod
    def generate_user_data():
        user_data = {
            'firstname':DataUtils.get_first_name(),
            'lastname': DataUtils.get_last_name(),
            'address':DataUtils.get_address(),
            'city': DataUtils.get_city(),
            'state': DataUtils.get_state(),
            'zipcode': DataUtils.get_zip_code(),
            'phone': DataUtils.get_phone_number(),
            'ssn': DataUtils.get_ssn(),
            'username': DataUtils.get_random_username(),
            'password': DataUtils.get_password(),
            'confirm_password': DataUtils.get_password(),
        }

        return user_data
    @staticmethod
    def generate_payee_data():
        payee_data = {
            'name': DataUtils.get_first_name(),
            'address': DataUtils.get_address(),
            'city': DataUtils.get_city(),
            'state': DataUtils.get_state(),
            'zipcode': DataUtils.get_zip_code(),
            'phone': DataUtils.get_phone_number(),
            'account_number': str(random.randint(100000, 999999))
        }

        return payee_data