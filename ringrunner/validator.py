'''
This handles anything related to the NLNOG API -- including value validations, etc
'''

import sys

from .configuration import CLIConfig
from .helpers import *

class CLIValidate():


    def __init__(self):

        self.args = []
        self.debug = False
        self.config = CLIConfig()


    def validateIP(self, ipaddress):

        # ipaddress = 111.222.333.444
        octets = ipaddress.split('.') #this splits the ip address into separate parts, so octets[0] = 111 and octets[1] = 222 and octets[3] = 333 etc
        if len(octets) > 4 or (len(octets) < 4): #if there aren't 4 octets, it's not an IP, so fail
            debugMessage("initial '{ipaddress}', octets '{octets}'".format(ipaddress=ipaddress, octets=octets), self.debug)
            quitMessage("Expecting IP Address -- there should be 4 octets separated by '.' i.e 8.8.8.8")

        for octet in octets: #for each octet in the octets object do the following
            try:
                octet = int(octet) #convert it to a number -- if there is an error, we know one of the octets contains a letter or non-number
            except (ValueError, TypeError):
                debugMessage("initial '{ipaddress}, octet '{octet}'".format(ipaddress=ipaddress, octet=octet), self.debug)
                quitMessage("Expecting numeric IP address i.e. 8.8.8.8")
            if octet > 255: #
                debugMessage("initial '{ipaddress}, octet '{octet}'".format(ipaddress=ipaddress, octet=octet), self.debug)
                quitMessage("IP Address is out of range: {octet} > 255".format(octet=octet))

        return True


    def validatePrimaryRun(self):

        # > ringrunner.py run command "dig mx google.com"
        # > ringrunner.py run command "dig mx google.com" from SG
        # > ringrunner.py run command "dig mx google.com" from nodes "451, 515, 526, 216"
        # > ringrunner.py run command "dig mx google.com" from SG max 5
        # > ringrunner.py run command "dig txt apple.com" from countries

        '''
        To avoid IndexError or KeyError  I use len(self.args)
        to check for the number of args and then validate from there instead
        of using Try: Except: blocks -- The downside is
        that it sends up not being very readable and just seems cryptic.
        The code assumes that the validation will succeed / pass and only
        Fail conditions are dealt with.
        '''
        # if there is at least 1 command and it is run, then pass. Else, fail.
        if len(self.args) >= 1:
            if self.args[0] != self.config.ACTION_RUN:
                return False
        else: return False

        # if there are at least 2 commands and the second is 'command', then pass
        # Else, fail.
        if len(self.args) >= 2:
            if self.args[1] != self.config.ACTION_COMMAND:
                return False
        else: return False

        # if there aren't at least 3 commands, then fail
        # if there are just 3 commands: 'run' 'command' something then true
        if not len(self.args) >= 3:
            return False
        if len(self.args) == 3 and self.args[1] == self.config.ACTION_COMMAND:
            return True

        # if there are at least 4 commands
        # and the fourth is 'FROM' then pass
        # Else, fail.
        if len(self.args) >= 4:
            if self.args[3] != self.config.JOINER_FROM:
                return False

        # if there aren't at least 5 commands, then fail
        if not len(self.args) >= 5:
            return False

        # if there are at least 5 commands
        # and the fifth is not 'nodes' and not 'countries'
        # then it should be a country code, so fail if not 2 letters in length
        if len(self.args) >= 5:
            if self.args[4] != self.config.ACTION_NODES:
                if self.args[4] != self.config.ACTION_COUNTRIES:
                    if len(self.args[4]) != 2:
                        return False

        # if there are only 5 commands
        # and the fifth is two letters long, then pass.
        # otherwise, if the fifth command is 'countries' then pass
        # otherwise, if the fifth command is 'nodes' then fail (there should be 6)
        if len(self.args) == 5:
            print(self.args[4])
            if len(self.args[4]) == 2:
                return True
            if self.args[4] == self.config.ACTION_COUNTRIES:
                return True
            if self.args[4] == self.config.ACTION_NODES:
                return False

        # if there are only 6 commands
        # and the fifth is 'nodes', then pass
        # otherwise, if the fifth is 'max', then fail because there should be 7
        if len(self.args) == 6:
            if self.args[5] == self.config.ACTION_NODES:
                return True
            if self.args[5] == self.config.ACTION_MAX:
                return False

        # if there are 7 commands
        # and the sixth is 'max' and the seventh is a number then pass
        if len(self.args) == 7:
            if self.args[5] == self.config.ACTION_MAX:
                try: int(self.args[6])
                except ValueError: return False
                return True

        return True
