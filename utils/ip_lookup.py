import json
import time
import requests
import random
import socket
from helper import printer
from utils import randomuser


class Lookup:
    """
    Gets information about a given ip address using https://ipinfo.io/

    :param ip: The ip address to search for.
    """
    def __init__(self, ip):
        try:
            ip = socket.gethostbyname(ip)
            url = f"https://ipinfo.io/{ip}/json"
            headers = {'User-Agent': random.choice(randomuser.users)}
            url = requests.get(url, headers=headers)
            # printer.info(url.text)
            values = json.loads(url.text)

            printer.info(f"Trying to find information for '{ip}'...")
            time.sleep(1)

            for value in values:
                # If value contains readme, skip it.
                if value == "readme":
                    continue
                elif value == "" or value is None:
                    value = "Not Found"

                printer.success(f"{value.capitalize()} - ", values[value])

            printer.success(f"Maps URL - ", f"https://www.google.com/maps/search/{values['loc']}")

        except Exception as e:
            printer.error(f"Error : {e}")
            pass
