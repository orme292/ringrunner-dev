class CLIConfig():
    
    
    def __init__(self):
        
        self.SCRIPT_MAX_DEFAULT = 3
        self.SCRIPT_SSH_OPTIONS = "oStrictHostKeyChecking=no"
        self.SCRIPT_DEBUG = True
        
        self.ACTION_RUN = "run"
        self.ACTION_LIST = "list"
        self.ACTION_MTR = "mtr"
        self.ACTION_HIGH = "high"
        self.ACTION_PING = "ping"
        self.JOINER_FROM = "from"
        self.ACTION_MAX = "max"
        self.ACTION_SEARCH = "search"
        self.ACTION_ALL = "all"
        self.ACTION_ASN = "asn"
        self.ACTION_NODES = "nodes"
        self.ACTION_COMMAND = "command"
        self.ACTION_COUNTRIES = "countries"
        self.ACTION_DOMAIN = "domain"
        

        
# maybe split this into ringconfig for API urls and ACTION vars (so it's separate from the main config)

class RingConfig():
    
    
    def __init__(self):
        
        self.api_base = "https://api.ring.nlnog.net/1.0"
        self.api_country_codes = "/countries"
        self.api_nodes = "/nodes"
        self.api_node_by_id = "/nodes/[id]"
        self.api_nodes_if_active = "/nodes/active"
        self.api_nodes_if_active_by_country = "/nodes/active/country/[countrycode]"
        self.api_participants = "/participants"
        self.api_participant_nodes_by_id = "/participants/[id]/nodes/active"
        
        self.RING_GET_COUNTRY_CODES = "get_country_codes"
        self.RING_GET_ALL_NODES = "get_all_nodes"
        self.RING_GET_NODE_BY_ID = "get_node_by_id"
        self.RING_GET_ACTIVE_NODES = "get_active_nodes"
        self.RING_GET_ACTIVE_NODES_BY_COUNTRY = "get_active_nodes_by_country"
        self.RING_GET_PARTICIPANTS = "get_participants"
        self.RING_GET_PARTICIPANTS_NODES_BY_ID = "get_participants_nodes_by_id"