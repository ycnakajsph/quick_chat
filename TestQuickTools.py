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



    # Adding a user_name that suits the specifications
    def test_add_user_name_ok(self):
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        # 'Username' should be a correct user_name
        quick_tools.add_user(db_path, 'Username', 0, 0, 'password1!')

        sql = 'SELECT user_name FROM Users;'

        users = cursor.execute(sql).fetchall()
        self.assertTrue(('Username',) in users)


    # Adding a user_name that does not suit the specifications
    def test_add_user_name_ko(self):
        # 'Username98' has a number in it
        with self.assertRaises(Exception):
            quick_tools.add_user(db_path, 'Username98', 0, 0, 'password1!')

        # 'Username!' has a special character in it
        with self.assertRaises(Exception):
            quick_tools.add_user(db_path, 'Username!', 0, 0, 'password1!')

        # 'my_username' is not unique
        with self.assertRaises(Exception):
            quick_tools.add_user(db_path, 'my_username', 0, 0, 'password1!')
            quick_tools.add_user(db_path, 'my_username', 0, 0, 'password1!')
            



if __name__ == '__main__':
    unittest.main()
