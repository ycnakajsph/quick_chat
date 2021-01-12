import unittest
import quick_tools
import os
import sqlite3


db_path = 'quick_chat.db'

class TestQuickTools(unittest.TestCase):

    def test_create_db(self):
        files = os.listdir()
        self.assertTrue(db_path in files)

    def test_add_user(self):
        quick_tools.add_user('quick_chat.db','yann.c',0,0,'password')
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        sql = 'SELECT user_name FROM Users WHERE user_name="yann.c" AND user_role=0 AND user_rights=0 AND user_password="password";'
        self.assertEqual('yann.c', cursor.execute(sql ).fetchone()[0])

    def test_add_room(self) :
        quick_tools.add_room('quick_chat.db', 'room1', 'chat')

        connect = sqlite3.connect('quick_chat.db')
        cursor = connect.cursor()
        room =  cursor.execute("select room_name from rooms where room_name = 'room1'").fetchall()

        self.assertEqual(room, [('room1',)])

    def test_get_users(self):
        self.assertEqual(quick_tools.get_users(db_path), ['yann.c'])

    def test_delete_room(self) :
        quick_tools.add_room(db_path, "room_test", "discussion")
        quick_tools.delete_room(db_path, "room_test")
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        sql = 'SELECT room_name FROM Rooms WHERE room_name="room_test";'
        self.assertEqual([], cursor.execute(sql).fetchall())
        
	#test ajout d'un username correct
	def test_add_user_name_ok(self):
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()

        # 'Ludollaoo' est correct
        quick_tools.add_user(db_path, 'Ludollaoo', 0, 0, 'password1!')

        sql = 'SELECT user_name FROM Users;'

        users = cursor.execute(sql).fetchall()
        self.assertTrue(('Ludollaoo',) in users)

if __name__ == '__main__':
    unittest.main()
    #TestQuickTools.test_delete_room()
