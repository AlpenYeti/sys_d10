## Introduction
Vous trouverez ici la feuille de personnage type pour le système D10. Cette feuille a été crée pour fonctionner avec Roll20.

## Macros roll20
Peuvent etre utile a modifier ou récuperer:
 - ```shieldLife_Points / shieldLife_Points_max``` : Points de Vie
 - ```shieldEndurance_Points / shieldEndurance_Points_max``` : Points de fatigue
 - ```shieldgeneral_item_weapon1``` : La valeur de dégats de l'arme 1
 - ```shieldgeneral_item_weapon1_name``` : Le nom de l'arme 1
 - ```shieldgeneral_effective_weapon1``` : La valeur de dégats de l'arme 1 si elle est activée; 0 sinon
 - ```shieldbase_damage_dices``` : La base de dégats offensif (a priori, rien sauf compétence particulière)
 - ```shieldexal_damage_dices``` : Le modificateur de dégats (Un bonus de charge, un buff de dégats temporaires)

Exemple (avec chatSetAttr) [chatSetAttr](https://github.com/Roll20/roll20-api-scripts/blob/master/ChatSetAttr/README.md):
 - ```!setattr --sel --Life_Points|21```
 - ```!setattr --set --mod --Life_Points|-5```
 - ```!setattr --name Basil --general_item_weapon1|55```

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
   ```shield```, ```roll_``` ou ```repeating_``` seront préfixées de
   ```sheet-```. Il faut donc prévoir le CSS en conséquence.

##### Ces informations proviennent de la doc Roll20, et plus particulièrement de la page [Building Character Sheet](https://wiki.roll20.net/Building_Character_Sheets).
