#!/usr/bin/python3

import socket

def fileToSend():
    text = open("text.txt","w")
    text.write("This file is gonna be sent\n")
    text.close()


fileToSend()

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 300

socket_server.bind((host,port))

socket_server.listen(3)

while True:

    client_socket, address = socket_server.accept()
    print("Connection recieved from {0}".format(str(address)))
    message1 = ("Thanks for connecting to our server")

    f = open("text.txt", "r")
    message2 = f.read()
    
    client_socket.send(message1.encode('ascii'))
    client_socket.send(message2)

    client_socket.close()

