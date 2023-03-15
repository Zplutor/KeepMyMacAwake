import xbmc
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from lib import smbclient

smbclient.ClientConfig(username="SharedUser", password="shareduser")

monitor = xbmc.Monitor()
while not monitor.abortRequested(): 

    try:
        xbmc.log("[KeepMacAlive] Test connect.", xbmc.LOGDEBUG)
        smbclient.stat(r"\\192.168.50.53\Shared")
    except:
        xbmc.log("[KeepMacAlive] Test connect error.", xbmc.LOGERROR)

    if (monitor.waitForAbort(10)):
        break

xbmc.log("[KeepMacAlive] Terminating.", xbmc.LOGINFO)
smbclient.reset_connection_cache()