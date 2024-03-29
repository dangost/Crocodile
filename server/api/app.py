from flask import Flask
from application.app.initialize import database
from application.entities.lobbies.controller import lobbies_controller
from application.entities.users.controller import users_controller

app = Flask(__name__)

ip = "0.0.0.0"
port = 8080

# init routes
app.register_blueprint(lobbies_controller)
app.register_blueprint(users_controller)

if __name__ == "__main__":
    database.load()
    app.run(ip, port)
