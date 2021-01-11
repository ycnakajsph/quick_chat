import unittest
from quick_tools import verify_user_passwd
from quick_tools import verify_room_type
import sqlite3
import quick_tools as tool

class QuickToolsTester(unittest.TestCase):

	def setUp(self):
        #Creation de BDD
        self.db_path = 'test_chat.db'
        self.connect = sqlite3.connect(self.db_path)
        self.cursor = self.connect.cursor()
        tool.create_db(self.db_path)

    def tearDown(self):
        #Suppression de BDD
        tool.delete_db(self.db_path)

	def test_verify_user_passwd(self):
		#User_password : > 8 chars, inclut nombres et au moins un caractère special

		self.assertFalse(verify_user_passwd('aout')) #Trop court
		self.assertFalse(verify_user_passwd('moisdaout')) #Pas de chiffres
		self.assertFalse(verify_user_passwd('29aout1997')) #Pas de caracteres speciaux

		self.assertTrue(verify_user_passwd('29_aout_1997')) #Mot de passe correct


	def test_verify_room_type(self):
		#Room_type : 'public' ou 'private'

		#Noms incorrects
		self.assertFalse(verify_room_type('pablic'))
		self.assertFalse(verify_room_type('poblic'))
		self.assertFalse(verify_room_type('piblic'))
		self.assertFalse(verify_room_type('peblic'))
		self.assertFalse(verify_room_type('pyblic'))
		self.assertFalse(verify_room_type('pravate'))
		self.assertFalse(verify_room_type('provate'))
		self.assertFalse(verify_room_type('pryvate'))

		#Majuscules non autorisées
		self.assertFalse(verify_room_type('PRIVATE'))
		self.assertFalse(verify_room_type('PUBLIC'))

		self.assertTrue(verify_room_type('public')) # 'public', nom correct
		self.assertTrue(verify_room_type('private')) # 'private', nom correct

	def test_verify_username(self):
		#L'username doit être unique et ne doit comporter aucun chiffre ou
		#symbole

		#Ajout de données
		tool.add_user(self.db_path,'hunk',0,0,'26_juin_1946')
		tool.add_user(self.db_path,'zeke',0,0,'26_juin_1946')
		tool.add_user(self.db_path,'hickory',0,0,'26_juin_1946')

		#Unicité du username
		self.assertFalse(verify_username(self.dbpath, 'hunk'))
		self.assertFalse(verify_username(self.dbpath, 'zeke'))
		self.assertFalse(verify_username(self.dbpath, 'hickory'))

		#Verification des chiffres et symboles
		self.assertFalse(verify_username(self.dbpath, 'z3k3'))
		self.assertFalse(verify_username(self.dbpath, '/HuNk/'))
		self.assertFalse(verify_username(self.dbpath, '_h|ck0ry_'))

		#Usernames corrects
		self.assertTrue(verify_username(self.dbpath, 'dorothy'))
		self.assertTrue(verify_username(self.dbpath, 'witch'))
		self.assertTrue(verify_username(self.dbpath, 'oz'))


if __name__ == '__main__':
	unittest.main()
