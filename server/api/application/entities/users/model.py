from uuid import uuid4


class User:
    def __init__(self, nickname, avatar_id):
        self.user_id = str(uuid4())
        self.nickname = nickname
        self.avatar_id = avatar_id

    @property
    def to_json(self) -> dict:
        _json = {
            "userId": self.user_id,
            "nickname": self.nickname,
            "avatarId": self.avatar_id
        }
        return _json

    @staticmethod
    def from_json(_json: dict):
        user_id = _json['userId']
        nickname = _json['nickname']
        avatar_id = _json['avatarId']

        user = User(nickname, avatar_id)
        user.user_id = user_id

        return user

    @staticmethod
    def many_from_json(_json: list):
        users = list(map(User.from_json, _json))
        return users
