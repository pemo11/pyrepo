#!/usr/bin python

# Der Server - sendet Nachrichten per Socket-Verbindung an einen Client
# Erstellt: 29/10/20

import socket
import json
from json import JSONEncoder

class Message(object):

    def __init__(self, Id, Header, Body):
        self.id = Id
        self.header = Header
        self.body = Body

class MsgEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__

HOST = "127.0.0.1"
PORT = 64000

with socket.socket(socket.AF_INET) as sh:
    sh.bind((HOST, PORT))
    print(f"*** Warten auf Verbindung auf Port {PORT} ***")
    sh.listen()

    conn, addr = sh.accept()
    with conn:
        print(f"*** Verbindung mit {addr}:{PORT} wurde hergestellt ***")
        abbruch = False
        while not abbruch:
            data = conn.recv(1024)
            if not data:
                abbruch = True
            # Auswerten der Client-Anforderung
            clientMsg = data.decode("utf8")
            if clientMsg == "quit":
                abbruch  = True
                print("*** Just quitting ***")
            else:
                bodyText = "Welcome, to the socket machine"
                headerText = clientMsg
                msg = Message(1, headerText, bodyText)
                print(">>>" + MsgEncoder().encode(msg))
                # Jetzt soll die Nachricht als Json-Text übertragen werden
                jsonText = json.dumps(msg, indent=4, cls=MsgEncoder)
                conn.sendall(bytes(jsonText,encoding="utf8"))
