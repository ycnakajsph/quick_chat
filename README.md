# Questions

## Le TDD

TDD signifie Test Driven Developpement qui se traduit grossièrement par développement dirigé par les tests. Il s'agit d'une méthode de développement qui consiste à développé un logiciel petit à petit en se basant sur des tests.
Le TDD est fondé par trois règles:
- Il est interdit d'écrire du code de production tant qu'on n'a pas réussi à écrire un code test qui échoue.
	- Si on écrit un test qui échoue, on ne dois pas en écrire un autre tant que celui-ci n'est pas résolu
	- On ne peut écrire que du code de production visant à résoudre les tests en cours, ni plus ni moins
	
## En quoi le TDD améliore le code ?

L'approche devops autonomise les tests d'intégrations, c'est-à-dire les tests sur l'ensemble du projet. À chaque fois que la branche master est mise à jour, elle doit repasser les tests pour vérifier que tout est encore fonctionnel.
En construisant et vérifiant les nouvelles fonctionnalitées de manière unitaire avec l'approche TDD et de manière globale avec le devops, on s'assure que le projet est construit sur des bases saines.

# Developpement

## Test username

### Step 1 : test username correct

Insertion d'un username correct
Vérification de l'ajout

### Step 2 : test username incorrect

Insertion d'username incorrect:
	- chiffre dans le nom
	- caractère spécial dansle nom
	- nom déjà utilisé
La fonction add_user ne passe pas les tests

### Step 3 : modification de la fonction

Ajout d'une fonction is_user_name_ok pour que le username respecte la spécification

### Step 4 : Gestions des exceptions

try/except dans la fonction add_user


