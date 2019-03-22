#!/usr/bin/env python

from jsonrpclib import Server

switch = Server(
    "http://admin:arista@eos-leaf1/command-api")

response = switch.runCmds(1, ["show version"])

print(response)
