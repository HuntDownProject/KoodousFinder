"""Unit test for the Koodous client implementation."""
import json
import os
from typing import List
from unittest.mock import patch

import pytest

from koodousfinder import Client
from koodousfinder.response import Response


def test_build_client() -> None:
    """Test the method parse_requirements."""
    my_client = Client(api_key='')
    assert isinstance(my_client, Client)

    file_path = os.path.join(
        os.path.dirname(__file__),
        'data',
        'payload.json'
    )

    with open(file_path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = payload

        # test get_app_name method
        response = my_client.get_app_name(app_name="Modulo Guardiao")
        assert isinstance(response, List)
        for item in response:
            assert isinstance(item, Response)

        # test get_package_name method
        response = my_client.get_package_name(package_name="net.droidjack.server")
        assert isinstance(response, List)
        for item in response:
            assert isinstance(item, Response)

        # test get_package_name method but raising exception
        mock_get.return_value.json.return_value = {}
        with pytest.raises(KeyError):
            response = my_client.get_package_name(package_name="net.droidjack.server")
