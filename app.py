from flask import Flask, render_template
from flask_socketio import SocketIO, send
from bot import ChatHistory, ask_bot
import time


# Initializing Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Never put passwords on code'
socketio = SocketIO(app)

# To keep track of conversation
chat_history = ChatHistory()

# Get default chat page
@app.route('/')
def index():
  return render_template('chat.html')

# Websocket for instant messaging
@socketio.on('message')
def answer_client(message):
  print(time.strftime('%H:%M:%S', time.localtime()) + ' | Received message: ' + message)
  send(ask_bot(message, chat_history))

if __name__ == '__main__':
  socketio.run(app, debug=True)