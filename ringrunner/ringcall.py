import urllib
import requests
import json

from .configuration import Config
from .helpers import *

class RingCall():
    
    
    def __init__(self):
        
        self.api_base = "https://api.ring.nlnog.net/1.0"
        self.api_country_codes = "/countries"
        self.api_nodes = "/nodes"
        self.api_node_by_id = "/nodes/[id]"
        self.api_nodes_if_active = "/nodes/active"
        self.api_nodes_if_active_by_country = "/nodes/active/country/[countrycode]"
        self.api_participants = "/participants"
        self.api_participant_nodes_by_id = "/participants/[id]/nodes/active"
        self.config = Config()
        self.debug = False
        
        
    def build_api_url(self, action, **kwargs):
        # build and return the API URL
        
        if action == self.config.RING_GET_COUNTRY_CODES:
            url = self.api_base + self.api_country_codes
        
        elif action == self.config.RING_GET_ALL_NODES:
            url = self.api_base + self.api_nodes
        
        elif action == self.config.RING_GET_NODE_BY_ID:
            url = self.api_base + self.api_node_by_id
            url = url.replace("[id]", kwargs['id'])
            
        elif action == self.config.RING_GET_ACTIVE_NODES:
            url = self.api_base + self.api_nodes_if_active
            
        elif action == self.config.RING_GET_ACTIVE_NODES_BY_COUNTRY:
            url = self.api_base + self.api_nodes_if_active_by_country
            url = url.replace("[countrycode]", kwargs['countrycode'])
            
        elif action == self.config.RING_GET_PARTICIPANTS:
            url = self.api_base + self.api_participants

        elif action == self.config.RING_GET_PARTICIPANTS_NODES_BY_ID:
            url = self.api_base + self.api_participant_nodes_by_id
            url = url.replace("[id]", kwargs['id'])
            
        else:
            if not url: sys.exit(1)
            
        return url
        
        
    def do_api_call(self, url, **kwargs):
        
        try:
            response = urllib.request.urlopen(url=url)
            json_struct = json.loads(response.read().decode())
            
        except (urllib.error.HTTPError, urllib.error.URLError, ValueError):
            print ("do_api_call: Error getting data from the API URL.", url)
            sys.exit(1)
            
        return json_struct
        
    
    def validateCountryCode(self, code):
        
        code = code.upper()
        
        if len(code) != 2:
            quitMessage("Country Code should be at least two letters. See {api}{country}".format(api=self.api_base, country=self.api_country_codes))
            
        api_url = self.build_api_url(self.config.RING_GET_COUNTRY_CODES)
        data = self.do_api_call(api_url)
        
        for country in data['results']['countrycodes']:
            if country == code: 
                return True
        
        return False