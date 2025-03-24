import pdb

from base.api_base import APiBase


class TransactionsApi(APiBase):

    def __init__(self, request_context, base_url, session_id):
        super().__init__(request_context, base_url, session_id)


    def get_all_transactions(self, account_number, amount):
        endpoint = self.get_endpoint("transactions", account_id=account_number, amount=amount, timeout=30000)
        return self.get(endpoint)