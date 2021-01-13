import unittest
from quick_tools import *
import random
import string

class QuickToolsTester(unittest.TestCase):

	def test_verify_room_name(self):

		self.assertFalse(verify_room_name('whatever')) # Doesn't start with ROOM_
		self.assertFalse(verify_room_name('ROOM_')) # starts with ROOM_ but isn't long enough

		# kindly stolen and adapted from : https://pynative.com/python-generate-random-string/
		random_str_len = random.randint(3,20)
		correct_room = 'ROOM_'
		correct_room += ''.join(random.choice(string.ascii_lowercase) for i in range(random_str_len))

		self.assertTrue(verify_room_name(correct_room))

	def test_verify_username(self):

		db_path = 'quick_chat.db'


		self.assertFalse(verify_username(db_path, 'USER94?')) 	#Special character and number
		self.assertFalse(verify_username(db_path, 'USERword?'))	#Special character
		self.assertFalse(verify_username(db_path, 'USERword94'))	#Number

		# We add a username, and test the uniqueness

		delete_user(db_path,'MervisMudry') #On supprime l'élement à chaque lancement de la fonction, pour que l'ajout ensuie se passe sans problème
		add_user('quick_chat.db','MervisMudry',0,0,'password')


		# users = get_users(db_path)
		# print(users)

		self.assertFalse(verify_username(db_path, 'MervisMudry'))

		self.assertTrue(verify_username(db_path, 'USERname'))
