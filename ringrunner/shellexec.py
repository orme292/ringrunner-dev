#!/usr/local/bin/python3
import sys
import os
import subprocess
import urllib

from .configuration import CLIConfig
from .helpers import *

class ShellEX():


    def __init__(self):

        self.config = CLIConfig()
        self.debug = False


    def run_command (self, cmd, host, **kwargs):

        if not cmd or not host:
            return False

        command = "ssh {options} {host} -- {command}; exit 0".format(options=self.config.SCRIPT_SSH_OPTIONS, host=host, command=cmd)

        debugMessage(" Exec: {command}".format(command=command), self.debug)

        try:
            result = subprocess.check_output(command, shell=True, universal_newlines=True)

        except subprocess.CalledProcessError:
            print("An unknown error ooccurred when executing the command:", command)
            sys.exit()

        print (result)
