from application.data.abstract.base_database import BaseDatabase
import os
import json

from application.entities.users.model import User


class JsonDatabase(BaseDatabase):
    def __init__(self):
        self.path = "../../storage/users.json"

    def load(self):
        if not os.path.isdir("../../storage"):
            os.mkdir("../../storage")
            with open(self.path, 'w') as created_json:
                created_json.write('[]')
        users_json = open(self.path, 'r')
        json_string = users_json.read()
        self.users = list(User.many_from_json(json.loads(json_string)))
        self.lobbies = []

    def save(self):
        _users_json = []
        for user in self.users:
            _users_json.append(user.to_json)

        with open(self.path, 'w') as users_json:
            users_json.write(json.dumps(_users_json))



