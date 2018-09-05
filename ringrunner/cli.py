import sys

from .ringcall import RingCall
from .configuration import CLIConfig
from .helpers import *

class CLIObject():
    
    
    def __init__(self):
        
        self.level = 0
        self.args = []
        self.debug = False
        self.showhelp = False
        self.config = CLIConfig()
        self.ring = RingCall()
        
    
    def setDebugMode(self, value):
        
        self.debug = value
        self.ring.debug = value
        
        
    def startActionPath(self):
        
        self._prepArgs()
        if self.level == 0:
            
            if self.args[self.level] == self.config.ACTION_LIST: 
                self._primaryActionList()
                
            elif self.args[self.level] == self.config.ACTION_RUN: 
                self._primaryActionRun()
                
            elif self.args[self.level] == self.config.ACTION_DOMAIN: 
                self._primaryActionDomain()
                
            else: 
                if self._validateIP(self.args[self.level]): 
                    self._primaryActionIP()
                    
    
    def _prepArgs(self):
        
        self.args = [arg.strip().lower() for arg in self.args]
        
                   
    def _primaryActionList(self):
        
        print("primaryActionList")
        
        
    def _primaryActionRun(self):
        
        self.level =+ 1
        
        # 0   1      2              3    4
        # run comand "command here" from CC
        #     level
        if (
           self.args[self.level] == self.config.ACTION_COMMAND 
           and self.args[self.level+2] == self.config.JOINER_FROM 
        ):
            if not self.ring.validateCountryCode(self.args[self.level+3]):
                debugMessage("code provided {cc}".format(cc=(self.level+3)))
                quitMessage("There are no active/inactive nodes in that country or the country is invalid.")
            
            self._runCommand()     
    
    def _primaryActionDomain(self):
        
        self.level += 1
        print("primaryActionDomain")
        
    
    def _primaryActionIP(self):
        
        self.level += 1
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
        
    def _runCommands(self, nodes):
        
        