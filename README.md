# Quick Chart
_**Projet de Test Logiciel**_

_**Author : Huiling BAO & Heyang LI**_

Introduction général
--
Un logiciel de chat d'entreprise pour développeurs:
- Pourra être exécuté dans un terminal
- Devra avoir un système d’authentification
- Les salles pourront être publiques ou privées
- Il devra y avoir un historique
- Il n’y aura probablement pas plus de 20 personnes par salle
- Côté architecture, les ressources sont limitées mais un serveur pourra être mis à disposition

Architecture de base des données
--
Afin de réaliser ce logiciel, il doit d'abord créer une base des données pour sauvegarder les données utiles et en utilisant ces données pour contrôler le système.

| Room |[id_room] INTEGER|[room_name] text|[room_type] text|
| :------------: | :------------: | :------------: | :------------: |

| User |[id_user] INTEGER|[user_name] text|[user_role] integer|[user_rights] integer|[user_password] text|
| :------------: | :------------: | :------------: | :------------: | :------------: | :------------: |

Donc la processus de contôler ce systèmes peut faciliter par les opérations de SQL.
- Ajouter les valeur : `add_room` et `add_user`
- Sélectionner les valeurs : `get_rooms` et `get_users`
- Supprimer les valeurs : `delete_room` et `delete_user`

TDD: Test-Driven Development
--

Le but est de nous familiariser de la méthode TDD. Donc nous avons d'abord analysé les fonction à réaliser et codé les tests. Après nous avons fait le développment afin de réaliser et passer tout les tests.

Etape 1: Ajouter les tests et les fonctions à tester. Les fonctions sera codé après les tests sont finis.

Prototypes des Fonctions: 
```python
def verify_user_password(user_password):

def verify_room_name(room_name):

def verify_room_type(room_type):

```
Tests unitaires:
```python
def test1_create_db(self):

def test2_verify_user_password(self):

def test3_add_user(self):

def test4_get_users(self):

def test5_delete_user(self):

def test6_verify_room_name(self):

def test7_verify_room_type(self):

def test8_add_room(self):

def test9_get_rooms(self):

def test10_delete_room(self):

```
Etape 2: Compléter les tests correspondant à différentes fonctions (Détails dans la section suivante Test Unitaire)

Etape 3: Compléter les fonctions pour passer tout les tests (Détails après la section Test Unitaire)

Test Unitaire
--
Afin de réaliser les tests unitaires, nous avons utiliser le _unittest_. En raison que les tests exécutent à l'ordre d'alphabet(ACSII). Donc nous devons bien générer les noms de la fonctions de test pour organiser notre test dans le bon ordre.
- `test1_create_db`
Dans cette test, nous devons assurer qu'on a bien généré les deux tableaux _Rooms_ et _Users_, et on les vérifie à l'aide de l'instruction de SQL.
```python
def test1_create_db(self):
		c.execute('DROP TABLE IF EXISTS Rooms;')
		c.execute('DROP TABLE IF EXISTS Users;')
		create_db(db_path)
		sql = "select * from Users;"
		table_name = ''
		for row in c.execute(sql).fetchall():
			table_name = row[0]
		self.assertEqual(table_name,'')

		sql = "select * from Rooms;"
		table_name = ''
		for row in c.execute(sql).fetchall():
			table_name = row[0]
		self.assertEqual(table_name,'')
```

- `test2_verify_user_password`
Nous savons que le mot de passe doit avoir un numéro, un caractère spécial et une longueur>= 8. Donc dans cette test, on désigne 3 tests avec des mots de passe valides/invalides pour assuser que seulement les mots de passe qui répondent aux exigences peuvent réussir le test. Nous donnons 3 situations : la longueur du mot de passe soit inférieur à 8, manque le caractère spécial et la situation correcte.
```python
def test2_verify_user_password(self):

		self.assertFalse(verify_room_name('qwer')) # not long enough
		self.assertFalse(verify_room_name('qwer123456')) # no special character

		random_str_len = random.randint(5,10)

		correct_password = ''.join(random.choice(string.ascii_lowercase) for i in range(random_str_len))
		correct_password += '123456,'

		self.assertTrue(verify_user_password(correct_password))
```

- `test3_add_user`
Nous savons que seulement les mots de passe qui répondent aux exigences peuvent réussir d'ajouter les valeurs dans la tableau. Donc on a fait deux test.Une avec le mot de passe correcte afin de vérifier les valeurs sont bien ajoutés dans la tableau.L'autre avec le mot de passe incorrecte pour vérifier que l'on a bien refuser d'ajouter ces valeurs.
```python
def test3_add_user(self):
		add_user(db_path,'yann.c',0,0,'qwer123456,')  # add a correct user
		sql = "select user_name from Users where user_name = 'yann.c';"
		user_name = ''
		for row in c.execute(sql):
			user_name = row[0]
		self.assertEqual(user_name,'yann.c')

		add_user(db_path,'huiling.b',0,0,'pass')  # add a user with wrong password format
		sql = "select user_name from Users where user_name = 'huiling.b';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'')
```

