import sqlite3
import re

def get_rooms(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT room_name FROM Rooms;'

	rooms = cursor.execute(sql ).fetchall()

	rooms = [room[0] for room in rooms]

	return rooms

def verifyRoomType(room_type):
	if (room_type != 'public') and (room_type != 'private'):
		print("La room ne peut être que 'public' ou 'private'")
		return False
	return True

def add_room(db_path, room_name, room_type):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

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

def verifyPassword(password):
	
	if len(password) <= 8:
		print("Error ! Mdp trop court")
		return False

	chiffres = '0123456789'	
	if not any(c in chiffres for c in password):
		print("Error ! Pas de chiffre") 
		return False

	caracteresSpeciaux = '[\'*!?#$%&*+-.^_|~:$]'
	if not any(c in caracteresSpeciaux for c in password):
		print("Error ! pas de caractére spécial")	
		return False
	return True

def add_user(db_path, user_name, user_role, user_rights, user_password):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
    
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

# Db creation :
# db_path = 'quick_chat.db'

# create_db(db_path)

# add_user('quick_chat.db','yann.c',0,0,'password')
# add_room('quick_chat.db','room0','public')

# print(get_users(db_path))
# print(get_rooms(db_path))
# delete_user(db_path,'yann.c')
