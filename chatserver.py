#!/usr/bin python3
import re
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
clients = [server]
clients_hashmap = {}
clients_in_queue = []


def broadcast(msg, conn):
    for client in clients_hashmap.keys():
        if client!=conn:
            print("Broadcasting")
            try:
                client.sendall(msg.encode('ascii'))
            except:
                client.close()
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
                clients_in_queue.append(newclient)
            elif socket in clients_in_queue:
                try:
                    name_load = socket.recv(1024).decode('ascii')
                    if name_load:
                        check = re.search(r'NICK\s(\S*)',name_load)
                        name = str(check.group(1))
                        if len(name)>12:
                            socket.sendall("ERROR".encode('ascii'))
                        elif re.search(r'!',name_load):
                            socket.sendall("ERROR")
                        elif check:
                            socket.sendall(("Welcome to chat room" + str(name)).encode('ascii'))
                            clients_hashmap[socket] = name
                            clients_in_queue.remove(socket)
                        else:
                            socket.sendall("ERROR".encode('ascii'))
                    else:
                        socket.close()
                        clients.remove(socket)
                        clients_in_queue.remove(socket)
                except:
                    continue



