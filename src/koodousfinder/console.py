"""This is the main module for koodousfinder application."""


import argparse
import getpass
import math
from typing import List, Optional

import keyring
from stix2 import Bundle, Grouping, Indicator

from .client import Client
from .response import Response


def get_api_key():
    """Get the api-key for koodous service."""
    api_key = keyring.get_password("koodousfinder", "api_key")
    if not api_key:
        api_key = getpass.getpass(
            "Koodous api-key not found, entry one to continue: ")
        keyring.set_password("koodousfinder", "api_key", api_key)
    return api_key


def run():
    """Main method that run the application."""
    # Set up command line arguments
    parser = argparse.ArgumentParser(
        description="Search for an APK on Koodous.")
    parser.add_argument(
        "--package-name", type=str, help="Package name of the APK to search for"
    )
    parser.add_argument(
        "--app-name", type=str, help="Name of the app to search for"
    )
    parser.add_argument(
        "--stix", 
        help="Show the output as bundle to share the results using Stix2",
        action='store_true',
        default=False
    )
    args = parser.parse_args()

    client = Client(
        api_key=get_api_key()
    )

    response : List[Response] = []
    search_used = ""
    try:
        if args.package_name:
            response = client.get_package_name(
                package_name=args.package_name
            )
            search_used = args.package_name
        if args.app_name:
            response = client.get_app_name(
                app_name=args.app_name
            )
            search_used = args.app_name
    except Exception as ex:  # pylint: disable=broad-exception-caught)
        print(ex)
        return

    if args.stix:
        show_stix_results(search_used=search_used, response=response)
        return

    show_results(response=response)


def show_stix_results(search_used: str, response: List[Response]):
    """Show results in Stix format."""
    list_indicators = []
    for result in response:
        description = f"{result.app} => {result.package_name}"
        indicator = Indicator(
            name=description,
            pattern=f"[file:hashes.sha256 = '{result.sha256}']",
            pattern_type="stix",
            external_references=[
                {
                "url": result.url,
                "source_name": "koodous.com",
                }
            ]
        )
        list_indicators.append(indicator)

    grouping = Grouping(
        name=f"Hunting for {search_used}",
        context=f"Koodous search used: {search_used}",
        object_refs=list_indicators
    )
    bundle = Bundle(list_indicators, grouping)
    print(bundle.serialize())

def show_results(response: List[Response]):
    """Show results in console."""
    sha256_counts = {}
    for result in response:
        app_size_hr = get_mb_size(result.size)
        sha256 = result.sha256
        if sha256 != "N/A":
            sha256_counts[sha256] = sha256_counts.get(sha256, 0) + 1

        print(f"App Name: {result.app}")
        print(f"Package Name: {result.package_name}")
        sha256_color = (
            "\033[32m" if sha256_counts.get(sha256, 0) == 1 else "\033[31m"
        )
        print(f"App Version: {result.version}")
        print(f"Size: {app_size_hr}")
        print(f"SHA256: {sha256_color}{sha256}\033[0m")
        print(f"URL: {result.url}")
        print("-" * 50)

def get_mb_size(app_size: Optional[int]) -> str:
    if app_size:
        return f"{round(app_size / math.pow(1024, 2), 2)} MB"

    return "N/A"
