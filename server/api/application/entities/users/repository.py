from application.app.initialize import database
from application.entities.users.model import User


class UsersRepository:
    @staticmethod
    def get_all_users():
        users = database.users
        users_json = User.many_to_json(users)
        return users_json

    @staticmethod
    def get_user_by_id(user_id: str) -> dict:
        user = next((u for u in database.users if u.user_id == user_id), None)
        user_json = user.to_json
        return user_json

    @staticmethod
    def create_new_user(nickname, avatar_id) -> str:
        user = User(nickname, avatar_id)
        user_id = user.user_id
        database.users.append(user)
        database.save()
        return user_id

    @staticmethod
    def update_user(user: User) -> int:
        for i in range(len(database.users)):
            if database.users[i].user_id == user.user_id:
                database.users[i] = user
                database.save()
                return 200
        return 404
