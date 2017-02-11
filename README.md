## Introduction
Vous trouverez ici la feuille de personnage type poour le système D10. Cette feuille a été créée pour fonctionner avec Roll20.

## HTML

 - Ne pas utiliser d'ID, seulement des classes. Il y a en effet
   plusieurs copies de la feuille lors d'une partie, l'utilisation d'ID
   pourra par conséquent entraîner des comportements inattendus.

## CSS

 - La feuille complète est contenue dans une grande div
   ```.charsheet```, pour éviter d'appliquer le CSS au reste de roll20.
   Le CSS sera modifié en conséquence lors de l'import.
 - Lors de
   l'import, toutes les classes qui ne sont pas préfixées de
   ```attr_```, ```roll_``` ou ```repeating_``` seront préfixées de
   ```sheet-```. Il faut donc prévoir le CSS en conséquence.

   