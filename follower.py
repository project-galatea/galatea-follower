#! /usr/bin/python2.7

import socket
import sys
import ipcMessage_pb2
from thread import *

class Follower():
    def __init__(self, port):
        self.host = ''
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.bind((self.host, self.port))
        self.socket.listen(10)

        while 1:
            conn, addr = self.socket.accept()

            start_new_thread(handleConn ,(conn,))

        self.socket.close()

def handleConn(conn):

    while True:

        #Receiving from client
        data = conn.recv(4096)
        if not data:
            break

        msg = ipcMessage_pb2.Message()
        msg.ParseFromString(data)

    conn.close()
