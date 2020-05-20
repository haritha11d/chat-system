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
    sys.exit(1)
# protocol part 1.2 receiving Hello <VERSION> from server
try:
    hello = client.recv(1024).decode('ascii')
    print(hello)
except:
    print("Not able to receive Hello <VERSION> msg from the server at address " + ip + ":" + str(port) + '\n' + "Exiting :)")
    sys.exit(1)

# protocol part 2 sending NICK <nick> and receiving OK/ERR <text> as a response from the server
nick_load = "NICK " + nick
client.sendall((nick_load).encode('ascii'))
response = client.recv(1024).decode('ascii')
if response == 'Error' or response == 'ERROR':
    print(response)
    sys.exit(1)
print(response)
