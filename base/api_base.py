import pdb
from pathlib import Path
import yaml

from playwright.sync_api import sync_playwright

class APiBase:
    def __init__(self, request_context, base_url,session_id, headers=None, timeout=10):
        """
        Initialize the Playwright API client.
        :param request_context : Playwright API request context
        :param base_url: Base URL for the API
        :param headers: Optional headers (default: None)
        :param timeout: Request timeout in milliseconds
        """
        self.request_context = request_context
        self.base_url = base_url.rstrip("/")
        self.headers = headers if headers else {"Content-Type": "application/json", "Cookie": f"JSESSIONID={session_id}"}
        self.timeout = timeout * 1000  # Convert seconds to milliseconds
        self._load_endpoints()

    def _load_endpoints(self):
        """Load API endpoints from endpoints.yml"""
        file_path =  "./api_endpoints.yml"
        with open(file_path, "r") as file:
            self.endpoints = yaml.safe_load(file)

    def get_endpoint(self, key, **kwargs):
        """
        Retrieve the API endpoint with dynamic parameters.
        Example: get_endpoint("transactions", account_id=12345, amount=10, timeout=30000)
        """
        endpoint_template = self.endpoints.get("accounts", {}).get(key, "")
        if not endpoint_template:
            raise ValueError(f"Endpoint '{key}' not found in endpoints.yml")
        return endpoint_template.format(**kwargs)

    def _send_request(self, method, endpoint, params=None, headers=None):
        """
        Send an HTTP request using Playwright's request API.

        :param method: HTTP method (GET, POST, PUT, DELETE, PATCH)
        :param endpoint: API endpoint (relative path)
        :param params: Query parameters
        :param headers: Additional headers (optional)
        :return: Response object
        """
        service_proxy = self.endpoints.get('accounts', {}).get('service_proxy', '')
        url = f"{self.base_url}{service_proxy}/{endpoint.lstrip('/')}"
        headers = {**self.headers, **(headers or {})}
        response = self.request_context.fetch(
            url,
            method=method,
            params=params,
            headers=headers,
            timeout=self.timeout
        )
        if response.ok:
            return response
        else:
            print(f"Error: {response.status} - {response.status_text}")
            return None

    def get(self, endpoint, params=None, headers=None):
        """Perform a GET request."""
        response = self._send_request("GET", endpoint, params=params, headers=headers)
        return response.json()


    def post(self, endpoint, json=None, headers=None):
        """Perform a POST request."""
        response = self._send_request("POST", endpoint, headers=headers)
        return response

    def put(self, endpoint, json=None, headers=None):
        """Perform a PUT request."""
        response = self._send_request("PUT", endpoint, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        """Perform a DELETE request."""
        return self._send_request("DELETE", endpoint, headers=headers)

    def patch(self, endpoint, json=None, headers=None):
        """Perform a PATCH request."""
        response =  self._send_request("PATCH", endpoint, headers=headers)
        return response
