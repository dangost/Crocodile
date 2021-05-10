import socket
import threading
import time

import jpysocket


class Server:
    def __init__(self, ip, port):
        self.clients = []
        self.ip = ip
        self.port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(0)
        threading.Thread(target=self.connect_handler).start()

        # we need all data about users
        # i think to get it by json
        # store it in ram
        # user: User [ "connection": socket,

    def connect_handler(self):
        while True:
            client, address = self.server.accept()
            if client not in self.clients:
                self.clients.append(client)
                threading.Thread(target=self.message_handler, args=(client,)).start()

                message = jpysocket.jpyencode("Connected")
                client.send(message)
                print("connection")

    def message_handler(self, client):
        while True:
            _message = client.recv(1024)

            for _client in self.clients:
                if _client != client:
                    _client.send(_message)
                    print("message sent")
            time.sleep(1)


server = Server("192.168.100.5", 9090)
