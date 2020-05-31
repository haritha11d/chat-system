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
   # print("connected to server at address " + ip + ":" + str(port) + '\n')
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
if response[:5].upper() == 'ERROR':
    print(response)
    sys.exit(1)
print(response)

'''
develop the code for protocol part 3
Client : MSG <text> --> Server
Server: MSG nick <text> / ERROR <text> --> Client
'''

while True:
    sockets = [sys.stdin, client] # reading sockets
    # just have to read sockets either from stdin or client socket (from server)
    read_sockets, write_sockets, error_sockets = select.select(sockets, [], [])
    for socket in read_sockets:
        # if there is a receiving socket from the server
        if socket == client:
            msg = client.recv(1024).decode('ascii')
            if (msg[:5].upper() == 'ERROR'):
                print(msg)
            else:
                # strip out the MSG part
                msg = msg[4:]
                print(msg)
        # take the standard input from user!
        else:
            msg = sys.stdin.readline()
            if (msg == '\n'):
                continue
            else:
                msg_load = 'MSG ' + msg
                client.sendall((msg_load).encode('ascii'))

# close the connection to server (client socket)
client.close()

