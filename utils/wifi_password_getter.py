import os
import subprocess
import re
from helper import printer
import time


class Scan:
    """
    Scans for the saved Wi-Fi passwords on the system.
    """

    def __init__(self):
        printer.info(f"Linux system detected..!\n")
        time.sleep(1)
        try:
            output = subprocess.check_output(['nmcli', '-f', 'NAME,UUID', 'connection', 'show', '--active'])
            connections = re.findall(r'(\S+)\s+([0-9a-f-]{36})', output.decode())
            for ssid, uuid in connections:
                password_output = subprocess.check_output(
                    ['nmcli', '-s', '-g', '802-11-wireless-security.psk', 'connection', 'show', uuid])
                password = password_output.decode().strip()
                printer.success(f"SSID: {ssid}")
                printer.success(f"Password: {password}\n")

        except OSError as e:
            printer.error("Is your system using nmcli?")
            printer.error(f"Error : ", e)
            pass
