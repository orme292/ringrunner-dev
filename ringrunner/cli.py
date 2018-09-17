import sys

from .ringcall import RingCall
from .validator import CLIValidate
from .configuration import CLIConfig
from .helpers import *

class CLIObject():


    def __init__(self):

        self.args = []
        self.debug = False
        self.showhelp = False
        self.config = CLIConfig()
        self.ring = RingCall()
        self.validate = CLIValidate()
        self.max = self.config.SCRIPT_MAX_DEFAULT


    def setDebugMode(self, value):

        self.debug = value
        self.ring.debug = value
        self.validate.debug = value


    def startActionPath(self):

        self._prepArgs()

        if self.args[0] == self.config.ACTION_LIST:
            self._primaryActionList()

        elif self.args[0] == self.config.ACTION_RUN:
            self._primaryActionRun()

        elif self.args[0] == self.config.ACTION_DOMAIN:
            self._primaryActionDomain()

        else:
            if self._validateIP(self.args[0]):
                self._primaryActionIP()


    def _prepArgs(self):

        self.args = [arg.strip().lower() for arg in self.args]


    def _primaryActionList(self):

        print("primaryActionList")


    def _primaryActionRun(self):

        self.validate.args = self.args
        self.validate.validatePrimaryRun()

        try:

            if (
               self.args[1] == self.config.ACTION_COMMAND
               and self.args[3] == self.config.JOINER_FROM
            ):

                # validateCountryCode will handle errors.
                self.ring.validateCountryCode(self.args[4])

                # If a max is specified, then set the script default.
                if self.args[5] == self.config.ACTION_MAX:
                    try:
                        int(self.args[6])
                        self.max = self.args[6]
                    except (ValueError):
                        debugMessage("max value from level is {max}".format(max=self.args[6]), self.debug)
                        quitMessage("'max' must be followed by a number")

                self._runCommand([451,251,162])

        except (IndexError):
            debugMessage("IndexError. {arg}".format(arg=self.args), self.debug)
            quitMessage("Expected additional commands. Try --showhelp")

    def _primaryActionDomain(self):

        print("primaryActionDomain")


    def _primaryActionIP(self):

        print("IP address")


    def _validateIP(self, ipaddress):

        octets = ipaddress.split('.')
        if len(octets) > 4 or (len(octets) < 4):
            debugMessage("initial '{ipaddress}', octets '{octets}'".format(ipaddress=ipaddress, octets=octets), self.debug)
            quitMessage("Expecting IP Address -- there should be 4 octets separated by '.' i.e 8.8.8.8")

        for octet in octets:
            try:
                octet = int(octet)
            except (ValueError, TypeError):
                debugMessage("initial '{ipaddress}, octet '{octet}'".format(ipaddress=ipaddress, octet=octet), self.debug)
                quitMessage("Expecting numeric IP address i.e. 8.8.8.8")
            if octet > 255:
                debugMessage("initial '{ipaddress}, octet '{octet}'".format(ipaddress=ipaddress, octet=octet), self.debug)
                quitMessage("IP Address is out of range: {octet} > 255".format(octet=octet))

        return True


    def _runCommand(self, nodes):

        print("runCommand")
