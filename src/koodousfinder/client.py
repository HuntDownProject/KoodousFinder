"""Koodous client."""
from typing import List

import requests

from .response import Response

API_ENDPOINT = "https://developer.koodous.com/apks/"
TIMEOUT = 60


class Client:
    """A wrapper for Koodous endpoint."""

    def __init__(self, api_key: str) -> None:
        """Class constructor."""
        self.headers = {"Authorization": f"Token {api_key}"}
        self.query_params = {} # {"search": ""}

    def get_app_name(self, app_name: str) -> List[Response]:
        """Query based in an application name."""
        self.query_params["search"] = f"app: {app_name}"
        return self._get()

    def get_package_name(self, package_name: str) -> List[Response]:
        """Query based in an package name."""
        self.query_params["search"] = f"package: {package_name}"
        return self._get()

    def _get(self) -> List[Response]:
        """A wrapper method for requests get."""
        response = requests.get(
            API_ENDPOINT,
            params=self.query_params,
            headers=self.headers,
            timeout=TIMEOUT
        )

        response.raise_for_status()
        response_dict = response.json()

        if response_dict.get('results'):
            output = []
            for result in response_dict.get('results'):
                output.append(Response(**result))

            return output

        raise KeyError(f"Invalid payload, 'results' not found: {response.text}")
