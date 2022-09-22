from flask import Flask
from flask import request
from flask import render_template
import json     

app = Flask(__name__)

@app.route("/")
def general_room():
    return render_template('index.html')

@app.route("/<int:room_id>")
def room(room_id):
    return render_template('index.html')

@app.route('/api/chat/general', methods=['GET', 'POST']) # some dummy text
def general_chat():
    db_path = 'database/rooms.json'
    room_name = 'general'
    if request.method == 'POST':
        username = request.form['username']
        user_message = request.form['msg']
        if len(username) < 1 or len(user_message) < 1:
            return "Error: username or message is empty."

        handle_post_message(room_name, username, user_message)
        return 'Message added successfully!'

    elif request.method == 'GET':
        rooms_data = get_room_data()
        if rooms_data and room_name in rooms_data and len(rooms_data[room_name]):
            return ''.join(rooms_data[room_name])
        else:
            return 'There is no messages yet.'


@app.route('/api/chat/<int:room_id>', methods=['GET', 'POST'])
def room_chat(room_id):
    room_name = f"room{room_id}"
    if request.method == 'POST':
        username = request.form['username']
        user_message = request.form['msg']
        if len(username) < 1 or len(user_message) < 1:
            return "Error: username or message is empty."

        handle_post_message(room_name, username, user_message)
        return 'Message added successfully!'

    elif request.method == 'GET':
        rooms_data = get_room_data()
        if rooms_data and room_name in rooms_data and len(rooms_data[room_name]):
            return ''.join(rooms_data[room_name])
        else:
            return 'There is no messages yet.'


def handle_post_message(room_name, username, user_message):
    db_path = 'database/rooms.json'
    msg = f"{username}: {user_message}\n"

    rooms_data = get_room_data()

    with open(db_path, 'w') as f:
        if (room_name not in rooms_data):
            rooms_data[room_name] = []
        rooms_data[room_name].append(msg)
        json.dump(rooms_data, f)


def get_room_data():
    db_path = 'database/rooms.json'
    with open(db_path, 'r') as f:
        try:
            rooms_data = json.load(f)
            return rooms_data
        except:
            return {}