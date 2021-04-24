from flask import Flask, jsonify, request
import socket


ip = socket.gethostbyname(socket.gethostname())
port = 8080

app = Flask(__name__)


@app.route("/api/ip", methods=['GET'])
def ping():
    return jsonify({"ip": request.remote_addr})


if __name__ == "__main__":
    print({ip: port})
    app.run(host=ip, port=port)

