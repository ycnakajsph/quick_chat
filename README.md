<h1>Ajout de fonctions et tests sur les room_type et user_password</h1>
<p> Réalisé par Théo GERMAIN et Thomas BOUIX </p>
<ul>
  <li><h2>Etape 1 : </h2> Ajout d'une fonction 'is_room_type_ok' appelée lors de l’ajout d’une nouvelle room. Cette fonction <br /> test le room_type pour savoir s’il vaut ‘public’ ou ‘private’. <br />Si le paramètre à une autre valeur, une exception est  levée.</li>

  <li><h2>Etape 2 : </h2> Ajout d'une fonction 'is_user_password_ok' appelée lors de l’ajout d’un nouvel utilisateur. Cette fonction <br /> vérifie que le mot de passe fasse au moins 8 caractères, et contienne au moins 1 nombre et 1 caractère non alphanumérique.<br /> Dans le cas contraire, une exception est levée.</li>

  <li><h2>Etape 3 : </h2> Ajout d'une fonction 'test_add_room_type' dans le module de test 'TestQuickTools.py'. <br />Cette fonction vérifie qu'une exception est bien levée lorsque l'on passe un room_type différent de 'public' ou 'private' lors de l'ajout d'une room.</li>

  <li><h2>Etape 4 : </h2> Ajout d'une fonction 'test_add_user_password' dans le module de test 'TestQuickTools.py'. <br />Cette fonction vérifie qu'une exception est bien levée lorsque l'on passe un user_password qui ne répond pas aux spécifications. Cette fonction test que les 3 cas possibles (moins de 8 caractères, pas de chiffre ou pas de caractère spéciaux) lèvent bien une exception.</li>
</ul>
