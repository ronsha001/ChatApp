import json     
    
# db_path = 'database/rooms.json'

# with open(db_path, 'r') as f:
#     rooms = json.load(f)

#     print(rooms['room1'])

db_path = 'database/rooms.json'
    
msg = "new msg\n"
rooms_data = ''

with open(db_path, 'r') as f:
    rooms_data = json.load(f)
    print(rooms_data['room1'])

with open(db_path, 'w') as f:
    if ('room2' not in rooms_data):
        rooms_data['room2'] = []

    rooms_data['room2'].append(msg+"\n")
    json.dump(rooms_data, f)

