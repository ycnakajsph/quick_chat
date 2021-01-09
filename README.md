<h1>Ajout de fonctions et tests sur les room_type et user_password</h1>
<p> Réalisé par Théo GERMAIN et Thomas BOUIX </p>
<ul>
  <li><h2>Etape 1 : </h2> Ajout d'une fonction 'is_room_type_ok' appelée lors de l’ajout d’une nouvelle room. Cette fonction <br /> test le room_type pour savoir s’il vaut ‘public’ ou ‘private’. <br />Si le paramètre à une autre valeur, une exception est  levée.</li>
  <li><h2>Etape 2 : </h2> Ajout d'une fonction 'is_user_password_ok' appelée lors de l’ajout d’un nouvel utilisateur. Cette fonction <br /> vérifie que le mot de passe fasse au moins 8 caractères, et contienne au moins 1 nombre et 1 caractère non alphanumérique.<br /> Dans le cas contraire, une exception est levée.</li>
</ul>
