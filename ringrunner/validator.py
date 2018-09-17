import sys

from .configuration import CLIConfig

class CLIValidate():


    def __init__(self):

        self.args = []
        self.debug = False
        self.config = CLIConfig

    def _fatal(self, msg):

        print(msg)
        sys.exit(1)


    def validatePrimaryRun(self):

        # > ringrunner.py run command "dig mx google.com" from SG
        # > ringrunner.py run command "dig mx google.com" from nodes "451, 515, 526, 216"
        # > ringrunner.py run command "dig mx google.com" from SG max 5
        # > ringrunner.py run command "dig txt apple.com" from countries
        if self.args[0] != self.config.ACTION_RUN:
            return False
        if self.args[1]:
            if self.args[1] != self.config.ACTION_COMMAND:
                return False
        else:
            return False

        if not self.args[2]:
            return False

        if not self.args[3]:
            return False
        if self.args[3] != self.config.JOINER_FROM:
            return False

        if not self.args[4]:
            return False
        if self.args[4] != self.config.ACTION_NODES:
            if self.args[4] != self.config.ACTION_COUNTRIES:
                if len(self.args[4]) != 2:
                    return False

        if self.args[4] == self.config.ACTION_NODES:
            if not self.args[5]:
                return False

        return True
