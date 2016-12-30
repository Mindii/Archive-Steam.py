import os, sys

## Steam Settings
SteamDir = 'C:\Program Files (x86)\Steam\Steam.exe'

## Control steam ##
def SteamCMD(CMD='False'):
    if CMD == 'False':
        return 'No command given'
        sys.exit(1)
    elif CMD == 'away':
        SteamCmd = 'friends/status/away'
    elif CMD == 'busy':
        SteamCmd = 'friends/status/busy'
    elif CMD == 'offline':
        SteamCmd = 'friends/status/offline'
    elif CMD == 'online':
        SteamCmd = 'friends/status/online'
    elif CMD == 'add':
        SteamCmd = 'open/activateproduct'
    else:
        return 'no valid command, look commands over here: https://developer.valvesoftware.com/wiki/Steam_browser_protocol'
        sys.exit(1)
    SteamRun = '"%s" steam://%s' %(SteamDir, SteamCmd)
    os.popen(SteamRun)
		
print(SteamCMD(sys.argv[1]))