import sys, json, subprocess, requests, random, urllib

try:
    import argparse
    from terminaltables import SingleTable
    
except:
    print("Ringrunner Error: One or more of the following python packages is missing: ")
    print("argparse, terminaltables")
    sys.exit(1)
    
try:
    from .ringcall import RingCall
    import .runner

except:
    print("Ringrunner Error: A ringrunner module could not be loaded: ")
    print("ringcall, runner")
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

def main():
    parser = argparse.ArgumentParser(description="Use the NLNOG Ring Network to nest network latency from multiple points.")
    parser.add_argument("initial", type=str, nargs="+", help="The intial IP address or initial command to pass to ringrunner.")
    parser.add_argument("--debug", action="store_true", help="Force Ringrunner into debug mode.")
    args = parser.parse_args()
    
    if validateInitial(args.initial[INITIAL]):
        api_object = RingCall()
        print(api_object.build_api_url(action='get_country_codes'))
        
if __name__ == '__main__':   
