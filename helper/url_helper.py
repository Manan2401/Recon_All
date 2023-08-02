import requests
import random
import json
from helper import printer
from utils import randomuser


def get_file(path):
    """
    Downloads the file from the given url and saves it to the current directory

    """
    try:
        # printer.info(f"Getting file from '{BASE_URL + path}'..!")
        headers = {
            "User-Agent": random.choice(randomuser.users)
        }
        r = requests.get(BASE_URL + path, headers=headers)
        with open(path, 'wb') as f:
            f.write(r.content)
        printer.success(f"Successfully downloaded file to '{path}'..!")
    except requests.exceptions.ConnectionError:
        printer.error("Unable to connect to the server..!")


def read_content(path):
    """
    Reads the content of the file from the given url

    """
    try:
        # printer.info(f"Getting file from '{BASE_URL + path}'..!")
        headers = {
            "User-Agent": random.choice(randomuser.users)
        }
        r = requests.get(BASE_URL + path, headers=headers)
        return r.text
    except requests.exceptions.ConnectionError:
        printer.error("Unable to connect to the server..!")


def read_json_content(path):
    """
    Reads the content of a json file from the given url
    """
    try:
        # printer.info(f"Getting file from '{BASE_URL + path}'..!")
        headers = {
            "User-Agent": random.choice(randomuser.users)
        }
        r = requests.get(BASE_URL + path, headers=headers)
        return json.loads(r.text)
    except requests.exceptions.ConnectionError:
        printer.error("Unable to connect to the server..!")
