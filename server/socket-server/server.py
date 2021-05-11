import socket
import threading
import time
from typing import List
from models.events import Events
import json
import requests

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
        print("started ", self.port)
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
            try:
                _message = user.connection.recv(1024)

                response: list = self.handle_message(_message)
                if response is None:
                    pass
                elif response[0] == Events.exit_:
                    self.users.remove(user)
                    break

                elif response[0] == Events.guessed_:
                    _message = response[2]

                for _client in self.users:
                    if _client.connection != user.connection:
                        _client.connection.send(_message)
                        print("message sent")
                time.sleep(1)
            except BaseException:
                self.users.remove(user)
                break

    def handle_message(self, message: bytes):
        # 0 - exit,
        try:
            message: str = jpysocket.jpydecode(message)

            _json_str = message[1:len(message)]

            _json = json.loads(_json_str)

            event = int(message[0])

            if event == Events.exit_:
                return [event]

            elif event == Events.chat_:
                print("chat")
                return [event]

            elif event == Events.brush_:
                return [event]

            elif event == Events.guessed_:
                lobby_id = _json['lobbyId']
                user_id = _json['userId']

                address = f"http://{self.ip}:8080/api/lobbies/{lobby_id}/player-guessed/{user_id}/"
                print("guess")
                response = requests.get(address).json()
                print(response['text'])
                encoded = jpysocket.jpyencode(response)

                return [event, "OK", encoded]

        except BaseException as e:
            print(e)
            return None


# server = Server("192.168.100.5", 9090)
server = Server("77.223.97.149", 9092)
