#TD pour le developpement en mode TDD

## Questions

### Qu'est ce que du TDD?

TDD ou Test-Driven Development est la pratique qui consiste à développer un
programme en préparant le test pour chaque étape avant d'écrire le code source.

### en quoi le TDD et l'approche DevOps peuvent ils améliorer la qualité d'un logiciel ?

En testant continuellement les limites du code, par l'ajout de tests de plus en plus
sophistiqués, nous pouvons remanier constamment le code et le faire atteindre sa forme
la plus robuste. Il est plus simple de remanier un programme pendant son developpement
car il est encore possible de changer entièrement sa logique pour l'améliorer
plutôt que de tout tester à la fin et faire de simples modifications pour que les
tests renvoient le bon résultat.

## Etape 1 : Developpement des tests

Nous avons d'abord commencer par faire les tests pour nos fonctions
verify_user_psswd() et test_verify_room_type(). Une fois codée, elles devront
les passer pour être validées.

## Etape 2 : Developpement des fonctions

Nous avons ensuite écrit les fonctions et une fois que les tests ne renvoyaient
pas d'erreurs, nous avons pu arrêter le développement.

## Etape 3 : Test de verify_username

Les conditions à respecter pour le username sont ici d'avoir un nom unique et
qui ne dispose d'aucun symbole ou chiffre. Pour verifier que le nom est unique,
il faut le verifier directement dans la base de données, on ajoute donc les
méthodes setUp() et tearDown() pour créer une BDD de test. On utilise la
fonction add_user pour ajouter quelques utilisateurs pour le test.
