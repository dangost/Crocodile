import socket
import threading
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

                if _message == b'':
                    raise Exception

                response: list = self.handle_message(_message)

                check = False
                if response is None:
                    pass
                elif response[0] == Events.exit_:
                    print('exit')
                    raise Exception

                elif response[0] == Events.guessed_:
                    _message = response[2]
                    check = response[3]

                elif response[0] == Events.user_init:
                    user_idx = self.users.index(user)
                    user.user_id, user.lobby_id = response[2]
                    self.users[user_idx] = user
                    _message = response[3]
                    check = True

                users = list(filter(lambda u: u.lobby_id == user.lobby_id, self.users))
                for _client in users:
                    if _client.connection != user.connection or check:
                        _client.connection.send(_message)

            except BaseException:
                self.users.remove(user)
                user.connection.close()
                print('user has closed | ', user.address_str)
                break

    def handle_message(self, message: bytes):
        # 0 - exit,
        try:
            message: str = jpysocket.jpydecode(message)

            _json_str = message[1:len(message)]

            _json = json.loads(_json_str)

            event = int(message[0])

            if event == Events.exit_:
                print('exit')
                return [event]

            elif event == Events.chat_:
                print("chat")
                return [event]

            elif event == Events.brush_:
                return [event]

            elif event == Events.guessed_:
                lobby_id = _json['lobbyId']
                user_id = _json['userId']

                # address = f"http://{self.ip}:8080/api/lobbies/{lobby_id}/player-guessed/{user_id}/"
                address = f"http://77.223.97.149:8080/api/lobbies/{lobby_id}/player-guessed/{user_id}/"
                print("guess")

                response = requests.get(address).text

                #####
                _json = json.loads(response)
                print(_json['text'])
                #####

                encoded = jpysocket.jpyencode(str(Events.guessed_) + response)

                not_check_me = True

                return [event, "OK", encoded, not_check_me]

            elif event == Events.user_init:
                lobby_id = _json['lobbyId']
                user_id = _json['userId']

                user_json = requests.get(f"http://77.223.97.149:8080/api/users/{user_id}/").text

                encoded = jpysocket.jpyencode(str(Events.user_connected) + user_json)

                return [event, "OK", (user_id, lobby_id), encoded]

        except BaseException as e:
            print(e)
            return None


# server = Server("192.168.100.5", 9090)
server = Server("77.223.97.149", 9090)
