from multiprocessing import connection
from flask import Flask
from flask import request
from flask import render_template
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    user='root', password='example', port='3306', database='mydb'
)
print('DB connected')
cursor = connection.cursor()

@app.route("/")
def general_room():
    return render_template('index.html')


@app.route("/<int:room_id>")
def room(room_id):
    return render_template('index.html')


@app.route('/api/chat/general', methods=['GET', 'POST']) # some dummy text
def general_chat():
    room_name = 'general'
    if request.method == 'POST':
        username = request.form['username']
        user_message = request.form['msg']
        if len(username) < 1 or len(user_message) < 1:
            return "Error: username or message is empty."

        handle_post_message(room_name, username, user_message)
        return 'Message added successfully!'

    elif request.method == 'GET':
        chat_list = get_room_data(room_name)
        return chat_list


@app.route('/api/chat/<int:room_id>', methods=['GET', 'POST'])
def room_chat(room_id):
    if request.method == 'POST':
        username = request.form['username']
        user_message = request.form['msg']
        if len(username) < 1 or len(user_message) < 1:
            return "Error: username or message is empty."

        handle_post_message(room_id, username, user_message)
        return 'Message added successfully!'

    elif request.method == 'GET':
        chat_list = get_room_data(room_id)
        return chat_list



def handle_post_message(room_name, username, user_message):
    sql = f"INSERT INTO rooms (username, msg, room_id) VALUES (%s, %s, %s)"
    val = (username, user_message, room_name)
    cursor.execute(sql, val)
    connection.commit()


def get_room_data(room_name):
    cursor.execute(f"SELECT * FROM rooms WHERE room_id='{room_name}'")
    room_data = cursor.fetchall()
    chat_list = []
    for room in room_data:
        message_format = f"{room[-1]} - {room[0]}: {room[1]}\n"
        chat_list.append(message_format)
    if len(chat_list):
        return ''.join(chat_list)
    else:
        return 'There is no messages yet.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
