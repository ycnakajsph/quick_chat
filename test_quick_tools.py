import unittest
import sqlite3
from quick_tools import createDb


class test_creation_delete_bdd(unittest.TestCase):

	def setUp(self):
		#Création de BDD
		self.db_path = 'quick_chat.db'
		self.connect = sqlite3.connect(self.db_path)
		self.cursor = self.connect.cursor()

	def test_createDb(self):
		createDb(self.db_path)
		sql = "SELECT name FROM sqlite_master WHERE type='table';"
		#print(self.cursor.execute(sql).fetchall())
		self.assertEqual(self.cursor.execute(sql).fetchall(), [('Room',), ('User',), ('Message',)])

if __name__ == '__main__':
    unittest.main()
