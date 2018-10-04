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
    from colorclass import Color, Windows
except ImportError:
    print("Required modules aren't available -- colorclass, requests, terminaltables")
    print("Try installing them with `pip3 install requests` and `pip3 install terminaltables`")
    sys.exit(1)

'''

Author: Andrew Orme
https://github.com/orme292/

An easier more intuitive way to use NLNOG Ring Network
(and hopefully much easier than ringattack.py)
https://ring.nlnog.net/

'''

from .cli import CLIObject

def main():

    parser = argparse.ArgumentParser(description="Use the NLNOG Ring Network to nest network latency from multiple points.")
    parser.add_argument("commands", type=str, nargs="+", help="The intial IP address or initial command to pass to ringrunner.")
    parser.add_argument("--debug", action="store_true", help="Force Ringrunner into debug mode.")
    parser.add_argument("--json", action="store_true", help="Display results as raw JSON data when possible. No formatting when possible.")
    parser.add_argument("--showhelp", action="store_true", help="Tell me what Ringrunner can do and how to do it.")
    args = parser.parse_args()

    cli = CLIObject()
    cli.showhelp = args.showhelp
    cli.setDebugMode(args.debug)
    cli.args = args.commands
    cli.startActionPath()
