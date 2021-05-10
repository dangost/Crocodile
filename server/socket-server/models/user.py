# user: User { "address": ip, "userId": UUID, lobbyId: "UUID" }
import socket


class User:
    def __init__(self, connection: socket.socket, user_id: str, lobby_id: str):
        self.ip, self.port = connection.getpeername()
        self.user_id = user_id
        self.lobby_id = lobby_id

    @property
    def address(self) -> str:
        return f"{self.ip}:{self.port}"
