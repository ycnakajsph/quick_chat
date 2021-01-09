import unittest
from quick_tools import verify_room_type
import random

class QuickToolsTester(unittest.TestCase):

	def test_verify_room_type(self):

		self.assertFalse(verify_room_type('')) # Not private or public
		self.assertFalse(verify_room_type('azerty')) # Not private or public
		self.assertTrue(verify_room_name('private')) # is private
		self.assertTrue(verify_room_name('public')) # is public
