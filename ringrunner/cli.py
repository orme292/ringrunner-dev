import sys

from terminaltables import SingleTable
from colorclass import Color, Windows

from .ringcall import RingCall
from .validator import CLIValidate
from .configuration import CLIConfig
from .shellexec import ShellEX
from .helpers import *



class CLIObject():


    def __init__(self):

        self.args = []
        self.showhelp = False
        self.config = CLIConfig()
        self.ring = RingCall()
        self.validate = CLIValidate()
        self.shell = ShellEX()
        self.max = self.config.SCRIPT_MAX_DEFAULT


    def setDebugMode(self, value):

        if value != self.config.SCRIPT_DEBUG:
            self.debug = self.config.SCRIPT_DEBUG
            self.ring.debug = self.config.SCRIPT_DEBUG
            self.validate.debug = self.config.SCRIPT_DEBUG
            self.shell.debug = self.config.SCRIPT_DEBUG

        else:
            self.debug = value
            self.ring.debug = value
            self.validate.debug = value
            self.shell.debug = value


    def startActionPath(self):

        self._prepArgs()

        if self.args[0] == self.config.ACTION_LIST:
            self._primaryActionList()

        elif self.args[0] == self.config.ACTION_RUN:
            self._primaryActionRun()

        elif self.args[0] == self.config.ACTION_DOMAIN:
            self._primaryActionDomain()

        else:
            if self.validate.validateIP(self.args[0]):
                self._primaryActionIP()


    def _prepArgs(self):

        self.args = [arg.strip().lower() for arg in self.args]
        debugMessage(self.args, self.debug)


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

        if not commands_validated:
            quitMessage("Invalid Command.")

        # argument length = 3
        # 1st argument: run
        # 2nd argument: command
        # 3rd argument: is assumed to be a command in quotes
        if (len(self.args) == 3) and (self.args[0] == self.config.ACTION_RUN) and (self.args[1] == self.config.ACTION_COMMAND):
            # run command from random servers
            debugMessage("We're running a command on random nodes", self.debug)
            nodes, json = self.ring.return_random_nodes(self.config.SCRIPT_MAX_DEFAULT)

            for node in nodes:
                node_host, json = self.ring.get_node_by_id(id=str(node), field="hostname")
                node_particpant, json = self.ring.get_node_by_id(id=str(node), field="participant", json=json)
                debugMessage("Hostdata: " + str(node_host) + " " + str(node_particpant), self.debug)
                debugMessage("JSON: " + str(json), self.debug)

                for struct in json['results']['nodes']:
                    table_data_city = str(struct['city'])
                    table_data_countrycode = str(struct['countrycode'])
                    table_data_datacenter = str(struct['datacenter'])
                    table_data_asn = str(struct['asn'])
                    table_data_id = str(struct['id'])
                    table_data_ipv4 = str(struct['ipv4'])
                    table_data_ipv6 = str(struct['ipv6'])

                Windows.enable(auto_colors=True, reset_atexit=True)
                table_data = [
                    [Color('{autogreen}'+str(node_host)+'{/autogreen}'), table_data_datacenter + " (ASN: " + table_data_asn + ")" ],
                    [table_data_city + ", " + table_data_countrycode, table_data_ipv4 + " / " + table_data_ipv6]
                ]
                table_instance = SingleTable(table_data, "Node " + table_data_id)
                print(table_instance.table)

                self.shell.run_command(self.args[2], node_host)

        if (len(self.args) == 5) and (self.args[3] == self.config.JOINER_FROM) and (self.args[4] == self.config.ACTION_COUNTRIES):
            # run command from all the countries
            debugMessage("We're running commands from 1 node in each of the countries with active nodes", self.debug)

        if (len(self.args) == 5) and (len(self.args[4]) == 2):
            # run command from self.config.SCRIPT_MAX_DEFAULT nodes in country
            debugMessage("We're running commands from a specific country on 3 (or the default # of) nodes", self.debug)
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
