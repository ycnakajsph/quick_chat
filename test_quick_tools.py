import unittest, os, sys,sqlite3, random, string
from quick_tools import create_db, add_user, add_room, get_users, get_rooms,delete_user,delete_room, verify_room_type,verify_room_name,verify_user_password


db_path = 'quick_chat.db'


conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
c = conn.cursor()


class QuickToolsTester(unittest.TestCase):
	
	def test1_create_db(self):
		c.execute('DROP TABLE IF EXISTS Rooms;')
		c.execute('DROP TABLE IF EXISTS Users;')
		create_db(db_path)
		sql = "select * from Users;"
		table_name = ''
		for row in c.execute(sql).fetchall():
			table_name = row[0]
		self.assertEqual(table_name,'')

		sql = "select * from Rooms;"
		table_name = ''
		for row in c.execute(sql).fetchall():
			table_name = row[0]
		self.assertEqual(table_name,'')

	def test2_verify_user_password(self):

		self.assertFalse(verify_room_name('qwer')) # not long enough
		self.assertFalse(verify_room_name('qwer123456')) # no special character

		random_str_len = random.randint(5,10)
		
		correct_password = ''.join(random.choice(string.ascii_lowercase) for i in range(random_str_len))
		correct_password += '123456,'

		self.assertTrue(verify_user_password(correct_password))

	def test3_add_user(self):
		add_user(db_path,'yann.c',0,0,'qwer123456,')  # add a correct user
		sql = "select user_name from Users where user_name = 'yann.c';"
		user_name = ''
		for row in c.execute(sql):
			user_name = row[0]
		self.assertEqual(user_name,'yann.c')

		add_user(db_path,'huiling.b',0,0,'pass')  # add a user with wrong password format
		sql = "select user_name from Users where user_name = 'huiling.b';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'')

	def test4_get_users(self):

		self.assertEqual(get_users(db_path),['yann.c'])  # Have to be able to get the user added

	def test5_delete_user(self):

		delete_user(db_path,'yann.c')
		sql = "select user_name from Users where user_name = 'yann.c';"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')  # Successful delete the user 

	def test6_verify_room_name(self):

		self.assertFalse(verify_room_name('false')) 
		self.assertFalse(verify_room_name('ROOM_')) 

		random_str_len = random.randint(3,20)
		correct_room = 'ROOM_'
		correct_room += ''.join(random.choice(string.ascii_lowercase) for i in range(random_str_len))

		self.assertTrue(verify_room_name(correct_room))

	def test7_verify_room_type(self):
		self.assertFalse(verify_room_type('false_type')) 
		self.assertTrue(verify_room_type('public'))
		self.assertTrue(verify_room_type('private'))
		
	def test8_add_room(self):

		add_room(db_path,'ROOM_dinningroom','public') # correct room 
		sql = "select room_name from Rooms where room_name = 'ROOM_dinningroom';"
		for row in c.execute(sql):
			room_name = row[0]
		self.assertEqual(room_name,'ROOM_dinningroom')

		add_room(db_path,'ROOM_bedroom','unknown') # wrong room type
		sql = "select room_name from Rooms where room_name = 'ROOM_bedroom';"
		res = ''
		for row in c.execute(sql):
			res = row[0]
		self.assertEqual(res,'')

		add_room(db_path,'ROOM_no','private') # wrong room name
		sql = "select room_name from Rooms where room_name = 'ROOM_no';"
		res = ''
		for row in c.execute(sql):
			res = row[0]
		self.assertEqual(res,'')


	def test9_get_rooms(self):

		self.assertEqual(get_rooms(db_path),['ROOM_dinningroom'])

	def test10_delete_room(self):
		delete_room(db_path,'ROOM_dinningroom')
		sql = "select room_name from Rooms where room_name = 'ROOM_dinningroom';"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')
	


if __name__ == '__main__':
	unittest.main()
	conn.commit()
	conn.close()

# add_room('quick_chat.db','room0','public')

# print(get_users(db_path))
# print(get_rooms(db_path))