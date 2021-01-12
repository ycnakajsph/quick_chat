#TD Tests logiciels : Développement TDD
***
_**Réalisé par Ghettas Walid et Jebali Afif**_
--
##1) Qu’est-ce que le TDD ?

Le TTD est un acronyme anglais signifiant Test Driven Development que l'on peut traduire par "développement piloté par les tests". Il s'agit d'une méthode contrôlant la qualité des logiciels. Les processus du TDD sont cycliques (on détermine les cas tests qui échouent souvent). Cela est fait exprès, car par la suite, nous n’écrivons uniquement la quantité de code nécessaire pour réussir le test. Les composants sont alors remaniés. Ainsi, en conservant ses fonctions, nous étendons le code source ou nous en faisons la restructuration si nécessaire.

##2) En quoi le TDD et l'approche devops peuvent ils améliorer la qualité d'un logiciel?

Comme vu à la question précédente, l'objectif du TDD est d'écrire des tests avant le code. En testant chaque fonction de manière unitaire, on s’assure du bon fonctionnement de celle-ci de manière individuelle. Chaque fonction sera traitée isolément avec des caractéristiques propres à chaque fonction. L’approche devops permet également le test de chaque fonction que l’on écrit. La différence réside dans la façon de mener le test. Ici, l'ensemble du code sert de contexte pour le test de la fonction. Les fonctions ne sont plus testées séparément mais seront liées aux performances de l'ensemble du code. Ces 2 approches permettent l’amélioration de la qualité d’un logiciel, la 1ère avec une vue individuelle à chaque fonction tandis que la 2nde avec une vue plus globale, celle de la fonction qu’on modifie avec la vue générale du projet

Objectif :

Coder la feature suivante en mode TDD (avec les même consignes que la dernière fois):le nom d'utilisateur doit être unique et ne doit contenir aucun chiffre ni aucun symbole

Etape 1 : 
--
    Ecrire le prototype de la fonction de vérification du nom d'utilisateur unique et sans aucun chiffre ni symbole
    verifyUsername

    Ecrire le prototype de la fonction verifyRoomType, verifiant le type de la room
    
    Ecrire le prototype de la fonction verifyPassword, verifiant la taille et la présence de chiffre et caractere spéciaux.

Etape 2 :
--
    Ecrire les test correspondant aux fonctions, afin de définir les spécifications
    TestVerifyUsername
    TestverifyPassword
    TestVerifyRoomtype

Etape 3 :
--
    Rédiger ensuite les fonctions de l'étape 1 répondant au test.
