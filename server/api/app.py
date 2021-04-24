from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/api/ip", methods=['GET'])
def ping():
    return jsonify({"ip": request.remote_addr})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

