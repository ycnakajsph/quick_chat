import unittest
#import test function 
from quick_tools import verify_room_name
from quick_tools import verify_room_type 

from quick_tools import verify_password_length
from quick_tools import verify_password_number
from quick_tools import verify_password_special

from quick_tools import verify_password_total

from quick_tools import verify_add_room
from quick_tools import create_db

from quick_tools import verify_add_user
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
	
	def test_verify_room_type(self): #test room type 
	
		self.assertFalse(verify_room_type('whatever')) # ni privé ni public
		self.assertFalse(verify_room_type('publicc')) # pas tout à fait public
		self.assertFalse(verify_room_type('privat')) # pas tout à fait private
		
		
		self.assertTrue(verify_room_type('public')) # bon type public
		self.assertTrue(verify_room_type('private')) # bon type private
		
		length =  random.randint(1,10) # password is now beetween 8 and 20 char 
		letters = string.ascii_letters + string.digits # add a digiit to make sure public or private can't be the outcome
		wrong_type = ''.join(random.choice(letters) for i in range(length))
		self.assertFalse(verify_room_type(wrong_type))
		
		
	def test_verify_password_length(self):
	
		self.assertFalse(verify_password_length('coucou')) # too short
		
		# kindly stolen from : https://pynative.com/python-generate-random-string/
		length =  random.randint(8,20) # password is now beetween 8 and 20 char 
		letters = string.ascii_letters + string.digits
		result_str = ''.join(random.choice(letters) for i in range(length))
		self.assertTrue(verify_password_length(result_str)) # > 8
		
	def test_verify_password_number(self):
		
		self.assertFalse(verify_password_number('paasswoordd')) # no number
		
		has_number = 'password'
		length =  random.randint(1,5) # password is now beetween 8 and 20 char 
		letters = string.digits
		has_number += ''.join(random.choice(letters) for i in range(length))
		self.assertTrue(verify_password_number(has_number)) # number
		
	def test_verify_password_special(self):
		self.assertFalse(verify_password_special('passwoord1')) # no special char
		
		has_spec = 'password'
		length =  random.randint(1,5) # password is now beetween 8 and 20 char 
		letters = string.punctuation
		has_spec += ''.join(random.choice(letters) for i in range(length))
		self.assertTrue(verify_password_special(has_spec)) # special char
		
		
	def test_verify_password_total(self) : #test user passowrd
		self.assertFalse(verify_password_total('1234567'))#too short 
		self.assertFalse(verify_password_total('12345678'))#no special char
		self.assertFalse(verify_password_total('password+'))#no number
		self.assertFalse(verify_password_total('password7')) #no special character
		
		self.assertTrue(verify_password_total('password7!')) # >8 number and special character
		self.assertTrue(verify_password_total('7password+')) #Test different position of the required type of symboles
		self.assertTrue(verify_password_total('pass7+word')) 
		self.assertTrue(verify_password_total('7*password')) 
		
		
	def test_verify_add_room(self) :
		db_path = 'quick_chat.db'
		create_db(db_path)
		with self.assertRaises(NameError) :
			verify_add_room('quick_chat.db','room0','public') #wrong room name
			verify_add_room('quick_chat.db','ROOM_0','VIP')#wrong room type
		try:
        		verify_add_room('quick_chat.db','ROOM_000','public') #ok
		except NameError:
        		self.fail("verify_add_room raised NameError unexpectedly!")
        
	def test_verify_add_user(self) :
		db_path = 'quick_chat.db'
		create_db(db_path)
		with self.assertRaises(NameError) :
			verify_add_user('quick_chat.db','yann.c',0,0,'password')
			verify_add_user('quick_chat.db','yann.c',0,0,'pass1/')
			verify_add_user('quick_chat.db','yann.c',0,0,'password12')
			verify_add_user('quick_chat.db','yann.c',0,0,'password+')
		try:
        		verify_add_user('quick_chat.db','yann.c',0,0,'password7!')
		except NameError:
        		self.fail("verify_add_room raised NameError unexpectedly!")
        		
        	
		
if __name__ == '__main__': # main to test all the fonction 
    unittest.main()
