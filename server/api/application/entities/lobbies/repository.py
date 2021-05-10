from application.app.initialize import database
from application.entities.lobbies.model import Lobby
from typing import List
from application.entities.users.repository import UsersRepository


class LobbiesRepository:
    @staticmethod
    def get_all_lobbies() -> list:
        all_lobbies = database.lobbies
        _json = Lobby.many_to_json(all_lobbies)
        return _json

    @staticmethod
    def get_by_id(lobby_id: str) -> dict:
        all_lobbies = database.lobbies
        lobby = next((lo for lo in all_lobbies if lo.lobby_id == lobby_id), None)
        lobby_json = lobby.to_json
        return lobby_json

    @staticmethod
    def get_lobby_players(lobby_id:  str) -> List[dict]:
        all_lobbies = database.lobbies
        lobby = next((lo for lo in all_lobbies if lo.lobby_id == lobby_id), None)

        players_list: List[dict] = []
        for player_id in lobby.lobby_players:
            user = UsersRepository.get_user_by_id(player_id)
            players_list.append(user)
        return players_list

    @staticmethod
    def lobby_join_player(lobby_id, player_id) -> int:
        for i in range(len(database.lobbies)):
            if database.lobbies[i].lobby_id == lobby_id:
                if database.lobbies[i].current_players >= \
                        database.lobbies[i].lobby_max_players:
                    return 400
                database.lobbies[i].lobby_players.append(player_id)
                database.lobbies[i].current_players += 1
                return 200
        return 404

    @staticmethod
    def lobby_quit_player(lobby_id, player_id) -> int:
        for i in range(len(database.lobbies)):
            if database.lobbies[i].lobby_id == lobby_id:
                database.lobbies[i].lobby_players.remove(player_id)
                database.lobbies[i].current_players -= 1
                if database.lobbies[i].current_players >= 0:
                    database.lobbies.remove(database.lobbies[i])
                return 200
        return 404

    @staticmethod
    def create_lobby(lobby) -> Lobby:
        database.lobbies.append(lobby)
        return lobby
