import unittest, os, sys,sqlite3,time
import random
import string
from code import create_db, add_user, add_room, get_users, get_rooms,delete_user,delete_room,verify_room,verify_password,verify_username


conn = sqlite3.connect('quick_chat.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

db_path = 'quick_chat.db'

class TestDB(unittest.TestCase):
	def test_A_init(self):
		c.execute('DROP TABLE IF EXISTS Rooms;')
		c.execute('DROP TABLE IF EXISTS Users;')
		#os.remove(db_path)
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
 
	def test_B_add_user(self):
		add_user(db_path,'yann.c',0,0,'password')
		sql = "select user_name from Users where user_name = 'yann.c';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'')

		add_user(db_path,'yann.c',0,0,'password0')
		sql = "select user_name from Users where user_name = 'yann.c';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'')

		add_user(db_path,'yann.c',0,0,'password.')
		sql = "select user_name from Users where user_name = 'yann.c';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'')


		add_user(db_path,'yann.c',0,0,'password0.')
		sql = "select user_name from Users where user_name = 'yann.c';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'yann.c')

	def test_C_get_users(self):
		self.assertEqual(get_users(db_path),['yann.c'])

	def test_D_delete_user(self):
		delete_user(db_path,'yann.c')
		sql = "select user_name from Users where user_name = 'yann.c';"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')
	

	def test_E_add_room(self):


		add_room(db_path,'room1','public')
		sql = "select room_name from Rooms where room_name = 'room1';"
		for row in c.execute(sql):
			room_name = row[0]
		self.assertEqual(room_name,'room1')

		add_room(db_path,'room0','unknown')
		sql = "select room_name from Rooms where room_name = 'room0';"
		res = ''
		for row in c.execute(sql):
			res = row[0]
		self.assertEqual(res,'')



	def test_F_get_rooms(self):
		self.assertEqual(get_rooms(db_path),['room1'])

	def test_G_delete_room(self):
		delete_room(db_path,'room1')
		sql = "select room_name from Rooms where room_name = 'room1';"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')
	def test_H_verify_room(self):
		self.assertTrue(verify_room('public')) 
		self.assertTrue(verify_room('private')) 

		random_str_len = random.randint(1,10)
		name_room = ''
		name_room += ''.join(random.choice(string.ascii_lowercase) for i in range(random_str_len))

		self.assertFalse(verify_room(name_room))

	def test_I_verify_password(self):
		rightpwd1 = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], random.randint(4,7)))
		rightpwd1 += ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9'],random.randint(4,7)))
		rightpwd1 += ''.join(random.sample(['!','-','*','[',']','=','+','-','(',')'],random.randint(1,3)))

		rightpwd2 = ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9'],random.randint(8,10)))
		rightpwd2 += ''.join(random.sample(['!','-','*','[',']','=','+','-','(',')'],random.randint(1,3)))

		self.assertTrue(verify_password(rightpwd1)) 
		self.assertTrue(verify_password(rightpwd2)) 

		wrongpwd1 = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 9))
		wrongpwd2 = ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9'],6))
		wrongpwd2 += ''.join(random.sample(['!','-','*','[',']','=','+','-','(',')'],1))
		self.assertFalse(verify_password(wrongpwd1)) 
		self.assertFalse(verify_password(wrongpwd2)) 

	def test_J_verify_username(self):
		sql = "INSERT INTO Users (user_name, user_role, user_rights, user_password) VALUES (\"liu\",0,0,\"password\")"
		c.execute(sql)
		# c.execute('INSERT INTO Users (user_name, user_role, user_rights, user_password) VALUES ("liu",0,0,"password")')
		random_str_len = random.randint(5,10)
		wrongname1 = 'liu'

		wrongname2 = ''.join(random.choice(string.ascii_lowercase) for i in range(random_str_len))
		wrongname2 += ''.join(random.sample(['!','-','*','[',']','=','+','-','(',')'],2))

		wrongname3 = ''.join(random.choice(string.ascii_lowercase) for i in range(random_str_len))
		wrongname3 += ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9'],2))

		rightname1 = 'wang'
		rightname2 = 'Wang'

		self.assertFalse(verify_username(db_path,wrongname1)) 
		self.assertFalse(verify_username(db_path,wrongname2))
		self.assertFalse(verify_username(db_path,wrongname3)) 
		self.assertTrue(verify_username(db_path,rightname1))
		self.assertTrue(verify_username(db_path,rightname2)) 

		c.execute('DELETE FROM Users WHERE user_name="liu"')
if __name__ == '__main__':
	unittest.main()
	conn.commit()
	conn.close()

# add_room('quick_chat.db','room0','public')

# print(get_users(db_path))
# print(get_rooms(db_path))
