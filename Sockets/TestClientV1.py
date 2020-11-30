#!/usr/bin python

# Der Client - empfängt Nachrichten per Socket-Verbindung von einem Server
# Erstellt: 29/10/20

import socket
import json

HOST = "127.0.0.1"
PORT = 64000

with socket.socket(socket.AF_INET) as sh:
    sh.connect((HOST, PORT))
    print("*** Verbindung mit Server wurde hergestellt")
    sh.sendall(b"info")
    data = sh.recv(1024)
    print(repr(data))
    sh.sendall(b"quit")



