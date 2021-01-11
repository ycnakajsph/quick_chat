import unittest
from quick_tools import verify_user_name
import random
import string

class QuickToolsTester(unittest.TestCase):

	def test_verify_user_name(self):

		db_path = 'quick_chat.db'

		str_lett = string.ascii_letters
		test_str = ''.join(random.choice(str_lett) for _ in range(random.randint(2,6)))
		self.assertTrue(verify_user_name(test_str))

		str_chif = string.digits
		test_str = ''.join(random.choice(str_chif) for _ in range(random.randint(2,6)))
		self.assertFalse(verify_user_name(test_str))

		str_symb = string.punctuation
		test_str = ''.join(random.choice(str_symb) for _ in range(random.randint(2,6)))
		self.assertFalse(verify_user_name(test_str))

		try:
			connect = sqlite3.connect(db_path)
			cursor = connect.cursor()
			sql = 'INSERT INTO Users (user_name) VALUES ("username")'
			cursor.execute(sql)
			cursor.execute(sql)
		except IntegrityError: # exception sql
			self.assertTrue(verify_user_name('username'))
		else:
			self.assertFalse(verify_user_name('username'))
		finally:
			cursor.close() # close sans commit pour ne pas enregistrer 'username'
