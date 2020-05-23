#!/usr/bin python3
import sys
import socket


server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if (len(sys.argv) != 2):
    print("Usage: ./chatserver <server-ip>:<port>")
    sys.exit(1)
args = str(sys.argv[1].split(':'))
ip = str(args[0])
port = str(args[1])
