from os import getenv

from flask import Flask
from application.app.initialize import database
from application.entities.lobbies.controller import lobbies_controller
from application.entities.users.controller import users_controller

app = Flask(__name__)

ip = getenv("IP")
port = getenv("PORT")

if ip is None:
    ip = "127.0.0.1"
if port is None:
    port = 9090

# init routes
app.register_blueprint(lobbies_controller)
app.register_blueprint(users_controller)

if __name__ == "__main__":
    database.load()
    app.run(ip, port)
