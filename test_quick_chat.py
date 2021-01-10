import unittest
from quick_tools import verify_user_passwd
from quick_tools import verify_room_type

class QuickToolsTester(unittest.TestCase):

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

if __name__ == '__main__':
	unittest.main()
