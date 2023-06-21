"""Unit test for the console module."""
import json
from typing import Tuple
from unittest.mock import call, patch

from koodousfinder.console import get_mb_size, show_results, show_stix_results
from koodousfinder.response import Response


def get_data() -> Tuple[str, dict]:
    """Craft data to use in tests."""
    search_used = "com.app.guardiao30h"
    raw = {
        "app": "Modulo Guardi\u00e3o",
        "package_name":  search_used,
        "version": "",
        "size": 1,
        "sha256": "2efc944bf9a52f3096acb26307904e8a27d8f4c79b62a18e8e41aa99ddae505a",
        "url": "http://test/"
    }
    return search_used, raw


@patch('builtins.print')
def test_show_stix_results(mocked_print) -> None:
    """Test the method parse_requirements."""
    search_used, raw = get_data()
    response = Response(**raw)
    show_stix_results(
        search_used=search_used,
        response=[response]
    )
    output = json.loads(mocked_print.call_args.args[0])
    assert output.get('id')
    assert output.get('type') == "bundle"
    for obj in output.get('objects'):
        assert obj.get("id")
        # relationship object doesn't has name
        if obj.get("name"):
            assert search_used in obj.get("name")

@patch('builtins.print')
def test_show_results(mocked_print) -> None:
    """Test the method parse_requirements."""
    search_used, raw = get_data()
    response = Response(**raw)
    show_results(
        response=[response]
    )
    sha256 = '2efc944bf9a52f3096acb26307904e8a27d8f4c79b62a18e8e41aa99ddae505a'
    assert mocked_print.mock_calls == [
        call('App Name: Modulo Guardião'),
        call(f'Package Name: {search_used}'),
        call('App Version: '),
        call('Size: 0.0 MB'),
        call(f'SHA256: \x1b[32m{sha256}\x1b[0m'),
        call('URL: http://test/'),
        call('--------------------------------------------------')
    ]

def test_get_mb_size() -> None:
    get_mb_size(0)
    get_mb_size(None)
