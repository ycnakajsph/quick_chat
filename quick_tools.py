import sqlite3
import re

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

	try:
		is_room_type_ok(room_type)
	except Exception as error:
		print(error)
		return

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


def add_user(db_path, user_name, user_role, user_rights, user_password):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	try:
		is_user_password_ok(user_password)
		is_user_name_ok(user_name)
	except Exception as error:
		print(error)
		return

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

	cursor.execute('DROP TABLE IF EXISTS Rooms')
	cursor.execute('DROP TABLE IF EXISTS Users')

	cursor.execute('CREATE TABLE Rooms ([id_room] INTEGER PRIMARY KEY,[room_name] text UNIQUE, [room_type] text)')
	cursor.execute('CREATE TABLE Users ([id_user] INTEGER PRIMARY KEY,[user_name] text UNIQUE, [user_role] integer, [user_rights] integer, [user_password] text)')

	connect.commit()

def is_room_type_ok(room_type):
	if not (room_type == 'public' or room_type == 'private'):
		raise Exception('**Error : Room_type can only be \'public\' or \'private\'')

def is_user_password_ok(user_password):
	if (len(user_password) < 8) or (len(re.findall('\d', user_password)) == 0) or (len(re.findall('\W', user_password)) == 0):
		raise Exception('**Error : User password is > 8 chars, includes numbers and at least a special character')


def is_user_name_ok(user_name):
	if (len(re.findall('\d', user_name)) != 0) or (len(re.findall('\W', user_name)) != 0):
		raise Exception('**Error : Username cannot contain numbers or non-alphanumeric characters')

	if user_name in get_users(db_path):
		raise Exception('**Error : Username has to be unique')


# Db creation :
db_path = 'quick_chat.db'

create_db(db_path)

add_user(db_path,'testNom',0,0,'password1!')
add_room(db_path,'room0','public')
#add_room(db_path,'room1','test')					# Not added beacause of wrong room_type
#add_user(db_path,'badName26',0,0,'password1!') 	# Not added beacause of wrong room_name
#add_user(db_path,'goodName',0,0,'badPassword')		# Not added beacause of wrong room_password

print(get_users(db_path))
print(get_rooms(db_path))
#delete_user(db_path,'yann.c')
