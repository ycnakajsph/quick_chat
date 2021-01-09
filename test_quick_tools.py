import unittest, os, sys,sqlite3, random, string
from quick_tools import create_db, add_user, add_room, get_users, get_rooms,delete_user,delete_room, verify_room_type,verify_room_name,verify_user_password


db_path = 'quick_chat.db'


conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
c = conn.cursor()


class QuickToolsTester(unittest.TestCase):
	
	def test1_create_db(self):
		
	def test2_verify_user_password(self):

	def test3_add_user(self):
		
	def test4_get_users(self):

	def test5_delete_user(self):

	def test6_verify_room_name(self):

	def test7_verify_room_type(self):
		
	def test8_add_room(self):

	def test9_get_rooms(self):

	def test10_delete_room(self):
		




if __name__ == '__main__':
	unittest.main()
	conn.commit()
	conn.close()

# add_room('quick_chat.db','room0','public')

# print(get_users(db_path))
# print(get_rooms(db_path))