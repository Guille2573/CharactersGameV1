# No es necesario importar y parchear eventlet aquí, Gunicorn se encarga.
# import eventlet
# eventlet.monkey_patch()

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from game import Game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Dejamos async_mode='eventlet' para que Flask-SocketIO sepa qué esperar.
socketio = SocketIO(app, async_mode='eventlet')

game = Game(socketio)

@app.route('/')
def index():
    return render_template('index.html')

# --- El resto de tus rutas y manejadores de eventos no cambian ---

@socketio.on('join_game')
def on_join(data):
    sid = request.sid
    result = game.handle_join(data, sid)
    emit('join_response', result, room=sid)
    socketio.emit('players_update', game.get_players_info())

@socketio.on('start_game')
def on_start():
    game.handle_start()

@socketio.on('make_accusation')
def on_accuse(data):
    game.handle_accusation(data)

@socketio.on('send_general_message')
def on_general_msg(data):
    game.handle_general_message(data)

@socketio.on('send_private_message')
def on_private_msg(data):
    game.handle_private_message(data)


if __name__ == '__main__':
    # Para pruebas locales, eventlet debe estar instalado
    # y este comando usará el servidor de desarrollo de Flask
    socketio.run(app, debug=True)