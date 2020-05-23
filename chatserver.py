#!/usr/bin python3
import sys
import socket
import select

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if (len(sys.argv) != 2):
    print("Usage: ./chatserver <server-ip>:<port>")
    sys.exit(1)
args = str(sys.argv[1].split(':'))
ip = str(args[0])
port = str(args[1])

# bind the (ip,port) to the server
server.bind(ip, port)
# listen for atmost 100 connections
server.listen(100)
clients = []
clients.append(server)
clients_hashmap = {}
perm_clients = []


def broadcast(msg, conn):
    for client in perm_clients:
        if client!=conn:
            print("Broadcasting")
            try:
                client.sendall(msg.encode('ascii'))
            except:
                client.close()
                perm_clients.remove(client)
                del clients_hashmap[client]
                clients.remove(client)

def main():
    print("Chat Server running")
    while True:
        readsockets, writesockets, errorsockets = select.select(clients, [], [])
        for socket in readsockets:
            if socket == server:
                # accept a new connection
                newclient, addr = server.accept()
                newclient.sendall("Hello 1".encode('ascii'))
                clients.append(newclient)
            elif socket in


