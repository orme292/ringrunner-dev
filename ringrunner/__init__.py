#!/usr/local/bin/python3
import sys
import os
import argparse
import json
import subprocess
import random
import urllib

try:
    import requests
    from terminaltables import SingleTable
except ImportError:
    print("Required modules aren't available -- requests or terminaltables")
    sys.exit(1)
    
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

from .ringcall import RingCall
from .runner import *
      
def main():
    
    INITIAL = 0
    ARG_LEVEL = 0
    
    parser = argparse.ArgumentParser(description="Use the NLNOG Ring Network to nest network latency from multiple points.")
    parser.add_argument("initial", type=str, nargs="+", help="The intial IP address or initial command to pass to ringrunner.")
    parser.add_argument("--debug", action="store_true", help="Force Ringrunner into debug mode.")
    args = parser.parse_args()
    
    print(args)