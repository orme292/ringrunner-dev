# ringrunner

This will eventually be a more intuitive version of ringattack

- [x] Add TerminalTables support / Colorclass support
- [x] Break elements out into seperate classes (display, commands, API, ssh, validation, etc)
- [ ] Add hack to to search 'GB' and 'UK' when either country code is provided
- [ ] Make table display prettier with more information
- [ ] Turn country code into a country name for non --quiet displays
- [ ] Add command line option for API query debug --qcount (?)

Get the following commands to work:

- [x] python3 -m ringattack run command "dig mx google.com +short"
- [x] python3 -m ringattack run command "dig mx google.com +short" from SG
- [x] python3 -m ringattack run command "dig mx google.com +short" from SG max 5
- [x] python3 -m ringattack run command "dig mx google.com +short" from nodes "451, 515, 526, 216"
- [x] python3 -m ringattack run command "dig txt apple.com +short" from countries
- [ ] python3 -m ringattack run command "dig txt linode.com +short" search "equinix"
- [ ] python3 -m ringattack run command "dig txt linode.com +short" search "liquidweb" from SG
- [ ] python3 -m ringattack list
- [ ] python3 -m ringattack list all
- [ ] python3 -m ringattack list all active
- [ ] python3 -m ringattack list all inactive
- [ ] python3 -m ringattack list countries
- [ ] python3 -m ringattack list CA
- [ ] python3 -m ringattack list GB search "equinix"
- [ ] python3 -m ringattack list all search "equinix"
- [ ] python3 -m ringattack list ASN 2679
- [ ] python3 -m ringattack 1.2.3.4 run ping/mtr
- [ ] python3 -m ringattack 1.2.3.4 run high ping/mtr
- [ ] python3 -m ringattack 1.2.3.4 run high ping/mtr from EE
- [ ] python3 -m ringattack 1.2.3.4 run ping/mtr from CA max 4
- [ ] python3 -m ringattack 1.2.3.4 run high ping/mtr from JP max 4
- [ ] python3 -m ringattack 1.2.3.4 run ping/mtr from nodes "451, 161, 005, 231, 16"
- [ ] python3 -m ringattack 1.2.3.4 run high ping/mtr from ASN 2679
- [ ] python3 -m ringattack 1.2.3.4 run ping/mtr search "amazon"
- [ ] python3 -m ringattack 1.2.3.4 run ping/mtr search "amazon" from CN
- [ ] python3 -m ringattack 1.2.3.4 run ping/mtr from countries
- [ ] python3 -m ringattack domain "arstechnica.com" run mtr from CA
- [ ] python3 -m ringattack domain "google.com" run high ping from nodes "451, 515, 526, 216"
- [ ] python3 -m ringattack domain "linode.com" run mtr from CA max 5
- [ ] python3 -m ringattack domain "reuters.com" run ping from countries
- [ ] python3 -m ringattack domain "apple.com" run mtr from search "linode"
- [ ] python3 -m ringattack domain "apple.com" run mtr from search "linode" from GB
