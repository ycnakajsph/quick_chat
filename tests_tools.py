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
	
	# Test verification password
	def testPasswordLenght(self):
		# Test bon password
		self.assertTrue(verifyPassword('password1!'))
		# Test password trop petit
		self.assertFalse(verifyPassword('123*'))
		# Test password égal à 8
		self.assertFalse(verifyPassword('1234567/'))

	def testPasswordSyntax(self):
		# Test password sans chiffre	
		self.assertFalse(verifyPassword('password!'))
		# Test password sans symbole	
		self.assertFalse(verifyPassword('password1'))
		# Test password sans aucun des 2	
		self.assertFalse(verifyPassword('passwordbon'))
				
	def tearDown(self):
		# Db remove :
		os.remove("quick_chat.db")

if __name__ == '__main__':

	unittest.main()
