# weather.py

import argparse
import json
import sys
from configparser import ConfigParser
from urllib import error, parse, request
# from pprint import pp

BASE_MASTODON_API_URL = "http://3615.computer/api/1/statuses"

def _get_access_token():
    """Fetch the API key from your configuration file.


    Expects a configuration file named "secrets.ini" with structure:


        [openweather]

        api_key=<YOUR-OPENWEATHER-API-KEY>

    """

    config = ConfigParser()
    config.read("secrets.ini")

    return config["3615.computer"]["access_token"]


def read_user_cli_args():
    """Handles the CLI user interactions.


    Returns:

        argparse.Namespace: Populated namespace object

    """

    parser = argparse.ArgumentParser(
        description="gets text content and posts it to the fediverse"
    )

    parser.add_argument("text", nargs="+", type=str, help="enter the text content")

    return parser.parse_args()

if __name__ == "__main__":
    print(f"access_token : {_get_access_token()}")

    user_args = read_user_cli_args()
    print(user_args.text)
