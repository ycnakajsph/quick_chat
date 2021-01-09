import unittest
import quick_tools
import os
import sqlite3


db_path = 'quick_chat.db'

class TestQuickTools(unittest.TestCase):

    def test_add_room_type(self):
        # 'custom' is not 'public' or 'private'
        with self.assertRaises(Exception):
            quick_tools.add_room(db_path,'room0','custom')

            

    def test_add_user_password(self):
        # 'password1' has no special character
        with self.assertRaises(Exception):
            quick_tools.add_user(db_path,'testNom',0,0,'password1')

        # 'pass' is less than 8 characters long
        with self.assertRaises(Exception):
            quick_tools.add_user(db_path,'testNom',0,0,'pass')

        # 'password!?' has no number in it
        with self.assertRaises(Exception):
            quick_tools.add_user(db_path,'testNom',0,0,'password!?')



if __name__ == '__main__':
    unittest.main()
