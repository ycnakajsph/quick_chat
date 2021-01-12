import sqlite3
import unittest
import os
from quick_tools import *


class TestToolsMethods(unittest.TestCase):

	def setUp(self):
		# Db creation :
		self.db_path = 'quick_chat.db'
		create_db(self.db_path)
	# Test verification du type de la room	
	def testVerifyRoomtype(self):
		# Test mauvaise entrée
		self.assertFalse(verifyRoomType('no public'))
		self.assertFalse(verifyRoomType('publique'))
		# Test entrée correct
		self.assertTrue(verifyRoomType('public'))
		self.assertTrue(verifyRoomType('private'))
	
	def tearDown(self):
		# Db remove :
		os.remove("quick_chat.db")

if __name__ == '__main__':

	unittest.main()
