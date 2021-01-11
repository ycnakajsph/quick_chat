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
