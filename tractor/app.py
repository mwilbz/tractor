import logging

from flask import Flask, render_template
from flask_socketio import emit, join_room, leave_room, SocketIO
from shortuuid import uuid

from game import Game

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

GAMES = {}

LOGGER = logging.getLogger(__name__)


@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')


@socketio.on('connect')
def connection():
    LOGGER.info(f'A user just connected!')


@socketio.on('disconnect')
def disconnection():
    LOGGER.info(f'A user just disconnected!')


@socketio.on('create_game')
def create_game():
    game_id = uuid()
    GAMES[game_id] = Game()
    LOGGER.info(f'Created game {game_id}. GAMES is now {GAMES}')
    join_room(game_id)
    return {'game_id': game_id}


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    LOGGER.info('App running!')
    socketio.run(app)
