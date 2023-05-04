"""Unit test for the Koodous client implementation."""
from koodousfinder import Client


def test_build_client() -> None:
    """Test the method parse_requirements."""
    my_client = Client(api_key='')
    assert isinstance(my_client, Client)
