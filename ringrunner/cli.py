import sys

from terminaltables import SingleTable
from .ringcall import RingCall
from .validator import CLIValidate
from .configuration import CLIConfig
from .helpers import *

class CLIObject():


    def __init__(self):

        self.args = []
        self.showhelp = False
        self.config = CLIConfig()
        self.ring = RingCall()
        self.validate = CLIValidate()
        self.max = self.config.SCRIPT_MAX_DEFAULT


    def setDebugMode(self, value):

        self.debug = value
        self.debug = self.config.SCRIPT_DEBUG
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
        print(self.args)


    def _primaryActionList(self):

        print("primaryActionList")


    def _primaryActionRun(self):

        # > ringrunner.py run command "dig mx google.com"
        # > ringrunner.py run command "dig mx google.com" from SG
        # > ringrunner.py run command "dig mx google.com" from nodes "451, 515, 526, 216"
        # > ringrunner.py run command "dig mx google.com" from SG max 5
        # > ringrunner.py run command "dig txt apple.com" from countries
        self.validate.args = self.args
        commands_validated = self.validate.validatePrimaryRun()

        print(commands_validated)
        if not commands_validated:
            quitMessage("Invalid Command")

        if not (self.args[0] == self.config.ACTION_RUN) or not (self.args[1] == self.config.ACTION_COMMAND):
            #return_random_nodes
            quitMessage("what is it that you want?")

        if (len(self.args) == 3):
            # run command from random servers
            debugMessage("We're running commands from random servers", self.debug)
            nodes = self.ring.return_random_nodes(3)
            for node in nodes: print(node)

        if (len(self.args) == 5) and (self.args[3] == self.config.JOINER_FROM) and (self.args[4] == self.config.ACTION_COUNTRIES):
            # run command from all the countries
            debugMessage("We're running commands from 1 node in each of the countries", self.debug)

        if (len(self.args) == 5) and (len(self.args[4]) == 2):
            # run command from self.config.SCRIPT_MAX_DEFAULT nodes in country
            debugMessage("We're running commands from a specified country on 3 (Default #) nodes", self.debug)
            debugMessage("The country is {country}".format(country=self.args[4]), self.debug)
            country_is_valid = self.ring.validateCountryCode(self.args[4])
            if country_is_valid: debugMessage("The country {country} was validated with the API".format(country=self.args[4]), self.debug)
            elif not country_is_valid: debugMessage("The country {country} did not pass validation".format(country=self.args[4]), self.debug)

        if (len(self.args) == 7) and (len(self.args[4]) == 2) and (self.args[5] == self.config.ACTION_MAX):
            # run commands from specified countries from a specified number of nodes
            debugMessage("We're running commands from a specified country on a specified number of nodes", self.debug)

        if (len(self.args) == 6 and (self.args[4] == self.config.ACTION_NODES)):
            # run command from the specified nodes
            debugMessage("We're running commands from the specified nodes", self.debug)

        debugMessage("End", self.debug)
        exit()


    def _primaryActionDomain(self):

        print("primaryActionDomain")


    def _primaryActionIP(self):

        print("IP address")


    def _runCommand(self, nodes):

        print("runCommand")
