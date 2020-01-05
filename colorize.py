"""
    This is a simple module that allows you to
    print in color in the terminal.  You can chose
    4 different settings(bold, underlined, strikethrough, or regular
    color), along with 5 colors to print errors or
    warnings in.
"""


def normal(style, text):
    """
    print plain colored text
    """
    dictionary1 = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "purple": "35",
        "cyan": "36",
        "white": "37",
    }

    return ("\033[%sm" % dictionary1[style]) + str(text) + "\033[0;0m"


def bold(style, text):
    """
    print bold colored text
    """
    dictionary2 = {
        "black": "1;30",
        "red": "1;31",
        "green": "1;32",
        "yellow": "1;33",
        "blue": "1;34",
        "purple": "1;35",
        "cyan": "1;36",
        "white": "1;37",
    }
    return ("\033[%sm" % dictionary2[style]) + str(text) + "\033[0;0m"


def underline(style, text):
    """
    print underlined colored text
    """
    dictionary3 = {
        "black": "4;30",
        "red": "4;31",
        "green": "4;32",
        "yellow": "4;33",
        "blue": "4;34",
        "purple": "4;35",
        "cyan": "4;36",
        "white": "4;37",
    }
    return ("\033[%sm" % dictionary3[style]) + str(text) + "\033[0;0m"


def error(style, text):
    """
    print colored text for errors or warnings
    """
    dictionary4 = {
        "ERROR1": "1;36;41",
        "ERROR2": "1;34;103",
        "ERROR3": "4;90;101",
        "ERROR4": "1;35;7",
        "ERROR5": "4;30;107",
    }
    return ("\033[%sm" % dictionary4[style]) + str(text) + "\033[0;0m"


def strike(style, text):
    """
    print strikethrough colored text
    """
    dictionary5 = {
        "black": "9;30",
        "red": "9;31",
        "green": "9;32",
        "yellow": "9;33",
        "blue": "9;34",
        "purple": "9;35",
        "cyan": "9;36",
        "white": "9;37",
    }
    return ("\033[%sm" % dictionary5[style]) + str(text) + "\033[0;0m"
