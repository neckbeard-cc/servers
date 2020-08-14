#!/usr/bin/env python

import json

SERVERS_IN = "servers.txt"
SERVERS_OUT = "servers.json"

file_in = open(SERVERS_IN, "r")
raw = file_in.read().splitlines()
file_in.close()

servers = []
for address in raw:
    servers.append({"name": address, "ip": address, "type": "PC"})

json_data = json.dumps(servers, indent=2)

file_out = open(SERVERS_OUT, "w")
file_out.write(json_data)
file_out.close()
