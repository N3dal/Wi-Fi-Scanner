"""
    Docstring;
"""


from os import system
from os import name as OS_NAME


def clear():
    """
        wipe terminal screen;

        return None;
    """

    if OS_NAME == "posix":
        # for all *nix machines;
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for all other machines in this world;
        # system("your-command")
        pass
    
    return None
