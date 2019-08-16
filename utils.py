"""
The utils has helper methods for the main

"""

import re

def readFile(file):
    """Reads the commands and splits on newlines"""
    f = (open(file, 'r').read()).splitlines()
    return f

def preprocessCommands(commandLine):
    """The splitted commands are preprocessed for its roles"""
    regex_command = re.sub("PLACE ","",commandLine)
    commands = regex_command.split(",")
    return commands

