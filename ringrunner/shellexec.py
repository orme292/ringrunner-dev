#!/usr/local/bin/python3
import os
import subprocess
import sys
import urllib


from .configuration import CLIConfig
from .helpers import *

class ShellEX():


    def __init__(self):

        self.config = CLIConfig()
        self.debug = False
        self.testmode = False

    def run_command (self, cmd, host, **kwargs):

        if not cmd or not host:
            return False

        command = "ssh {options} {host} -- {command}; exit 0".format(options=self.config.SCRIPT_SSH_OPTIONS, host=host, command=cmd)

        debugMessage("Exec: {command}".format(command=command), self.debug)

        if not self.config.SCRIPT_TESTMODE:
            try:
                result = subprocess.check_output(command, shell=True, universal_newlines=True)

            except subprocess.CalledProcessError:
                debugMessage("subprocess.CalledProcessError -- ")
                return False

            print ("# {node_command}".format(node_command=cmd))
            print (result)
            return True

        else:
            debugMessage("==> Test mode configuration->testmode -- no SSH connections are made", self.debug)
            return True
