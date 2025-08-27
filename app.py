<<<<<<< HEAD
# app.py (Corregido y listo para producción)
=======
# app.py
>>>>>>> cc1b273 (cambios hechos en el tren)

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from game import Game
<<<<<<< HEAD
=======
import socket # Importamos el módulo socket
>>>>>>> cc1b273 (cambios hechos en el tren)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

game = Game(socketio)

@app.route('/')
def index():
    return render_template('index.html')

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

<<<<<<< HEAD
if __name__ == '__main__':
    socketio.run(app, debug=True)
=======
# Función para obtener la IP local
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No es necesario que sea alcanzable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1' # IP de fallback
    finally:
        s.close()
    return IP

if __name__ == '__main__':
    # Usamos host='0.0.0.0' para que sea accesible desde otros dispositivos en la misma red
    host = '0.0.0.0'
    port = 5000
    local_ip = get_local_ip()
    print("*"*50)
    print(f"Servidor iniciado. Para jugar, accede a: http://{local_ip}:{port}")
    print("*"*50)
    socketio.run(app, host=host, port=port, debug=True)
>>>>>>> cc1b273 (cambios hechos en el tren)
