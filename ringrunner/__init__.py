#!/usr/local/bin/python3
from __future__ import print_function

import sys
import os
import argparse
import json
import subprocess
import random
import urllib

import requests
from terminaltables import SingleTable

from .ringcall import RingCall
from .runner import *

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
    
def main():
    
    SCRIPT_MAX_DEFAULT = 3
    SCRIPT_SSH_OPTIONS = "-oStrictHostKeyChecking=no"
    SCRIPT_DEBUG = True

    INITIAL = 0
    ARG_LEVEL = 0

    INITIAL_CMD_LIST = "list"
    INITIAL_CMD_RUN = "run"
    INITIAL_CMD_DOMAIN = "domain"
    INITIAL_CMD_HELP = "help"
    
    parser = argparse.ArgumentParser(description="Use the NLNOG Ring Network to nest network latency from multiple points.")
    parser.add_argument("initial", type=str, nargs="+", help="The intial IP address or initial command to pass to ringrunner.")
    parser.add_argument("--debug", action="store_true", help="Force Ringrunner into debug mode.")
    args = parser.parse_args()
    
    if validateInitial(args.initial[INITIAL]):
        api_object = RingCall()
        print(api_object.build_api_url(action='get_country_codes'))