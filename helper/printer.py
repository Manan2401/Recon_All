from colorama import Fore


def info(message, *args):
    """
    Print info message with blue color.

    :param message: message to print
    :param args: arguments if any
    """
    print(Fore.BLUE + "[*] " + message + Fore.RESET, *args)


def success(message, *args):
    """
    Print success message with green color.

    :param message: message to print
    :param args: arguments if any

    """
    print(Fore.GREEN + "[+] " + message + Fore.RESET, *args)


def error(message, *args):
    """
    Print error message with red color.

    :param message: message to print
    :param args: arguments if any
    """
    print(Fore.RED + "[!!!] " + message + Fore.RESET, *args)


def warning(message, *args):
    """
    Print warning message with yellow color.

    :param message: message to print
    :param args: arguments if any
    """
    print(Fore.YELLOW + "[!] " + message + Fore.RESET, *args)


def nonprefix(message, *args):
    """
    Print message without prefix.

    :param message: message to print
    :param args: arguments if any
    """
    print(message, *args)
