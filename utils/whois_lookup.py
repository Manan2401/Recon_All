import whoisdomain
from helper import printer
import time


class Lookup:
    """
    Looks up for the information of a given domain.

    :param domain: The domain name.
    """
    def __init__(self, domain):
        try:
            q = whoisdomain.query(domain)
            printer.info(f"Trying to find the information of '{domain}'...")
            time.sleep(1)
            for key in q.__dict__:
                printer.success(key, "-", q.__dict__[key])
        except Exception as e:
            printer.error("Error : ", e)
            printer.error("Make sure you have 'whois' installed on your system..!")
