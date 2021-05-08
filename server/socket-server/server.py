import socket
from typing import List
from models.client import Client
from models.log import Log
from threading import *
import jpysocket


class Server:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 9090

        self.clients: List[Client] = []

        self.server: socket.socket = None

        self.server_quit = False

        self.threads = []

        self.connections = []

    def connecting(self):
        try:
            while not self.server_quit:
                self.server.listen(5)
                connection, client_address = self.server.accept()

                new_client = Client(name=None, address=client_address, connection=connection)
                message = jpysocket.jpyencode("Welcome")
                connection.send(message)
                self.clients.append(new_client)
                print('appended')
                print(f"new connection {client_address}")
                self.threads.append(Thread(target=self.server_messaging, args=[new_client]))
                self.threads[-1].start()
        except BaseException as e:
            print(e)
            self.shut_down()

    def server_messaging(self, client):
        print("server receiving..\n")
        try:
            self.server_quit = False
            while not self.server_quit:
                try:

                    answer = self.server.recvfrom(1024)
                    data = answer[0]
                    address = answer[1]
                    if address not in self.connections:
                        self.connections.append(address)

                    message = jpysocket.jpydecode(data)

                    log = None

                    for i in range(len(self.clients)):
                        client = self.clients[i]
                        if client.name is None:
                            self.clients[i].name = message  # fist message is username!
                            log = Log(client)
                        else:
                            log = Log(client, message)

                        if log is not None:
                            break

                    print(log)

                    for connection in self.connections:  # sending to clients
                        if address != connection:
                            message_to_send = jpysocket.jpyencode(message)
                            self.server.sendto(message_to_send, connection)

                except BaseException as e:
                    print(e)
                    print("Thread has stopped")
                    self.server_quit = True
        except BaseException as e:
            print(e)
            self.server.close()
            self.server_quit = True

    def start(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.ip, self.port))

            print(f"Server started as [{self.ip}:{self.port}]")

            connect = Thread(target=self.connecting, args=[])
            connect.start()
        except BaseException as e:
            print(e)
            print("shut down")
            self.server_quit = True
            self.server.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shut_down()

    def shut_down(self):
        self.server.close()


server = Server()
server.start()
