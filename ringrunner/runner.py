def quitMessage(erString, exitCode=2):
    print(f"FATAL: {erString}")
    sys.exit(exitCode)
    
def debugMessage(erString, doExit=False, exitCode=2):
    if SCRIPT_DEBUG:
        print("DEBUG:",erString)
        if doExit: sys.exit(exitCode)
        
def increaseLevel(byAmount=1):
    global ARG_LEVEL
    ARG_LEVEL = ARG_LEVEL + byAmount
    debugMessage(f"ARG_LEVEL changed: {ARG_LEVEL}.")
    
def decreaseLevel(byAmount=1):
    global ARG_LEVEL
    ARG_LEVEL = ARG_LEVEL - byAmount
    debugMessage(f"ARG_LEVEL changed {ARG_LEVEL}.")
        
def validateInitial(initial):
    initial = initial.strip().lower()
    while initial not in [INITIAL_CMD_LIST, INITIAL_CMD_RUN, INITIAL_CMD_DOMAIN, INITIAL_CMD_HELP]:
        debugMessage(f"initial {initial} is not checked in validateInitial({initial}), validating IP instead.")
        if validateIP(initial):
            increaseLevel()
            return True
    increaseLevel()
    return True
        
def doIt():    
    debugMessage(f"Initial level is '{ARG_LEVEL}' and the value is '{args.initial[ARG_LEVEL]}'")
    quitMessage("We're going somewhere!")
                
def validateIP(ipaddress):
    octets = ipaddress.split('.')
    if len(octets) > 4 or (len(octets) < 4):
        debugMessage(f"initial '{ipaddress}', octets '{octets}'")
        quitMessage("Expecting IP Address -- there should be 4 octets separated by '.' i.e 8.8.8.8")
    for octet in octets:
        try:
            octet = int(octet)
        except (ValueError, TypeError):
            debugMessage(f"initial '{ipaddress}, octet '{octet}'")
            quitMessage("Expecting numeric IP address i.e. 8.8.8.8")
        if octet > 255:
            debugMessage(f"initial '{ipaddress}, octet '{octet}'")
            quitMessage(f"IP Address is out of range: .{octet}. > 255")
    return True
    
            
def helpWith(initial):
    print("helpwith")