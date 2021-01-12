import unittest, os, unittest, sqlite3, random, string
import quick_tools

def delete_db(db_path):
    if(os.path.exists(db_path)):
        print("Destruction de la db")
        os.remove(db_path)

class testQuickChat(unittest.TestCase):

    # Apppelé au tout début des tests
    @classmethod
    def setUpClass(cls):
        # Initialisation de la db et du path
        cls.db_path = 'quick_chat_test.db'
        print("Initialise cls.db_path to quick_chat.db")
        cls.connect = sqlite3.connect(cls.db_path)
        cls.cursor = cls.connect.cursor()

        # Création de la db
        quick_tools.create_db(cls.db_path)
    
    def testPasswordVerification(self):
        # Tests sur le Password
        print("Tests \"Password Verification\"")

        # Inferieur à 8 caractères
        password = "Pass"
        self.assertTrue(not(quick_tools.verify_user_password(password)))

        # Pas de nombre/caractère spécial
        password = "Passwords"
        self.assertTrue(not(quick_tools.verify_user_password(password)))

        # Pas de lettre/caractère spéciaux
        password = "945530305"
        self.assertTrue(not(quick_tools.verify_user_password(password)))

        # Pas de lettre/nombre
        password = "§*$$µ*!_!"
        self.assertTrue(not(quick_tools.verify_user_password(password)))

        # Pas de lettre
        password = "9455§0£0!"
        self.assertTrue(not(quick_tools.verify_user_password(password)))

        # Pas de nombre
        password = "Passwo!§!"
        self.assertTrue(not(quick_tools.verify_user_password(password)))

        # Pas de caractère spécial
        password = "P4ssw0rds"
        self.assertTrue(not(quick_tools.verify_user_password(password)))

        # Mot de passes valide aléatoire
        for j in range(0, 10):          # Amélioration => tester tous les caractères
            password = ""
            for i in range(0, 7):
                password += random.choice(string.ascii_letters)
            password += random.choice(string.digits)
            password += random.choice(string.punctuation)
            self.assertTrue(quick_tools.verify_user_password(password))

        return
    
    def testRoomTypeVerification(self):
        # Tests sur les Rooms
        print("Tests \"Room Type Verification\"")

        quick_tools.add_room(self.db_path, "room1", "public")
        self.assertTrue(len(quick_tools.get_rooms(self.db_path)) == 1)
        quick_tools.delete_room(self.db_path, "room1")

        quick_tools.add_room(self.db_path, "room2", "error")
        self.assertTrue(len(quick_tools.get_rooms(self.db_path)) == 0)
        if(len(quick_tools.get_rooms(self.db_path)) == 1):
            quick_tools.delete_room(self.db_path, "room2")

        quick_tools.add_room(self.db_path, "room3", "private")
        self.assertTrue(len(quick_tools.get_rooms(self.db_path)) == 1)
        quick_tools.delete_room(self.db_path, "room3")

        return
    
    def testUserName(self):
        # Tests sur les Rooms
        print("Tests \"Username Verification\"")

        # Username avec nombre
        username = "Username0"
        self.assertTrue(not(quick_tools.verify_user_name(username)))

        # Username avec caractère spécial
        username = "Username!"
        self.assertTrue(not(quick_tools.verify_user_name(username)))

        # Username correct
        username = "Username"
        self.assertTrue(quick_tools.verify_user_name(username))

        # Utilisateur déjà existant
        quick_tools.add_user(self.db_path, "User", "none", "none", "Passw0rd!")
        username = "User"
        self.assertTrue(not(quick_tools.verify_user_name(username)))

        quick_tools.delete_user(self.db_path, "User")

        return

    # Appelé à la toute fin des tests
    @classmethod
    def tearDownClass(cls):
        cls.connect.close()
        delete_db(cls.db_path)

if __name__ == '__main__':
    unittest.main()