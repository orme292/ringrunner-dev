'''
style guide derived from
https://www.python.org/dev/peps/pep-0008/

4 space soft tabs (textmate)
max line length is 79 characters 
##############################################################################

imports:
    imports are done on separate lines (a single from import with multiple
                                        modules is okay though)
        i.e.
            from nlnog_api import NLNOG_API, AccessClass, ShortenString
    imports are done at the top of the file

linebreaks:
    top level functions are surrounded by two blank spaces
    functions are surrounded by one black line
        function code is separated logically by a single blank line

naming conventions:
    Class Names: CapWords
    Constants: UPPER_CASE_UNDERSCORE_SEPARATION_MEANS_READ_ONLY
    Public Functions: lower_case_underscore_separation_improves_readability()
    Variable Names: same_as_public_functions_for_readability
    Non-Public Functions: _leading_underscore()

commenting:
    class RingCall():
    # comment about the class here


        def make_it_happen(var1, var2
                           var3, var4):
            # the first code comment
    
            code_begins_here = True


Introduction to python class coding here:
http://introtopython.org/classes.html
'''


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
        
    def build_api_url(self, action, **kwargs):
        # build and return the API URL
        
        if action == 'get_country_codes':
            url = self.api_base + self.api_country_codes
        
        elif action == 'get_all_nodes':
            url = self.api_base + self.api_nodes
        
        elif action == 'get_node_by_id':
            url = self.api_base + self.api_node_by_id
            url = url.replace("[id]", kwargs['id'])
            
        elif action == 'get_active_nodes':
            url = self.api_base + self.api_nodes_if_active
            
        elif action == 'get_active_nodes_by_country':
            url = self.api_base + self.api_nodes_if_active_by_country
            url = url.replace("[countrycode]", kwargs['countrycode'])
            
        elif action == 'get_participants':
            url = self.api_base + self.api_participants

        elif action == 'get_participants_nodes_by_id':
            url = self.api_base + self.api_participant_nodes_by_id
            url = url.replace("[id]", kwargs['id'])
            
        else:
            if not url: sys.exit(1)
            
        return url