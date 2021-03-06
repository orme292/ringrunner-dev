#!/usr/local/bin/python3
import argparse
import json
import os
import random
import subprocess
import sys
import urllib

try:
    from colorclass import Color, Windows
    import requests
    from terminaltables import SingleTable

except ImportError:
    print("Required modules aren't available -- colorclass, requests, terminaltables")
    print("Try installing them with `pip3 install requests` and `pip3 install terminaltables`")
    sys.exit(1)

'''

Author: Andrew Orme
https://github.com/orme292/

An easier more intuitive way to use NLNOG Ring Network
https://ring.nlnog.net/

'''

from .cli import CLIObject

def main():

    print('\n RingRunner \n https://ring.nlnog.net/ \n\n')

    parser = argparse.ArgumentParser(description="Use the NLNOG Ring Network to nest network latency from multiple points.")
    parser.add_argument("commands", type=str, nargs="+", help="The intial IP address or initial command to pass to ringrunner.")
    parser.add_argument("--debug", action="store_true", help="Force Ringrunner into debug mode.")
    parser.add_argument("--json", action="store_true", help="Display results as raw JSON data when possible. No formatting when possible.")
    parser.add_argument("--quiet", action="store_true", help="Do not display tables with node data.")
    parser.add_argument("--showhelp", action="store_true", help="Tell me what Ringrunner can do and how to do it.")
    args = parser.parse_args()

    try:
        cli = CLIObject()
        cli.showhelp = args.showhelp
        cli.setDebugMode(args.debug)
        cli.setQuietMode(args.quiet)
        cli.args = args.commands
        cli.startActionPath()

    except KeyboardInterrupt:
        sys.exit(1)
