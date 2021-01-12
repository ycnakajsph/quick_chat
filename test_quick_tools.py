import unittest
import sqlite3
from quick_tools import verify_user_name
import random
import string

class QuickToolsTester(unittest.TestCase):

	def test_verify_user_name(self):

		db_path = 'quick_chat.db'

		str_lett = string.ascii_letters
		test_str = ''.join(random.choice(str_lett) for _ in range(random.randint(2,6)))
		self.assertTrue(verify_user_name(test_str, db_path))

		str_chif = string.digits
		test_str = ''.join(random.choice(str_chif) for _ in range(random.randint(2,6)))
		self.assertFalse(verify_user_name(test_str, db_path))

		str_symb = string.punctuation
		test_str = ''.join(random.choice(str_symb) for _ in range(random.randint(2,6)))
		self.assertFalse(verify_user_name(test_str, db_path))

		self.assertFalse(verify_user_name('yann.c', db_path)) # Déjà présent dans BDD

if __name__ == '__main__':
    unittest.main()
