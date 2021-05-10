import socket
import threading
import time
from typing import List

import jpysocket

from models.user import User


class Server:
    def __init__(self, ip, port):
        self.users: List[User] = []
        self.ip = ip
        self.port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(0)
        threading.Thread(target=self.connect_handler).start()

        # we need all data about users
        # i think to get it by json
        # store it in ram
        # user: User { "connection": socket, "userId": UUID, lobbyId: "UUID" }

    def connect_handler(self):
        while True:
            connection, address = self.server.accept()
            if next((user for user in self.users if user.connection == connection), None) is None:
                user = User(connection)
                self.users.append(user)
                threading.Thread(target=self.message_handler, args=(user,)).start()

                message = jpysocket.jpyencode("Connected")
                user.connection.send(message)
                print("connection")

    def message_handler(self, user: User):
        while True:
            _message = user.connection.recv(1024)

            # handle json

            # а похуй на тот джисон, будем делать на клиенте всё

            for _client in self.users:
                if _client.connection != user.connection:
                    _client.connection.send(_message)
                    print("message sent")
            time.sleep(1)


server = Server("192.168.100.5", 9090)
