#! /usr/bin/python2.7

import socket
import Queue
import sys
import ipcMessage_pb2
import chat
from thread import *
from galatea.galatea import Galatea

class Slave():
    def __init__(self, port, logger):

        self._logger = logger

        self._logger.info("Slave init start")

        self.host = ''
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._logger.info("Slave init sockets")

        self.chatDict = dict()

        self._logger.info("Slave init start nn")
        self.load_nn()
        self._logger.info("Slave init end nn")

        self.socket.bind((self.host, self.port))
        self.socket.listen(10)

        self._logger.info("Slave listening to socket")

        while 1:
            conn, addr = self.socket.accept()

            start_new_thread(self.handleConn ,(conn,))

        self.socket.close()

    def load_nn(self):
        self.g = Galatea()


    def handleConn(self, conn):

        data = conn.recv(4096)
        if data:
            hello = ipcMessage_pb2.Hello()
            hello.ParseFromString(data)

            if not hello.response:
                respHello = ipcMessage_pb2.Hello()
                respHello.response = True

                conn.send(respHello.SerializeToString())

        while True:

            #Receiving from client
            data = conn.recv(4096)
            if not data:
                break

            msg = ipcMessage_pb2.Message()
            msg.ParseFromString(data)

            if msg.chatId not in self.chatDict:
                self.chatDict[msg.chatId] = chat.Chat(self.g)

            self.chatDict[msg.chatId].addMessage(msg)

            respMsg = ipcMessage_pb2.Message()
            if msg.respond:
                respMsg.text = self.chatDict[msg.chatId].runNN()
                respMsg.chatId = msg.chatId
                respMsg.userId = msg.userId
                respMsg.time = msg.time
                respMsg.respond = True

                conn.send(respMsg.SerializeToString())


        conn.close()

if __name__ == '__main__':
    Slave(24833)
