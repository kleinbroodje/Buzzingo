from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import json
from random import choice
from threading import Thread
import time


# flask setup
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


# business logic
class Player:
    def __init__(self):
        self.sid = None
        self.username = None

    def __repr__(self):
        return f"Player(sid={self.sid}, username={self.username})"


players = {}


# "database" of words
countdown_active = False


with open("words.json", encoding="utf8") as data:
    words = json.load(data)


def get_active_usernames():
    return list(player.username for player in players.values() if player.username is not None)


# socket endpoints
@socketio.on("connect")
def handle_connect():
    players[request.sid] = Player()
    socketio.emit("player_list", get_active_usernames())
    print(f"player count: {len(players)}")


@socketio.on("disconnect")
def handle_disconnect():
    del players[request.sid]
    socketio.emit("player_list", get_active_usernames())
    print(f"{request.sid} disconnected")
    print(f"player count: {len(players)}")


@socketio.event
def set_username(usr):
    players[request.sid].username = usr
    print(f"username: {usr}")
    socketio.emit("player_list", get_active_usernames())

    if len(get_active_usernames()) == 2:
        # DUEL
        start_countdown()


@socketio.event
def handle_buzzer(arg):
    pass


def start_countdown():
    global countdown_active

    def start():
        global countdown_active    
        
        for t in range(5, 0, -1):
            socketio.emit("countdown", t)
            time.sleep(1)
        socketio.emit("countdown", "It's time to d-d-d-d-d-d-d-d-d-d-duel!")
        countdown_active = False
        time.sleep(5.5)
        gen_new_word()

    if not countdown_active:
        Thread(target=start).start()
        countdown_active = True


def gen_new_word():
    random_word = choice(words)["english"]
    print(f"new word: {random_word}")
    socketio.emit("new_word", f"{random_word}")


# main
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
