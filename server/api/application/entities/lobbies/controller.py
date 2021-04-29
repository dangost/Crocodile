from flask import Blueprint, jsonify, request

from application.entities.lobbies.model import Lobby
from application.entities.lobbies.repository import LobbiesRepository

lobbies_controller = Blueprint('lobbies_controller', __name__)


@lobbies_controller.route('/api/lobbies/', methods=['GET'])
def get_all():
    lobbies = LobbiesRepository.get_all_lobbies()
    return jsonify(lobbies)


@lobbies_controller.route('/api/lobbies/<lobby_id>/', methods=['GET'])
def get_by_id(lobby_id: str):
    lobby = LobbiesRepository.get_by_id(lobby_id)
    return jsonify(lobby)


@lobbies_controller.route('/api/lobbies/<lobby_id>/players', methods=['GET'])
def get_lobby_players(lobby_id: str):
    players = LobbiesRepository.get_lobby_players(lobby_id)
    return players


@lobbies_controller.route('/api/lobbies/', methods=['POST'])
def post_lobby():
    _json = request.get_json()
    lobby_name = _json['lobbyName']
    lobby_pass = _json['lobbyPass']
    lobby_max_players = _json['lobbyMaxPlayers']

    lobby = Lobby(lobby_name, lobby_pass, lobby_max_players)

    lobby_id = LobbiesRepository.create_lobby(lobby)
    return lobby_id


@lobbies_controller.route('/api/lobbies/<lobby_id>/players/<player_id>/join', methods=['GET'])
def lobby_join_player(lobby_id, player_id):
    response = LobbiesRepository.lobby_join_player(lobby_id, player_id)
    return jsonify(response)


@lobbies_controller.route('/api/lobbies/<lobby_id>/players/<player_id>/quit', methods=['GET'])
def lobby_quit_player(lobby_id, player_id):
    response = LobbiesRepository.lobby_quit_player(lobby_id, player_id)
    return jsonify(response)
