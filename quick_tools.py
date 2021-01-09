import sqlite3
from string import punctuation 

def get_rooms(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT room_name FROM Rooms;'

	rooms = cursor.execute(sql ).fetchall()

	rooms = [room[0] for room in rooms]

	return rooms


def verify_room_name(room_name):
	if room_name.startswith('ROOM_'):
		if len(room_name) >= 8 :
			return True
	return False

def verify_room_type(room_name): # TODO incomplete definition 
	return room_name == 'public' or room_name == 'private' 
	
def verify_password_length(user_password):
	if len(user_password) >=8:
		return True 
	return False 
	
def verify_password_number(user_password):
	number = set('0123456789')
	if any((c in number) for c in user_password):
    		return True
	else:
    		return False 
	
def verify_password_special(user_password):
	special = set(punctuation)
	if any((c in special) for c in user_password):
    		return True
	else:
    		return False 
	
def verify_password_total(user_password):
	return verify_password_length(user_password) and verify_password_number(user_password) and verify_password_special(user_password)

def add_room(db_path, room_name, room_type):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'INSERT INTO Rooms (room_name,room_type) VALUES (?,?)'

	cursor.execute(sql,(room_name, room_type))
	connect.commit()


def verify_add_room(db_path, room_name, room_type):
	if verify_room_name(room_name) and verify_room_type(room_type) :
		add_room(db_path, room_name, room_type) 
	else :
		raise NameError('Wrong room parameters')
		
	
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

	sql = 'INSERT INTO Users (user_name, user_role, user_rights, user_password) VALUES (?,?,?,?)'

	cursor.execute(sql,(user_name, user_role, user_rights, user_password))
	connect.commit()
	
def verify_add_user(db_path, user_name, user_role, user_rights, user_password):
	if verify_password_total(user_password) :
		add_user(db_path, user_name, user_role, user_rights, user_password)
	else :
		raise NameError('Wrong user parameters')
		
def delete_user(db_path, user_name):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'DELETE FROM Users WHERE user_name=?'

	cursor.execute(sql,(user_name,))
	connect.commit()

def create_db(db_path):
	connect = sqlite3.connect(db_path)

	cursor = connect.cursor()
	
	cursor.execute('DROP TABLE IF EXISTS Rooms') # To avoid OperationalError: table Rooms already exists
	cursor.execute('DROP TABLE IF EXISTS Users')
	
	cursor.execute('CREATE TABLE Rooms ([id_room] INTEGER PRIMARY KEY,[room_name] text UNIQUE, [room_type] text)')
	cursor.execute('CREATE TABLE Users ([id_user] INTEGER PRIMARY KEY,[user_name] text UNIQUE, [user_role] integer, [user_rights] integer, [user_password] text)')

	connect.commit()

#Db creation :
#db_path = 'quick_chat.db'

#create_db(db_path)
#add_user('quick_chat.db','yann.c',0,0,'password')
#add_room('quick_chat.db','room0','public')

#print(get_users(db_path))
#print(get_rooms(db_path))
#delete_user(db_path,'yann.c')
