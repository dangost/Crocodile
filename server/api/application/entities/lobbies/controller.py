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
    return jsonify(players)


@lobbies_controller.route('/api/lobbies/<lobby_name>/<lobby_pass>/<int:lobby_max_players>/', methods=['GET'])
def post_lobby(lobby_name: str, lobby_pass: str, lobby_max_players: int):
    if lobby_pass == "null":
        lobby_pass = None

    lobby = Lobby(lobby_name, lobby_pass, lobby_max_players)

    lobby = LobbiesRepository.create_lobby(lobby)
    lobby_json = lobby.to_json
    return jsonify(lobby_json)


@lobbies_controller.route('/api/lobbies/<lobby_id>/players/<player_id>/join', methods=['GET'])
def lobby_join_player(lobby_id, player_id):
    response = LobbiesRepository.lobby_join_player(lobby_id, player_id)
    return jsonify(response)


@lobbies_controller.route('/api/lobbies/<lobby_id>/players/<player_id>/quit', methods=['GET'])
def lobby_quit_player(lobby_id, player_id):
    response = LobbiesRepository.lobby_quit_player(lobby_id, player_id)
    return jsonify(response)


@lobbies_controller.route('/api/lobbies/<lobby_id>/player-guessed/<player_id>/', methods=['GET'])
def lobby_player_guessed(lobby_id, player_id):
    # todo check that lobby contains player
    # todo create new word and turn queue
    # todo return {"word" : str, "drawerId": str}
    response = LobbiesRepository.lobby_player_guessed(lobby_id, player_id)

    return jsonify(response)
