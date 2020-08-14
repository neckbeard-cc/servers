#!/usr/bin/env python

import json

file_in = open("servers.txt", "r")
raw = file_in.read().splitlines()
file_in.close()

servers = []
for address in raw:
    servers.append({"name": address, "ip": address, "type": "PC"})

file_out = open("servers.json", "w")
file_out.write(json.dumps(servers, indent=2))
file_out.close()
