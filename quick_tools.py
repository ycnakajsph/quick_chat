import sqlite3

def get_rooms(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT room_name FROM Rooms;'

	rooms = cursor.execute(sql ).fetchall()

	rooms = [room[0] for room in rooms]

	return rooms

def verify_room_name(room_name):
	# Extra requirement: room_name start with ROOM_ and length >=8
	if room_name.startswith('ROOM_'):
		if len(room_name) >= 8 :
			return True
	return False

def verify_room_type(room_type):
	# Extra requirement: room_type has to be public or private
	if room_type == 'public' or room_type == 'private':
		return True
	return False

def add_room(db_path, room_name, room_type):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	if verify_room_type(room_type) and verify_room_name(room_name):

		sql = 'INSERT INTO Rooms (room_name,room_type) VALUES (?,?)'
		cursor.execute(sql,(room_name, room_type))

	else:
		print("\nRooms ERROR: \n room_type has to be 'public' or 'private'\nroom_name has to start with ROOM_ and length>=8\n")

	connect.commit()


def delete_room(db_path, room_name):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'DELETE FROM Rooms WHERE room_name=?'

	cursor.execute(sql,(room_name,))
	connect.commit()


def get_users(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT user_name FROM Users;'

	users = cursor.execute(sql ).fetchall()

	users = [user[0] for user in users]

	return users

def verify_user_password(user_password):
	# Extra requirement: check the password have number,special character, length>8 
	is_number = 0
	special_character = 0

	for i in user_password:
		if i.isdigit():
			is_number = 1

		if (not i.islower()) and (not i.isupper())  and (not i.isdigit()):
			special_character = 1

	if len(user_password)>=8:
		if is_number and special_character:
			return True
		
	return False

	
def add_user(db_path, user_name, user_role, user_rights, user_password):

	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	
	
	if verify_user_password(user_password):
		sql = 'INSERT INTO Users (user_name, user_role, user_rights, user_password) VALUES (?,?,?,?)'
		cursor.execute(sql,(user_name, user_role, user_rights, user_password))

	else:
		print("\nUsers ERROR: password should > 8 chars, includes numbers and special character")
	
	connect.commit()


def delete_user(db_path, user_name):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'DELETE FROM Users WHERE user_name=?'

	cursor.execute(sql,(user_name,))
	connect.commit()

def create_db(db_path):
	connect = sqlite3.connect(db_path)

	cursor = connect.cursor()

	cursor.execute('CREATE TABLE Rooms ([id_room] INTEGER PRIMARY KEY,[room_name] text UNIQUE, [room_type] text)')
	cursor.execute('CREATE TABLE Users ([id_user] INTEGER PRIMARY KEY,[user_name] text UNIQUE, [user_role] integer, [user_rights] integer, [user_password] text)')

	connect.commit()

# Db creation :
# db_path = 'quick_chat.db'

# create_db(db_path)

# add_user('quick_chat.db','yann.c',0,0,'password')
# add_room('quick_chat.db','room0','public')

# print(get_users(db_path))
# print(get_rooms(db_path))
# delete_user(db_path,'yann.c')