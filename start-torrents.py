#!/usr/bin/env python2.7
# This script starts all paused and unfinished (progress != 100%) in deluge
from deluge_client import DelugeRPCClient
from sys import exit

# Setting variables
HOST = "cid.local"
PORT = 58846
USER = "deluge"
PASS = "password"

# Setup the client
client = DelugeRPCClient(HOST, PORT, USER, PASS)


def main():
    client.connect()
    if not client.connected:
        print("Connection Error!")
        exit(1)

    torrents = client.call('core.get_torrents_status', {}, [])

    for torrent in torrents:
        if not torrents[torrent]["is_finished"]:
            client.call('core.resume_torrent', [torrent])


if __name__ == "__main__":
    main()
