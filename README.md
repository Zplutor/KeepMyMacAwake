# KeepMyMacAwake

This is a script add-on for Kodi. It simply connects a SMB server on local network and maintains the connection periodically. It's useful if:

* You run a media server (such as Emby) on a Mac.
* You want the Mac sleep when there is no activity, and wake up automatically when you launch Kodi on other Macs.

## How to Use

1. Firstly, you need to set up a SMB shared directory on the server, and turn on “Wake for network access”.
2. Clone this repository, open `script.service.keep-my-mac-awake/addon.py`, modify username, password and shared directory's address to properly values.
3. Make a zip file from the repository root directory, and install it in Kodi.
