import sqlite3

def verify_room_type(room_type):
	# Extra requirement: room_type is 'public' or 'private'
	if room_type == 'public' or room_type == 'private':
		return True;
	return False

def verify_user_password(user_password):
	# Extra requirement: user_password is > 8 chars, includes numbers and at least a special character
	has_number = False
	has_special_character = False

	for c in user_password:
		if c.isdigit():
			has_number = True
		if (not c.islower()) and (not c.isupper())  and (not c.isdigit()):
			has_special_character = True

	if len(user_password) > 8 and has_number and has_special_character:
		return True
	return False

def verify_user_name(user_name):
	# Extra requirement: user_name has to be unique and cannot have number or special character
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	has_number = False
	has_special_character = False

	for c in user_name:
		if c.isdigit():
			has_number = True
		if (not c.islower()) and (not c.isupper())  and (not c.isdigit()):
			has_special_character = True

	if (not has_number) and (not has_special_character):
		sql = 'SELECT user_name FROM Users;'
		user_names = cursor.execute(sql).fetchall()
		if user_name not in user_names:
			return True

	return False

def get_rooms(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT room_name FROM Rooms;'

	rooms = cursor.execute(sql ).fetchall()

	rooms = [room[0] for room in rooms]

	return rooms


def add_room(db_path, room_name, room_type):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'INSERT INTO Rooms (room_name,room_type) VALUES (?,?)'

	cursor.execute(sql,(room_name, room_type))
	connect.commit()


def delete_room(db_path, room_name):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	if verify_room_type(room_type):
		sql = 'DELETE FROM Rooms WHERE room_name=?'

		cursor.execute(sql,(room_name, room_type))
		connect.commit()
	else:
		print('ERROR in Rooms: room_type must be \'public\' or \'private\'')


def get_users(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT user_name FROM Users;'

	users = cursor.execute(sql ).fetchall()

	users = [user[0] for user in users]

	return users


def add_user(db_path, user_name, user_role, user_rights, user_password):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	if verify_user_password(user_password) and verify_user_name(user_name):
		sql = 'INSERT INTO Users (user_name, user_role, user_rights, user_password) VALUES (?,?,?,?)'

		cursor.execute(sql,(user_name, user_role, user_rights, user_password))
		connect.commit()
	else:
		print('ERROR in Users: user_name must be unique without numbers and special characters')
		print('ERROR in Users: user_password must have at least 8 characters with numbers and special characters')

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
db_path = 'quick_chat.db'

create_db(db_path)

add_user('quick_chat.db','yann.c',0,0,'password')
add_room('quick_chat.db','room0','public')

print(get_users(db_path))
print(get_rooms(db_path))
delete_user(db_path,'yann.c')