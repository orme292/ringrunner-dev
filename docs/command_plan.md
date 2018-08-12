## Ringrunner Plan

This is a list of commands that the project will be based around

This will run an MTR (10 packets) from 3 random nodes
> ringrunner.py 1.2.3.4 run mtr

This will run a high count ping (100 packets) from 3 random nodes
> ringrunner.py 1.2.3.4 run high ping

This will run an MTR (10 packets) from 4 random nodes in the US
> ringrunner.py 1.2.3.4 run mtr from US max 4

This will run a high count MTR (100 packets) from 3 random nodes in the US
> ringrunner.py 1.2.3.4 run high mtr from JP

This will run pings (10 packets) from 3 random nodes with "linode" in their any of their fields
> ringrunner.py 1.2.3.4 run ping from search linode max 3

This will run an MTR (10 packets) from every node with "equinix" in any of their fields
> ringrunner.py 1.2.3.4 run mtr from search equinix
> ringrunner.py 1.2.3.4 run mtr from search equinix max all

This will run an MTR (10 packets) from every node with the ASN 2679
> ringrunner.py 1.2.3.4 run mtr from ASN 2679

This will run an MTR (100 packets) from nodes with the IDs 451, 161, 005, 231, and 16
> ringrunner.py 1.2.3.4 run high mtr from nodes "451, 161, 005, 231, 16"

This will list all active nodes
> ringrunner.py list
> ringrunner.py list all

This will list all active nodes in the US
> ringrunner.py list US

This will list all active nodes in GB with 'equinix' in any field
> ringrunner.py list GB search equinix

This will list all active nodes with the ASN 2679
> ringrunner.py list ASN 2679

This will list all active nodes with 'equinix' in any field
> ringrunner.py list search equinix
> ringrunner.py list search equinix

This will run the command "dig mx google.com" on 3 random nodes from SG
> ringrunner.py run command "dig mx google.com" from SG

This will run the command "dig txt apple.com" from a node on each country
> ringrunner.py run command "dig txt apple.com" from countries

This will run an MTR to 'arstechnica.com' from 3 random nodes in CA
> ringrunner.py domain arstechnica.com run mtr from CA

This will run an MTR to 'google.com' from nodes with the IDs 451, 515, 526, and 216
> ringrunner.py domain google.com run ping from nodes "451, 515, 526, 216"