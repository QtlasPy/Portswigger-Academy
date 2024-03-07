<h1> Business Logic Vulnerabilities </h1>

<h2> Definition : </h2>

<p> <strong><i>Business Logic</i></strong>

Dans ce contexte, ce terme désigne l'ensemble des règles et des scénarios défini par une application web, ainsi que la manière dont le serveur doit réagir en fonction de l'interaction d'un utilisateur. </p>

<p> <strong><i> Business Logic Vulnerabilities </i></strong>

  Les vulnérabilités liées à la logique d'une application web sont des failles qui résident  dans sa conception logique et ne dépendent pas d'une bibliothèque, d'un langage ou d'une technologie spécifique. Elles permettent à un attaquant de modifier le comportement normal de l'application et surviennent souvent lorsque le développeur n'a pas anticipé une situation particulière. </p>


<h2> Exemples : </h2>

<p>Ce type de vulnérabilité dépend de la manière dont le serveur a été développé, il serait donc difficile d'énumérer tous les exemples d'exploitation possibles. Contrairement à des failles d'injection SQL, ou d'une XSS, dont l'exploitation ne depend pas de la nature de l'application. Pour les vulnérabilités qui agissent sur le fonctionnement propre d'une application, il est crucial de différencier si le serveur web est un site marchand, une banque, un forum, une API etc ...

On peut cependant identifier des points communs entre les causes qui ont conduit à cette faille, car même si l'exploitation depend énormément de la nature du site web, l'origine de cette vulnérabilité elle repose souvent sur la naïveté des développeurs web.</p>

<ol>
  <li><strong> Mauvaises gestions des inputs </strong></li>
  <p> La mauvaise gestion des inputs constitue un réel danger pour une application. Faire confiance aux entrées fournies par les utilisateurs ou aux vérifications côté client, que ce soit avec du JavaScript ou des attributs HTML, peut exposer une application à des risques. Car il existe plusieurs moyens pour envoyer des requêtes HTTP directement au serveur sans passer par le navigateur, donc passer outre les vérifications clients. Ces moyens peuvent être l'utilisation d'un proxy (Burpsuite, Owasp ZAP), d'une commande (cURL), ou encore l'utilisation d'une librairie (requests).

  Prenons l'exemple d'un site web bancaire, et imaginons le pseudo-code suivant qui servirait pour effectuer des virements: </p>

  ```python
  def virements(montant, compte_envoyeur, compte_receveur):
    if type(montant) == int and montant <= compte_envoyeur['solde']:
      compte_envoyeur['solde'] -= montant  
      compte_receveur['solde'] += montant
  ```

  <p> Dans ce code, nous nous concentrons sur la logique de la fonction virements plutôt que sur les détails techniques. On peut identifier les contraintes suivantes : le montant doit être un entier et doit être inférieur à l'argent disponible sur le compte envoyeur. Maintenant que se passe-t-il si nous envoyons un montant négatif ? Les deux conditions sont vérifiée et l'argent que nous devrions normalement déduire de notre solde et en fait ajouté (car a - (-b) = a + b). Cette vulnérabilité majeure est un exemple d'exploitation d'une faille logique dans une application web, et démontre 2 choses : <ol>
  <li> Il ne faut jamais faire confiance aux inputs clients </li>
  <li> Il faut un domaine de définition très précis pour les variables  </li>
  </ol>
  </p>
    <li><strong> Scenario imprevue </strong> </li>
    <p> Lorsque un développeur va concevoir un site web, il va émettre des scénarios et des assumations sur ce qu'un utilisateur normale devrait faire par rapport à une fonctionalite doneee. Une mauvaise pratique est de pensée que l'utilisateur suivra toujours le scénario écrit pour une fonctionalite, dans ce cas-là l'application web manquera énormément d'anticipations vis a vis des scenarios imprevue et peut eventuellement ammener a etre exploiter. Prenons un autre exemple, celui d'un site marchand et imaginons le scenario classique d'un achat.</p>
    <img src=scenario.png/>
    <p> Ici on représente le cas classique d'un achat en ligne. Mais supposons maintenant que nous sortons du scénario écrit et que nous modifions un peu le dérouler de l'achat.</p>
    <img src=scenario2.png/>
    <p> Dans le deuxième cas, nous accédons directement à la page de confirmation de commandes sans passer par la page ou nous rentrons nos informations bancaires. Plusieurs questions peuvent se poser alors, sont ce que le serveur a été penser pour anticiper ce scénario . Ou cela va-t-il créer une erreur ? Ou pire encore, est-ce que nous pourrions valider une commande sans rentrées nos informations bancaires   ?</p>
</ol>
