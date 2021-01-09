import sqlite3

def get_rooms(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT room_name FROM Rooms;'

	rooms = cursor.execute(sql ).fetchall()

	rooms = [room[0] for room in rooms]

	return rooms

def verify_room(room_type):
	if room_type == 'public' or room_type == 'private':
		return True
	return False

def add_room(db_path, room_name, room_type):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	#if room_type == 'public' or room_type == 'private':
	if verify_room(room_type) :
		sql = 'INSERT INTO Rooms (room_name,room_type) VALUES (?,?)'

		cursor.execute(sql,(room_name, room_type))
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

def verify_password(user_password):
	have_number = 0
	have_special = 0
	for i in user_password:
		if i.isdigit():
			have_number = 1
		if (not i.isdigit()) and (not i.isupper())  and (not i.islower()):
			have_special = 1

	if len(user_password)>8 and have_number ==1 and have_special ==1:
		return True
	return False

def add_user(db_path, user_name, user_role, user_rights, user_password):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	"""
	have_number = 0
	have_special = 0
	for i in user_password:
		if i.isdigit():
			have_number = 1
		if (not i.isdigit()) and (not i.isupper())  and (not i.islower()):
			have_special = 1

	if len(user_password)>8 and have_number ==1 and have_special ==1:
	"""
	if verify_password(user_password):
		sql = 'INSERT INTO Users (user_name, user_role, user_rights, user_password) VALUES (?,?,?,?)'

		cursor.execute(sql,(user_name, user_role, user_rights, user_password))
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

