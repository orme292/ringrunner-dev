import sys

from .configuration import CLIConfig
from .configuration import RingConfig
from .display import CLIDisplay
from .helpers import *
from .ringcall import RingCall
from .shellexec import ShellEX
from .validator import CLIValidate


class CLIObject():


    def __init__(self):

        self.config = CLIConfig()
        self.display = CLIDisplay()
        self.ring = RingCall()
        self.shell = ShellEX()
        self.validate = CLIValidate()
        self.args = []
        self.max = self.config.SCRIPT_MAX_DEFAULT
        self.quiet = self.config.SCRIPT_QUIET
        self.showhelp = False


    def setQuietMode(self, value):
        if (value != self.config.SCRIPT_QUIET):
            self.display.quiet = value


    def setDebugMode(self, value):

        if value != self.config.SCRIPT_DEBUG:
            self.debug = value
            self.display.debug = value
            self.ring.debug = value
            self.shell.debug = value
            self.validate.debug = value

        else:
            self.debug = self.config.SCRIPT_DEBUG
            self.display.debug = self.config.SCRIPT_DEBUG
            self.ring.debug = self.config.SCRIPT_DEBUG
            self.shell.debug = self.config.SCRIPT_DEBUG
            self.validate.debug = self.config.SCRIPT_DEBUG


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

                debugMessage("Hostdata: " + str(node_host), self.debug)
                debugMessage("JSON: " + str(json), self.debug)

                table = self.display.print_node_id_table(json=json)

                self.shell.run_command(self.args[2], node_host)

        # arguement length = 5
        # 1st and 2nd arguments are 'run' and 'command'
        # 4th argument is 'from' and 5th is 'countries'
        if ((len(self.args) == 5) and (self.args[3] == self.config.JOINER_FROM) and (self.args[4] == self.config.ACTION_COUNTRIES) and
           (self.args[0] == self.config.ACTION_RUN) and (self.args[1] == self.config.ACTION_COMMAND)):
            # run command from all the countries
            debugMessage("We're running commands from 1 node in each of the countries with active nodes", self.debug)

            country_nodes = self.ring.return_node_per_country()

            debugMessage("Total Nodes: " + str(len(set(country_nodes))), self.debug)

            print(country_nodes)
            for node in country_nodes:
                node_host, json = self.ring.get_node_by_id(id=str(node), field="hostname")
                table = self.display.print_node_id_table(json=json)
                self.shell.run_command(self.args[2], node_host)

        # argument length = 5
        # and the length of the 5th argument is 2
        if ((len(self.args) == 5) and (len(self.args[4]) == 2) and (self.args[3] == self.config.JOINER_FROM) and
           (self.args[0] == self.config.ACTION_RUN) and (self.args[1] == self.config.ACTION_COMMAND)):
            # run command from self.config.SCRIPT_MAX_DEFAULT nodes in country
            debugMessage("We're running commands from a specific country on 3 (or the default # of) nodes", self.debug)

            country_is_valid = self.ring.validateCountryCode(self.args[4])
            if not country_is_valid:
                quitMessage("Invalid country code {code} or there are no active Ring Nodes.".format(code=self.args[4]))

            nodes_in_a_country, json = self.ring.return_nodes_from_a_country(countrycode=self.args[4])

            for node in nodes_in_a_country:
                node_host, json = self.ring.get_node_by_id(id=(str(node)), field="hostname")

                table = self.display.print_node_id_table(json=json)

                self.shell.run_command(self.args[2], node_host)

        # $ run command "dig mx google.com +short" from SG max 5
        # argument length = 7
        # the first and second arguments are 'run command'
        # the fourth argument is 'from'
        # the length of the fifth argument is 2
        # the sixth argument is 'max'
        # the seventh argument will be the number
        if ((len(self.args) == 7) and (len(self.args[4]) == 2) and (self.args[5] == self.config.ACTION_MAX) and
           (self.args[3] == self.config.JOINER_FROM) and (self.args[0] == self.config.ACTION_RUN) and
           (self.args[1] == self.config.ACTION_COMMAND)):
            # run commands from specified countries from a specified number of nodes
            debugMessage("We're running commands from a specified country on a specified number of nodes", self.debug)

            try:
                num_nodes = int(self.args[6])
            except ValueError: quitMessage("'max' should be followed by a number.")

            nodes_in_a_country, json = self.ring.return_nodes_from_a_country(countrycode=self.args[4], num_nodes=num_nodes)

            for node in nodes_in_a_country:
                node_host, json = self.ring.get_node_by_id(id=(str(node)), field="hostname")

                table = self.display.print_node_id_table(json=json)

                self.shell.run_command(self.args[2], node_host)

        # $ run command "dig mx google.com +short" from nodes "num, num, num"
        # argument length = 6
        # if the fourth argument is 'from'
        # and the fifth argument is 'nodes'
        # and the first and second are 'run command'
        if ((len(self.args) == 6) and (self.args[3] == self.config.JOINER_FROM) and
        (self.args[4] == self.config.ACTION_NODES) and (self.args[0] == self.config.ACTION_RUN) and
        (self.args[1] == self.config.ACTION_COMMAND)):
            # run command from the specified nodes
            debugMessage("We're running commands from the specified nodes", self.debug)

            provided_nodes = self.args[5]
            nodes = []
            ws_nodes = provided_nodes.split(',')
            for node in ws_nodes:
                nodes.append(node.strip())


        debugMessage("End", self.debug)
        exit()


    def _primaryActionDomain(self):

        print("primaryActionDomain")


    def _primaryActionIP(self):

        print("IP address")
