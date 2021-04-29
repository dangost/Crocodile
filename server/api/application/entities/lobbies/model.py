from uuid import uuid4


class Lobby:
    def __init__(self, lobby_name, lobby_pass=None, lobby_max_players=10):
        self.lobby_id = str(uuid4())
        self.lobby_name = lobby_name
        self.lobby_pass = lobby_pass
        self.lobby_max_players = lobby_max_players
        self.lobby_players = []
        self.current_players = 0

    @property
    def to_json(self) -> dict:
        _json = {
            "lobbyId": self.lobby_id,
            "lobbyName": self.lobby_name,
            "lobbyPass": self.lobby_pass,
            "maxPlayers": self.lobby_max_players,
            "lobbyPlayers": self.lobby_players,
            "currentPlayers": self.current_players
        }
        return _json

    @staticmethod
    def many_to_json(lobbies: list):
        _json = []
        for lobby in lobbies:
            _json.append(lobby.to_json)
        return _json

    @staticmethod
    def from_json(_json: dict):
        lobby_id = _json['lobbyId']
        lobby_name = _json['lobbyName']
        lobby_pass = _json['lobbyPass']
        lobby_max_players = _json['maxPlayers']
        current_players = _json['currentPlayers']
        lobby_players = _json['lobbyPlayers']

        lobby = Lobby(lobby_name, lobby_pass, lobby_max_players)
        lobby.lobby_id = lobby_id
        lobby.current_players = current_players
        lobby.lobby_players = lobby_players

        return lobby

    @staticmethod
    def many_from_json(_json: list):
        lobbies = list(map(Lobby.from_json, _json))
        return lobbies
