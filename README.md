Qu'est ce que du TDD? 

TDD： Test - Driven Dvelopement

Il faut d'abord écrire le code de test du certain module selon le besoin du projet. Et puis le développement du code faut passer ce code de test.

C'est une méthodologie de conception. C' est la pratique de base des méthodes agiles. Le principe de TDD est d'écrire le code de test unitaire avant de développer le code fonctionnel, et le code de test détermine quel code produit doit être écrit. 

L'idée de base du TDD est de promouvoir l'ensemble du développement par des tests, mais le développement piloté par les tests n'est pas seulement un simple travail de test, mais un processus de quantification de l'analyse des exigences, de la conception et du contrôle qualité.

Le but important de TDD n'est pas seulement de tester les logiciels, mais aussi d'aider les clients et les programmeurs à supprimer les exigences ambiguës pendant le processus de développement. TDD considère d'abord les exigences d'utilisation (objets, fonctions, processus, interfaces, etc.), principalement en écrivant des cadres de cas de test pour concevoir des processus fonctionnels et des interfaces, et le cadre de test peut continuer à vérifier.

Règles du TDD : 

Vous n'êtes pas autorisé à écrire un code de production à moins que ce ne soit pour réussir un test unitaire en échec.
Vous n'êtes pas autorisé à écrire plus de tests unitaires que ce qui est suffisant pour échouer; et les échecs de compilation sont des échecs.
Vous n'êtes pas autorisé à écrire plus de code de production que ce qui est suffisant pour réussir le test unitaire qui a échoué

Donc le processus de travail pour TDD : 

 Choisir une partie à tester et réaliser un test.
 Exécuter le programme et une fois que le test fonctionnel a échoué, trouvez un moyen d'écrire le code pour réussir (ou au moins laisser passer le test en cours d'échec). À cette partie, utilisez un ou plusieurs tests unitaires pour définir l'effet souhaité du code afin de vous assurer qu'il correspond à chaque ligne de l'application. 
 Une fois le test unitaire échoué, écrivez le moins de code d'application pour que le test unitaire réussisse. Parfois, on doit répéter plusieurs fois les deuxième et troisième étapes jusqu'à ce qu' on sente que le test fonctionnel a fait un peu de progrès.
Exécutez à nouveau le test fonctionnel pour voir s'il réussit ou s'il y a une progression. Cette étape peut nous inciter à écrire de nouveaux tests unitaires et du code, etc.


En quoi le TDD et l'approche devops peuvent ils améliorer la qualité d'un logiciel?

On peut également voir à partir du processus de cycle TDD ci-dessus que le plus grand avantage du développement piloté par les tests(TDD) est la refactorisation, l'itération continue, la refactorisation continue du code existant, l'optimisation continue de la structure interne du code et enfin la réalisation de l'amélioration globale du code.  De cette manière, une certaine redondance de conception, une redondance de code, une complexité d'interface, etc sont continuellement réduites.

Il peut aussi :

Réduisez le fardeau des développeurs. Grâce à un processus clair, concentrons-nous sur un seul point à la fois, avec moins de charge de réflexion.
Filet de protection. La couverture complète des tests unitaires fournit un filet de protection pour le code produit, afin que nous puissions facilement répondre aux changements d'exigences ou améliorer la conception du code. Ainsi, si les besoins du projet sont stables et terminés en une seule fois, sans aucune modification ultérieure, on pourra moins profiter des avantages du TDD.
Clarifiez les exigences à l'avance. Écrire d'abord les tests peut nous aider à réfléchir aux exigences et à clarifier les détails des exigences à l'avance, plutôt que de découvrir des exigences peu claires à la moitié du code.
Retour rapide. S'il n'y a pas de test unitaire, on doit le tester manuellement: il faut beaucoup de temps pour préparer les données, démarrer l'application, passer à l'interface, etc. Le retour d'information est très lent.
On regardera le produit qu' on est sur le point de terminer du point de vue de l'utilisateur et on devra penser à toutes les opérations que l'utilisateur effectue autant que possible. Plutôt que de réfléchir à la manière dont les utilisateurs devraient utiliser nos produits du point de vue des programmeurs.
Écrivez des cas de test avant d'écrire du code, ce qui peut nous fournir des références instructives pour l'écriture de code. Empêchez-nous de manquer certaines fonctionnalités.
Si le cas de test échoue après avoir changé le code, nous pouvons localiser avec précision le problème en fonction du cas de test qui a échoué et résoudre le bogue facilement.

Et pour le devops :

Déclenchée directement par la soumission de code: éliminez le temps d'attente et les commentaires rapides
Chaque changement correspond à un pipeline de livraison: localisation et débogage faciles des problèmes
Automatisation efficace de l'ensemble du processus de développement: résultats de livraison stables, rapides et prévisibles
Tests de régression automatisés en continu: améliorer la qualité de livraison
Les installations sont partagées et fournies à la demande: maximisez l'utilisation des ressources
La collaboration a brisé les barrières entre les processus et les services, le partage d'informations et la planification coordonnée; l'automatisation du processus a éliminé le travail répétitif et réduit les risques humains



TDD du vérification complémentaire:

Étape1:  
Selon les instructions, écrire le fichier de test: On a met les exemples incorrects(username déjà existé, username compris les digital et caractères spéciaux), et aussi les exemples correct.

Etape2: 
Selon le fichier de test, on écrit le code pour compléter la fonction verify_username.

Etape3: 
Après, on teste le code dev, le test ne passe pas si le code dev n’est pas correct. On modifie le code dev.

 

