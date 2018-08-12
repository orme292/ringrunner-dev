import sys, json, subprocess, requests, random, urllib

try:
    import argparse
    from terminaltables import SingleTable
    
except:
    print("Ringrunner Error: One or more of the following packages is missing: ")
    print("argparse, terminaltables")
    sys.exit(1)
    
try:
    import ringcall

except:
    print("Ringrunner Error: A submodule couldn't be loaded:")
    print("ringcall")
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