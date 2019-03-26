#!/usr/bin/python

from jsonrpclib import Server
switch = Server (
"http://ntc:ntc123@spine1/command-api" )

response = switch.runCmds( 1, ["enable",
"configure",
"vlan 500",
"name printer"] )
