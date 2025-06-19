from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import json
from random import randint


class Player:
    def __init__(self):
        self.sid = None
        self.username = None

    def __repr__(self):
        return f"Player(sid={self.sid}, username={self.username})"


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
# Allow all origins for CORS, change * to URL for security
players = {}


with open("server/words.json") as data:
    words = json.load(data)


@socketio.on("connect")
def handle_connect():
    players[request.sid] = Player()
    print(f"player count: {len(players)}")


@socketio.on("disconnect")
def handle_disconnect():
    players.remove(request.sid)
    print(f"{request.sid} disconnected")
    print(f"player count: {len(players)}")
    # socketio.emit("player_list", json.dumps(list(players.values())))


@socketio.event
def set_username(usr):
    players[request.sid].username = usr
    print(f"username: {usr}")
    # socketio.emit("player_list", json.dumpslist(players.values()))

    random_word = words[randint(0, len(words) - 1)]["english"]
    print(f"new word: {random_word}")
    socketio.emit("new", f"{random_word}")


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
