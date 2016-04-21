#! /usr/bin/python2.7

import socket
import Queue
import sys
import ipcMessage_pb2
import chat
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

chatDict = dict()

def handleConn(conn):

    while True:

        #Receiving from client
        data = conn.recv(4096)
        if not data:
            break

        msg = ipcMessage_pb2.Message()
        msg.ParseFromString(data)

        if msg.chatId not in chatDict:
            chatDict[msg.chatId] = chat.Chat()

        chatDict[msg.chatId].addMessage(msg)

        respMsg = ipcMessage_pb2.Message()
        respMsg.text = chatDict[msg.chatId].runNN()
        respMsg.chatId = msg.chatId
        respMsg.userId = msg.userId

        conn.send(respMsg.SerializeToString())


    conn.close()

Follower(24833)
