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

	def test_verify_room_type(self):

		self.assertFalse(verify_room_type('undefined')) # Isn't "private" or "public"
		self.assertTrue(verify_room_type('public'))
		self.assertTrue(verify_room_type('private'))


	def test_verify_user_password(self):

		self.assertFalse(verify_user_password('PASS94?')) 		# Isn't long enough
		self.assertFalse(verify_user_password('PASSword?'))		#Number missing
		self.assertFalse(verify_user_password('PASSword94'))	#Special character missing
		self.assertFalse(verify_user_password('Pass'))		#Isn't long enough, number AND special character missing
		self.assertTrue(verify_user_password('PASSwoRD94?'))
