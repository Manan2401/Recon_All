import os
from helper import printer
import time
import subprocess


class Scan:
    """
    Scans for the available Wi-Fi networks.

    Requires netsh for Windows and nmcli for Linux.
    """
    def __init__(self):
        printer.info("Linux system detected..! Doing an nmcli scan...")
        time.sleep(1)
        try:
            subprocess.run(["nmcli", "dev", "wifi"], check=True)
        except subprocess.CalledProcessError as e:
            printer.error(f"Error : {e.returncode}")
