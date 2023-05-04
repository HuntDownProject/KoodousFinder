"""This is the main module for koodousfinder application."""


import argparse
import getpass
import math
from typing import List

import keyring

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
    args = parser.parse_args()

    client = Client(
        api_key=get_api_key()
    )

    response : List[Response] = []
    try:
        if args.package_name:
            response = client.get_package_name(
                package_name=args.package_name
            )
        if args.app_name:
            response = client.get_app_name(
                app_name=args.app_name
            )
    except Exception as ex:  # pylint: disable=broad-exception-caught)
        print(ex)
        return

    sha256_counts = {}
    for result in response:
        app_name = result.app
        package_name = result.package_name
        app_version = result.version
        app_size = result.size
        if app_size:
            app_size_hr = f"{round(app_size / math.pow(1024, 2), 2)} MB"
        else:
            app_size_hr = "N/A"
        sha256 = result.sha256
        if sha256 != "N/A":
            sha256_counts[sha256] = sha256_counts.get(sha256, 0) + 1

        print(f"App Name: {app_name}")
        print(f"Package Name: {package_name}")
        sha256_color = (
            "\033[32m" if sha256_counts.get(sha256, 0) == 1 else "\033[31m"
        )
        print(f"App Version: {app_version}")
        print(f"Size: {app_size_hr}")
        print(f"SHA256: {sha256_color}{sha256}\033[0m")
        print("-" * 50)
