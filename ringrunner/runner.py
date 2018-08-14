def quitMessage(erString, exitCode=2):
    print("FATAL: {erString}".format(erString=erString))
    sys.exit(exitCode)
    
def debugMessage(erString, doExit=False, exitCode=2):
    if SCRIPT_DEBUG:
        print("DEBUG:",erString)
        if doExit: sys.exit(exitCode)
                
def validateIP(ipaddress):
    octets = ipaddress.split('.')
    if len(octets) > 4 or (len(octets) < 4):
        debugMessage("initial '{ipaddress}', octets '{octets}'".format(ipaddress=ipaddress, octets=octets))
        quitMessage("Expecting IP Address -- there should be 4 octets separated by '.' i.e 8.8.8.8")
    for octet in octets:
        try:
            octet = int(octet)
        except (ValueError, TypeError):
            debugMessage("initial '{ipaddress}, octet '{octet}'".format(ipaddress=ipaddress, octet=octet))
            quitMessage("Expecting numeric IP address i.e. 8.8.8.8")
        if octet > 255:
            debugMessage("initial '{ipaddress}, octet '{octet}'".format(ipaddress=ipaddress, octet=octet))
            quitMessage(f"IP Address is out of range: .{octet}. > 255".format(octet=octet))
    return True