import unittest
import quick_tools
import os
import sqlite3


db_path = 'quick_chat.db'

class TestQuickTools(unittest.TestCase):

	#ajout d'un nom d'utilisateur correct
	def test_add_user_ok(self):
		connect = sqlite3.connect(db_path)
		cursor = connect.cursor()
		
		#'Ludollaoo' est un username correct
		quick_tools.add_user(db_path, 'Ludollaoo', 0, 0, 'password')
		
		sql = 'SELECT user_name FROM Users;'
		users = cursor.execute(sql).fetchall()
		self.assertTrue(('Ludollaoo',) in users)
	
	#ajout d'un nom d'utilisateur incorrect : nombre
	def test_add_user_ko_nombre(self):
		connect = sqlite3.connect(db_path)
		cursor = connect.cursor()
		
		#'Ludollaoo1' est un username incorrect
		quick_tools.add_user(db_path, 'Ludollaoo1', 0, 0, 'password')
		
		sql = 'SELECT user_name FROM Users;'
		users = cursor.execute(sql).fetchall()
		self.assertFalse(('Ludollaoo1',) in users)
		
	#ajout d'un nom d'utilisateur incorrect : caractère spécial
	def test_add_user_ko_caractere_special(self):
		connect = sqlite3.connect(db_path)
		cursor = connect.cursor()
		
		#'Ludollaoo!' est un username incorrect
		quick_tools.add_user(db_path, 'Ludollaoo!', 0, 0, 'password')
		
		sql = 'SELECT user_name FROM Users;'
		users = cursor.execute(sql).fetchall()
		self.assertFalse(('Ludollaoo!',) in users)
	
	
		


if __name__ == '__main__':
    unittest.main()
    #TestQuickTools.test_delete_room()
