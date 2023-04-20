import requests
import argparse
import math
import keyring
import getpass


def get_api_key():
    api_key = keyring.get_password("koodousfinder", "api_key")
    if not api_key:
        api_key = getpass.getpass("Koodous api-key not found, entry one to continue: ")
        keyring.set_password("koodousfinder", "api_key", api_key)
    return api_key


def run():
    api_endpoint = 'https://developer.koodous.com/apks/'
    query_params = {'search': 'com.brata'}

    # Set up headers with API key
    api_key = get_api_key()
    headers = {'Authorization': f'Token {api_key}'}

    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Search for an APK on Koodous.')
    parser.add_argument('--package-name', type=str, help='Package name of the APK to search for')
    parser.add_argument('--app-name', type=str, help='Name of the app to search for')
    args = parser.parse_args()

    query_params = {}
    if args.package_name:
        query_params['search'] = args.package_name
    if args.app_name:
        query_params['app'] = args.app_name

    response = requests.get(api_endpoint, params=query_params, headers=headers)

    if response.status_code == 200:
        results = response.json()['results']
        sha256_counts = {}
        for result in results:
            app_name = result.get('app', 'N/A')
            package_name = result.get('package_name', 'N/A')
            app_version = result.get('version', 'N/A')
            app_size = result.get('size', 'N/A')
            if app_size != 'N/A':
                app_size_hr = f"{round(app_size / math.pow(1024, 2), 2)} MB"
            else:
                app_size_hr = 'N/A'
            sha256 = result.get('sha256', 'N/A')
            if sha256 != 'N/A':
                sha256_counts[sha256] = sha256_counts.get(sha256, 0) + 1

            print(f"App Name: {app_name}")
            print(f"Package Name: {package_name}")
            sha256_color = '\033[32m' if sha256_counts.get(sha256, 0) == 1 else '\033[31m'
            print(f"App Version: {app_version}")
            print(f"Size: {app_size_hr}")
            print(f"SHA256: {sha256_color}{sha256}\033[0m")
            print("-" * 50)
    else:
        print(f"Error: {response.status_code} - {response.content}")
