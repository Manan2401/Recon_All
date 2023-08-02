#!/usr/bin/env python3

import os
import time
from colorama import Fore
import socket
import requests
from getpass import getpass
from utils import (
    email_search,
    search_username,
    ig_scrape,
    whois_lookup,
    webhook_spammer,
    port_scanner,
    ip_lookup,
    phonenumber_lookup,
    websearch,
    smsbomber,
    web_scrape,
    wifi_finder,
    wifi_password_getter,
    fake_info_generator,
    dirbuster,
)
from helper import printer, url_helper


if os.name == "posix":
    os.system("clear")

version = "0.1.0"


def internet_check():
    """
    Checks if the internet connection is available.

    :return: None
    """
    try:
        socket.create_connection(("www.google.com", 80))
        printer.success("\nInternet Connection is Available!")
        return None
    except OSError:
        printer.warning("\nWarning! Internet Connection is Unavailable!")
        return None


def print_banner():
    """
    Prints the banner of Recon_All.
    """
    print(Fore.CYAN + f"""
[+]
|
|    //   ) )                                            // | |           
|   //___/ /   ___      ___      ___       __           //__| |    // //  
|  / ___ (   //___) ) //   ) ) //   ) ) //   ) ) ____  / ___  |   // //   
| //   | |  //       //       //   / / //   / /       //    | |  // //    
|//    | | ((____   ((____   ((___/ / //   / /       //     | | // //     
|
|
| by Manan
|
| NOTE! THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSES, DONT USE IT TO DO SOMETHING ILLEGAL!
|
[+]
    """)


def print_about():
    """
    Prints the about text.
    """
    print(Fore.GREEN)
    printer.nonprefix(f"Recon_All, collection of multiple tools for scraping, OSINT and more.\n")
    printer.nonprefix(f"Completely open source and free to use! Feel free to contribute.\n")
    printer.nonprefix(f"Repo: https://github.com/Manan2401/Recon_All\n")
    printer.nonprefix(f"NOTE! THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSES, DONT USE IT TO DO SOMETHING ILLEGAL!\n")



def print_menu():
    """
    Prints the main menu of H4X-Tools.
    """
    print(Fore.CYAN)
    print("[1] IG Scrape*           ||   [2] Web Search")
    print("[3] Phone Lookup         ||   [4] IP Lookup")
    print("[5] Username Search*     ||   [6] Email Search")
    print("[7] Port Scanner         ||   [8] Webhook Spammer*")
    print("[9] WhoIs Scan           ||   [10] SMS Bomber (US Only!)*")
    print("[11] Fake Info Generator ||   [12] Web Scrape*")
    print("[13] Wi-Fi Finder        ||   [14] Saved Wi-Fi Passwords")
    print("[15] Dir Buster          ||   [16] About")
    print("[19] Exit")
    print("\n")


def handle_ig_scrape():
    """
    Handles the IG Scrape util.

    Note, you have to log in to Instagram in order to use this util.
    """
    printer.warning("NOTE! You have to log in to Instagram everytime in order to use this util.")
    printer.warning("I suggest you to create a new account for this purpose.")
    username = str(input("Your username : "))
    password = getpass("Your password : ")
    target = str(input("Enter a target username : \t")).replace(" ", "_")
    ig_scrape.Scrape(username, password, target)
    time.sleep(1)


def handle_web_search():
    """
    Handles the Web Search util.
    """
    query = str(input("Search query : \t"))
    websearch.Search(query)


def handle_phone_lookup():
    """
    Handles the Phone number Lookup util.
    """
    no = str(input("Enter a phone-number with country code : \t"))
    phonenumber_lookup.LookUp(no)


def handle_ip_lookup():
    """
    Handles the IP/Domain Lookup util.
    """
    ip = str(input("Enter a IP address OR domain : \t"))
    ip_lookup.Lookup(ip)


def handle_username_search():
    """
    Handles the Username Search util.
    """
    username = str(input("Enter a Username : \t")).replace(" ", "_")
    search_username.Search(username)


def handle_email_search():
    """
    Handles the Email Search util.
    """
    email = str(input("Enter a email address : \t"))
    email_search.Holehe(email)


def handle_port_scanner():
    """
    Handles the Port Scanner util.
    """
    ip = str(input("Enter a IP address OR domain : \t"))
    port_range = int(input("Enter number of ports to scan : \t"))
    port_scanner.Scan(ip, port_range)


def handle_webhook_spammer():
    """
    Handles the Webhook Spammer util.
    """
    url = str(input("Enter a webhook url : \t"))
    amount = int(input("Enter a amount of messages : \t"))
    message = str(input("Enter a message : \t"))
    username = str(input("Enter a username : \t"))
    throttle = int(input("Enter time of sleep (seconds) : \t"))
    webhook_spammer.Spam(url, amount, message, username, throttle)


def handle_whois_lookup():
    """
    Handles the WhoIs Lookup util.
    """
    domain = str(input("Enter a domain : \t"))
    whois_lookup.Lookup(domain)


def handle_sms_bomber():
    """
    Handles the SMS Bomber util.

    Currently only works for US numbers.
    """
    number = str(input("Enter mobile number : \t")).strip("+")
    count = int(input("Enter number of Messages : \t"))
    throttle = int(input("Enter time of sleep : \t"))
    smsbomber.Spam(number, count, throttle)


def handle_fake_info_generator():
    """
    Handles the Fake Info Generator util.
    """
    fake_info_generator.Generate()


def handle_web_scrape():
    """
    Handles the Web Scrape util.
    """
    url = str(input(f"Enter a url : \t"))
    web_scrape.Scrape(url)


def handle_wifi_finder():
    """
    Handles the Wi-Fi Finder util.
    """
    printer.info(f"Scanning for nearby Wi-Fi networks...")
    wifi_finder.Scan()


def handle_wifi_password_getter():
    """
    Handles the Wi-Fi Password Getter util.
    """
    printer.info(f"Scanning for locally saved Wi-Fi passwords...")
    wifi_password_getter.Scan()


def handle_dir_buster():
    """
    Handles the Dir Buster util.
    """
    url = input(f"Enter a domain : \t")
    dirbuster.Scan(url)




# Create a dictionary to map menu options to corresponding functions
menu_options = {
    "1": handle_ig_scrape,
    "2": handle_web_search,
    "3": handle_phone_lookup,
    "4": handle_ip_lookup,
    "5": handle_username_search,
    "6": handle_email_search,
    "7": handle_port_scanner,
    "8": handle_webhook_spammer,
    "9": handle_whois_lookup,
    "10": handle_sms_bomber,
    "11": handle_fake_info_generator,
    "12": handle_web_scrape,
    "13": handle_wifi_finder,
    "14": handle_wifi_password_getter,
    "15": handle_dir_buster,
    "16": print_about,
    "17": print_donate,
    "18": update
}


def __main__():
    """
    Main function.
    """
    while True:
        print_banner()
        time.sleep(1)
        print_menu()
        a = input("[*] Select your option : \t")

        if a in menu_options:
            menu_options[a]()  # Call the corresponding function based on the selected option
            time.sleep(3)  # Sleep so user has time to see results.
        elif a == "19":
            printer.warning("Exiting...")
            printer.info("Thanks for using Recon-All! Remember to star this on GitHub! \n -Manan")
            time.sleep(1)
            print(Fore.RESET)
            break
        else:
            printer.error("Invalid option!")
            time.sleep(2)


if __name__ == "__main__":
    __main__()
