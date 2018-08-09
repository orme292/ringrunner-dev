#!/usr/bin/env python

'''

Author: Andrew Orme
https://github.com/orme292/

An easier more intuitive way to use NLNOG Ring Network
(and hopefully much easier than ringattack.py)
https://ring.nlnog.net/

Requires 3.6 because I love f strings.
It'll just all-out fail on anything less than Pyhon 3.6 because the f strings
are syntax errors. 

'''

import sys, json, subprocess, requests, random, urllib

try:
    import argparse
    from terminaltables import SingleTable
except:
    print("Ringrunner Error: One or more of the following packages is missing: ")
    print("argparse, terminaltables")
    sys.exit(1)

SCRIPT_VERSION = "0.1"
SCRIPT_MAX_DEFAULT = 3
SCRIPT_API_BASE = "https://api.ring.nlnog.net/1.0"
SCRIPT_SSH_OPTIONS = "-oStrictHostKeyChecking=no"
SCRIPT_DEBUG = True

INITIAL = 0
ARG_LEVEL = 0

INITIAL_CMD_LIST = "list"
INITIAL_CMD_RUN = "run"
INITIAL_CMD_DOMAIN = "domain"
INITIAL_CMD_HELP = "help"

def quitMessage(erString, exitCode=2):
    print(f"FATAL: {erString}")
    sys.exit(exitCode)
    
def debugMessage(erString, doExit=False, exitCode=2):
    if SCRIPT_DEBUG:
        print("DEBUG:",erString)
        if doExit: sys.exit(exitCode)
        
def increaseLevel(byAmount=1):
    global ARG_LEVEL
    ARG_LEVEL = ARG_LEVEL + byAmount
    debugMessage(f"ARG_LEVEL changed: {ARG_LEVEL}.")
    
def decreaseLevel(byAmount=1):
    global ARG_LEVEL
    ARG_LEVEL = ARG_LEVEL - byAmount
    debugMessage(f"ARG_LEVEL changed {ARG_LEVEL}.")
        
def validateInitial(initial):
    initial = initial.strip().lower()
    while initial not in [INITIAL_CMD_LIST, INITIAL_CMD_RUN, INITIAL_CMD_DOMAIN, INTIAL_CMD_HELP]:
        debugMessage(f"initial {initial} is not checked in validateInitial({initial}), validating IP instead.")
        if validateIP(initial):
            increaseLevel()
            return True
    increaseLevel()
    return True
        
def doIt():    
    debugMessage(f"Initial level is '{ARG_LEVEL}' and the value is '{args.initial[ARG_LEVEL]}'")
    quitMessage("We're going somewhere!")
                
def validateIP(ipaddress):
    octets = ipaddress.split('.')
    if len(octets) > 4 or (len(octets) < 4):
        debugMessage(f"initial '{ipaddress}', octets '{octets}'")
        quitMessage("Expecting IP Address -- there should be 4 octets separated by '.' i.e 8.8.8.8")
    for octet in octets:
        try:
            octet = int(octet)
        except (ValueError, TypeError):
            debugMessage(f"initial '{ipaddress}, octet '{octet}'")
            quitMessage("Expecting numeric IP address i.e. 8.8.8.8")
        if octet > 255:
            debugMessage(f"initial '{ipaddress}, octet '{octet}'")
            quitMessage(f"IP Address is out of range: .{octet}. > 255")
    return True
    
            
def helpWith(initial):
    print("helpwith")
  
if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description="Use the NLNOG Ring Network to nest network latency from multiple points.")
    parser.add_argument("initial", type=str, nargs="+", help="The intial IP address or initial command to pass to ringrunner.")
    parser.add_argument("--debug", action="store_true", help="Force Ringrunner into debug mode.")
    args = parser.parse_args()
    
    if validateInitial(args.initial[INITIAL]): doIt()