- `test4_get_users`
Dans cette test, nous devons assurer qu'on on a bien sélectionné les valeurs souhaités dans la tableau de _Users_.
```python
def test4_get_users(self):

		self.assertEqual(get_users(db_path),['yann.c'])  # Have to be able to get the user added
```

- `test5_delete_user`
Dans cette test, nous devons assurer qu'on a bien supprimé les valeurs souhaités dans la tableau de _Users_, et on les vérifie à l'aide de l'instruction de SQL.
```python
def test5_delete_user(self):

		delete_user(db_path,'yann.c')
		sql = "select user_name from Users where user_name = 'yann.c';"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')  # Successful delete the user 
```

- `test6_verify_room_name`
Nous savons que Room\_name doit commencer par ROOM\_ et comporter plus de 8 caractères. Donc dans cette test, on vérifie 3 fois pour assuser que seulement Room\_name qui répondent aux exigences peuvent réussir le test.Nous donnons 3 situations : Room\_name ne commence pas par ROOM\_, la longueur de Room\_name inférieur à 8 et la situation correcte.
```python
def test6_verify_room_name(self):

		self.assertFalse(verify_room_name('false')) 
		self.assertFalse(verify_room_name('ROOM_')) 

		random_str_len = random.randint(3,20)
		correct_room = 'ROOM_'
		correct_room += ''.join(random.choice(string.ascii_lowercase) for i in range(random_str_len))

		self.assertTrue(verify_room_name(correct_room))
```

- `test7_verify_room_type`
Le type de room doit définir en publiques ou privées.Donc dans cette test, on vérifie 3 fois pour assuser que seulement Room\_type qui est publiques ou privées peuvent réussir le test.Nous donnons 3 situations : Room\_type ne déclare pas, Room\_type de _public_ et Room\_type de _private_ .
```python
def test7_verify_room_type(self):
		self.assertFalse(verify_room_type('false_type')) 
		self.assertTrue(verify_room_type('public'))
		self.assertTrue(verify_room_type('private'))
```

- `test8_add_room`
Nous savons que seulement Room\_type qui est publiques ou privées peuvent réussir d'ajouter les valeurs dans la tableau. Donc on a fait trois test.Une avec Room\_type de _public_ et Room\_type de _private_ afin de vérifier les valeurs sont bien ajoutés dans la tableau.L'autre avec Room\_type qui est unconnu pour vérifier que l'on a bien refuser d'ajouter ces valeurs.
```python
def test8_add_room(self):

		add_room(db_path,'ROOM_dinningroom','public') # correct room 
		sql = "select room_name from Rooms where room_name = 'ROOM_dinningroom';"
		for row in c.execute(sql):
			room_name = row[0]
		self.assertEqual(room_name,'ROOM_dinningroom')

		add_room(db_path,'ROOM_bedroom','unknown') # wrong room type
		sql = "select room_name from Rooms where room_name = 'ROOM_bedroom';"
		res = ''
		for row in c.execute(sql):
			res = row[0]
		self.assertEqual(res,'')

		add_room(db_path,'ROOM_no','private') # wrong room name
		sql = "select room_name from Rooms where room_name = 'ROOM_no';"
		res = ''
		for row in c.execute(sql):
			res = row[0]
		self.assertEqual(res,'')
```

- `test9_get_rooms`
Dans cette test, nous devons assurer qu'on on a bien sélectionné les valeurs souhaités dans la tableau de _Rooms_.
```python
def test9_get_rooms(self):

		self.assertEqual(get_rooms(db_path),['ROOM_dinningroom'])
```

- `test10_delete_room`
Dans cette test, nous devons assurer qu'on a bien supprimé les valeurs souhaités dans la tableau de _Rooms_, et on les vérifie à l'aide de l'instruction de SQL.
```python
def test10_delete_room(self):
		delete_room(db_path,'ROOM_dinningroom')
		sql = "select room_name from Rooms where room_name = 'ROOM_dinningroom';"
		none = ''
		for row in c.execute(sql):
			none = row[0]
		self.assertEqual(none,'')
```

Système d'authentification
--
- Nous avons besoin de vérifiez que le mot de passe a un numéro, un caractère spécial, une longueur>= 8.

```python
def verify_user_password(user_password):
	# Extra requirement: check the password have number,special character, length>8 
	is_number = 0
	special_character = 0

	for i in user_password:
		if i.isdigit():
			is_number = 1

		if (not i.islower()) and (not i.isupper())  and (not i.isdigit()):
			special_character = 1

	if len(user_password)>=8:
		if is_number and special_character:
			return True

	return False
```

Salles publiques ou privées
--
- Room\_name doit commencer par ROOM\_ et comporter plus de 8 caractères

```python
def verify_room_name(room_name):
	# Extra requirement: room_name start with ROOM_ and length >=8
	if room_name.startswith('ROOM_'):
		if len(room_name) >= 8 :
			return True
	return False
```
- Le type de room doit définir en publiques ou privées

```python
def verify_room_type(room_type):
	# Extra requirement: room_type has to be public or private
	if room_type == 'public' or room_type == 'private':
		return True
	return False
```

