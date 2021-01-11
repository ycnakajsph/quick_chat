# Questions

## Qu'est ce que du TDD ?
```
Le _Test-Driven Development_ est une méthode de développement consitant à concevoir un logiciel par petits incréments.
Chaque test est alors écrit avant la fonctionnalité correspondante.
Ce paradigme de développement se base sur trois règles :
	- Il est interdit d'écrire du code de production tant qu'on n'a pas réussi à écrire un code test qui échoue.
	- Si on écrit un test qui échoue, on ne dois pas en écrire un autre tant que celui-ci n'est pas résolu
	- On ne peut écrire que du code de production visant à résoudre les tests en cours, ni plus ni moins

```

## En quoi le TDD et l'approche devops peuvent ils améliorer la qualité d'un logiciel?
```
L'approche devops telle que nous l'avons défini consiste en l'automatisation des tests d'intégrations.
Cela veut donc dire qu'à chaque fois que l'on ajoute une nouvelle fonctionnalité à la branche principale,
on va lancer une série de tests visant à vérifier que le master est toujours sain.

Ainsi, baser notre développement logicielle en utilisant le TDD et l'approche devops permet de construire
notre projet de manière très sécurisée. Chaque erreur sera détectée très tôt et sera donc peu coûteuse à
corriger
```

# Réalisations

## Ajout de fonctions et tests sur les user_name

### Etape 1 :
```
Ajout d'un test qui insert un nouvel utilisateur dans la base de données dont le user_name correspond bien
aux spécifications (username unique, ne contenant ni chiffre ni caractères spéciaux), et vérifie si ce dernier
est bel et bien ajouté dans la base.
```

### Etape 2 :
```
Ajout d'un second test qui insert un nouvel utilisateur ayant un username contenant un chiffre, un second ayant
un username contenant un caractère spécial, et en insert un troisième ayant un username correct deux fois (non unique),
le test vérifie que des exception sont bien levées lors des tentatives d'insertion.
```

### Etape 3 :
```
Ajout d'une fonction is_user_name_ok appelée lors de l'ajout d'un utilisateur à la base de données afin de vérifier
que le user_name spécifié est conforme aux spécifications. Dans le cas contraire, lève une exception.
```

### Etape 4 :
```
Gestion des exceptions levées lors des fonctions de vérifications de la conformité des user_name, user_password et
room_type grâce à l'ajout de blocs try/except dans les fonctions add_user et add_room. En cas de mauvaise données,
l'application ne crash plus et affiche simplement un message d'erreur, puis termine son execution sans ajouter les
données indésirables à la base de données.
```
