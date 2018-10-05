import urllib
import random
import requests
import json

from .configuration import RingConfig
from .configuration import CLIConfig
from .helpers import *

class RingCall():


    def __init__(self):

        self.config = RingConfig()
        self.cliconfig = CLIConfig()
        self.debug = False
        self.debug_query_count = False
        self.query_count = 0


    def build_api_url(self, action, **kwargs):
        # build and return the API URL

        if action == self.config.RING_GET_COUNTRY_CODES:
            url = self.config.api_base + self.config.api_country_codes

        elif action == self.config.RING_GET_ALL_NODES:
            url = self.config.api_base + self.config.api_nodes

        elif action == self.config.RING_GET_NODE_BY_ID:
            url = self.config.api_base + self.config.api_node_by_id
            url = url.replace("[id]", kwargs['id'])

        elif action == self.config.RING_GET_ACTIVE_NODES:
            url = self.config.api_base + self.config.api_nodes_if_active

        elif action == self.config.RING_GET_ACTIVE_NODES_BY_COUNTRY:
            url = self.config.api_base + self.config.api_nodes_if_active_by_country
            url = url.replace("[countrycode]", kwargs['countrycode'])

        elif action == self.config.RING_GET_PARTICIPANTS:
            url = self.config.api_base + self.api_participants

        elif action == self.config.RING_GET_PARTICIPANTS_NODES_BY_ID:
            url = self.config.api_base + self.config.api_participant_nodes_by_id
            url = url.replace("[id]", kwargs['id'])

        else:
            if not url:
                debugMessage("Could not determine API call for {action}".format(action=action), self.debug)
                quitMessage("Couldn't generate API call.")

        return url


    def do_api_call(self, url, **kwargs):

        try:
            response = urllib.request.urlopen(url=url)
            json_struct = json.loads(response.read().decode())

        except (urllib.error.HTTPError, urllib.error.URLError, ValueError):
            print ("do_api_call: Error getting data from the API URL.", url)
            sys.exit(1)

        self.query_count += 1
        debugMessage("Total number of API queries: {num_of_queries}".format(num_of_queries=self.query_count), self.debug_query_count)

        return json_struct


    def _get_all_active_nodes(self, **kwargs):

        field = kwargs.get('field')

        if not field:
            api_url = self.build_api_url(self.config.RING_GET_ALL_NODES)
            data = self.do_api_call(api_url)
            return data

        if field:
            api_url = self.build_api_url(self.config.RING_GET_ACTIVE_NODES)
            data = self.do_api_call(api_url)
            data_by_field = []
            for node in data['results']['nodes']:
                data_by_field.append(node[field])

            return data_by_field, data


    def get_node_by_id(self, **kwargs):

        id = kwargs.get('id')
        field = kwargs.get('field')
        json = kwargs.get('json')

        debugMessage("{id} {field} json?{jsonyes}".format(id=id, field=field, jsonyes=type(json)), self.debug)

        if not id:
            return False, None

        if id and not field:
            api_url = self.build_api_url(self.config.RING_GET_NODE_BY_ID,id=id)
            data = self.do_api_call(api_url)
            return data

        if id and field:
            if not json:
                api_url = self.build_api_url(self.config.RING_GET_NODE_BY_ID,id=id)
                data = self.do_api_call(api_url)
            else: data = json
            if (data['info']['resultcount'] == 1) and (data['info']['success'] == 1):
                for struct in data['results']['nodes']:
                    field_data = struct[field]
                    return field_data, data
            else: return False, None


    def return_node_per_country(self, **kwargs):

        api_url = self.build_api_url(self.config.RING_GET_COUNTRY_CODES)
        data = self.do_api_call(api_url)

        data_countries = []
        if (data['info']['success'] == 1):
            for country in data['results']['countrycodes']:
                data_countries.append(country)
        else:
            return False, []

        chosen_nodes = []

        print("We're gathering a list of nodes available in each country...")

        for country in data_countries:
            api_url = self.build_api_url(self.config.RING_GET_ACTIVE_NODES_BY_COUNTRY, countrycode=country)
            country_data = self.do_api_call(api_url)

            country_nodes = country_data['results']['nodes']
            if len(country_nodes) != 0 and len(country_nodes) == 1:
                for node in country_data['results']['nodes']:
                    chosen_nodes.append(node['id'])
            elif len(country_nodes) != 0:
                country_node_list = []
                for node in country_data['results']['nodes']:
                    country_node_list.append(node['id'])
                item = random.randint(0, (len(country_node_list)-1))
                chosen_nodes.append(item)

        return chosen_nodes

    def return_random_nodes(self, num=-1, **kwargs):
        # hit the api and ask for random servers. kwargs[country] will be the country code
        if num == -1:
            num = self.cliconfig.SCRIPT_MAX_DEFAULT

        all_nodes, json = self._get_all_active_nodes(field='id')
        chosen_nodes = []

        for count in range(num):
            item = random.randint(0, (len(all_nodes)-1))
            chosen_nodes.append(all_nodes[item])

        while len(set(chosen_nodes)) != num:
            item = random.randint(0, (len(all_nodes)-1))
            chosen_nodes.append(all_nodes[item])

        return set(chosen_nodes), json


    def return_node_data(self, node_id, active_only=True):
        # return data only if True
        print("return_node_data")


    def validateCountryCode(self, code):

        code = code.upper()

        if len(code) != 2:
            quitMessage("Country Code should be two letters. See {api}{country}".format(api=self.config.api_base, country=self.config.api_country_codes))

        api_url = self.build_api_url(self.config.RING_GET_COUNTRY_CODES)
        data = self.do_api_call(api_url)

        for country in data['results']['countrycodes']:
            if country == code:
                return True

        print("{code} is not a valid country code. See: {url}".format(code=code, url=self.build_api_url(self.config.RING_GET_COUNTRY_CODES)))
        sys.exit(1)
