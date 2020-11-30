#!/usr/bin python

# Der Client - empfängt Card-Messages per Socket-Verbindung von einem Server
# Erstellt: 29/10/20

import socket
import json

HOST = "127.0.0.1"
PORT = 64000

with socket.socket(socket.AF_INET) as sh:
    sh.connect((HOST, PORT))
    print("*** Verbindung mit Server wurde hergestellt")
    for _ in range(0,2):
        sh.sendall(b"deal")
        data = sh.recv(1024)
        print(repr(data))
        jsonText = data.decode("utf8")
        c = json.loads(jsonText)
        print("Die Karte ist: " + c["body"]["name"])
    sh.sendall(b"quit")



