import sys


def quitMessage(erString, exitCode=2):
    print("FATAL: {erString}".format(erString=erString))
    sys.exit(exitCode)


def debugMessage(erString, debugValue, doExit=False, exitCode=2):
    if debugValue: print("DEBUG:",erString)
    if doExit: sys.exit(exitCode)


def displayMessage(msgString):

    print(" " + str(msgString))
    return True
