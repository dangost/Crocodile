# user: User { "address": ip, "userId": UUID, lobbyId: "UUID" }
import socket


class User:
    def __init__(self, connection: socket.socket):
        self.connection = connection
        self.ip, self.port = connection.getpeername()
        self.user_id: str = "0"
        self.lobby_id: str = "0"

    def init_user(self, user_id: str, lobby_id: str):
        self.user_id = user_id
        self.lobby_id = lobby_id

    @property
    def address_str(self) -> str:
        return f"{self.ip}:{self.port}"

    @property
    def address_tuple(self) -> tuple:
        return self.ip, self.port

    @property
    def to_string(self) -> str:
        return f"{self.address_str}\t{self.user_id}\t{self.lobby_id}"
