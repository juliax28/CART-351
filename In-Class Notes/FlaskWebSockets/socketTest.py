from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
app = Flask(__name__)
 


#needed for sockets
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)


users = {} #for maintaining the users, a dictionaries! No limit on devices that can be connected
#handle new connection
@socketio.on('connect')
#^^ New decorater function, when it receeives a CONNECT message it will run the CONNECT function, given to the SOCKETIO decorator. Same pattern as app.run but with sockets!
def connectFunction ():
     app.logger.info(request.sid)

@app.route('/')
def index():
     return render_template('socketTest.html')
socketio.run(app, debug=True)



