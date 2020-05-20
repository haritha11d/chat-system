#!/usr/bin python3

import sys
import re
import select
import socket

if len(sys.argv) != 3:
    print("Usage: ./chat-client <server-ip>:<portnum> nick")
    sys.exit(1)

# Split the arguments into ip, port, nick

args = str(sys.argv[1]).split(':')
ip = str(args[0])
port = int(args[1])
nick = str(sys.argv[2])

# try to connect to the server
client = socket.socket()
try:
    client.connect((ip,port))
    print("connected to server at address " + ip + ":" + str(port) + '\n')
except:
    print("Not able to connect to server at address " + ip + ":" + str(port) + '\n' + "Exiting :)")
