from terminaltables import SingleTable
from textwrap import wrap
from colorclass import Color, Windows

from .configuration import CLIConfig
from .configuration import RingConfig
from .helpers import *
from .ringcall import RingCall


class CLIDisplay():


    def __init__(self):

        self.debug = False
        self.quiet = False
        self.config = CLIConfig()
        self.ring = RingCall()
        self.ringconfig = RingConfig()


    def print_node_id_table(self, json, **kwargs):

        for struct in json['results']['nodes']:
            table_data_host = str(struct['hostname'])
            table_data_city = str(struct['city'])
            table_data_countrycode = str(struct['countrycode'])
            table_data_datacenter = str(struct['datacenter'])
            table_data_asn = str(struct['asn'])
            table_data_id = str(struct['id'])
            table_data_ipv4 = str(struct['ipv4'])
            table_data_ipv6 = str(struct['ipv6'])

        if not self.quiet:
            table_data_url = self.ring.build_api_url(self.ringconfig.RING_GET_NODE_BY_ID, id=table_data_id)

            Windows.enable(auto_colors=True, reset_atexit=True)
            table_data = [
                [Color('{autogreen}'+str(table_data_host)+'{/autogreen}'),'', table_data_city + ", " + table_data_countrycode],
                [table_data_ipv4, table_data_ipv6, Color('{autoblue}'+table_data_url+'{/autoblue}')]
            ]
            table_instance = SingleTable(table_data, "Node " + table_data_id)
            column_max_width = table_instance.column_max_width(1)
            table_dc_location = table_data_datacenter + " (ASN: " + table_data_asn + ")"
            table_dc_location = '\n'.join(wrap(table_dc_location, column_max_width))
            table_instance.table_data[0][1] = table_dc_location

            print(table_instance.table)

        if self.quiet:
            line_title = Color('{green}' + table_data_host + '{/green}')
            api_url = self.ring.build_api_url(self.ringconfig.RING_GET_NODE_BY_ID, id=table_data_id)
            api_url = Color('{blue}'+api_url+'{/blue}')
            print(" ### Node: " + line_title + " ASN " + table_data_asn + " " + table_data_city + " " + table_data_countrycode + " @ " + api_url)
