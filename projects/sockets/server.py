#!/usr/bin/python3

#SOCKETS

import socket

HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # AF_INET -> IPv4 // SOCK_STREAM -> TCP
server.bind((HOST, PORT))                                       # bind server to IP and PORT

server.listen(5)                                                # hoe many unaccepted connections to allow 
                                                                # before dropping new ones
while True:
    communication_socket, address = server.accept()             #accept a connection // returns a socket used to send mesages back and IP of client
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')           # specify buffer size and decode
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got your message! Thank you!".encode('utf-8'))      #use com_socket to send responce
    communication_socket.close()                                                    #c close connection
    print(f"Connection with {address} ended!")