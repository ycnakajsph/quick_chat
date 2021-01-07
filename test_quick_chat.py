import unittest
from quick_tools import verify_room_name
import random

class QuickToolsTester(unittest.TestCase):

	def test_verify_room_name(self):

		self.assertFalse(verify_room_name('whatever')) # Doesn't start with ROOM_
		self.assertFalse(verify_room_name('ROOM_')) # starts with ROOM_ but isn't long enough


		self.assertTrue(verify_room_name('ROOM_12345')) # correct Room number

