import generator

__ALL__=["DISTANCE","MELEE"]

class DISTANCE(generator.Node):
    """DISTANCE Weapons"""

    def __init__(self, name,nb):
        super(DISTANCE, self).__init__("repeating_ranged-weapons",0)

    def content(self):
        ret="""    <!--ranged -->
    <fieldset class="repeating_ranged-weapons">
      <div class="quickborder">
        <div class="sheet-row">
         <input class="sheet-skill_name" type="number" name="attr_wid" title="Numero de ligne" />
         <input class="sheet-skill_name" type="text" name="attr_ranged_weaponname" title="Nom de l'arme" />
         <label>P</label>
         <input type="number" name="attr_ranged_accuracy" title="Précision" />
         <label>Mode</label>
         <input type="number" name="attr_ranged_single" title="Coup par coup" />
         <label>/</label>
         <input type="number" name="attr_ranged_burst" title="Rafale" />
         <label>/</label>
         <input type="number" name="attr_ranged_auto" title="Automatique" />
        </div>
        <div class="sheet-row">
          <label>Type</label>
          <input type="text" name="attr_typename" title="Type d'arme" />
          <select class="sheet-weapon_type_select" name="attr_ranged_type_select">
           <option value="@{combat_skilllevel_armesdassaut}">Arme d'Assaut</option>
           <option value="@{combat_skilllevel_armesdepoing}">Arme de Poing</option>
           <option value="@{combat_skilllevel_munitionssolide}">Munitions Solides</option>
           <option value="@{combat_skilllevel_projectilesbalistiques}">Arme Balistique</option>
           <option value="@{combat_skilllevel_projectilesautopropulss}">Projectile Autopropulsé</option>
           <option value="@{combat_skilllevel_armementlaser}">Armement Laser</option>
           <option value="@{combat_skilllevel_guidagedemissiles}">Guidage de Missiles</option>
           <option value="@{combat_skilllevel_balistique}">Balistique Superlative</option>
           <option value="0">Aucune spécialité</option>
          </select>
          <button type='roll' class="sheet-skillbutton" title ="Dégats" value="&{template:d10Shooting} {{name=@{ranged_weaponname}}} {{subtags=@{typename}}} {{damagedone=[[(?{Sucesses}-1)*@{ranged_dmgPlus}+@{ranged_dmgBase}]]}} {{magsize=@{ranged_magT}}} {{ammocurrent=@{ranged_magA}}} {{ammototal=@{ranged_ammoT}}}">Dégats</button>
          <button type='roll' class="sheet-skillbutton" title ="Rechargement" value="/em reloads the @{ranged_weaponname} loosing @{ranged_magA} ammo in the process. &#13;!setattr --name @{character_name} --repeating_ranged-weapons_$@{wid}_ranged_magA|[[{@{ranged_magT},@{ranged_ammoT}}kl1]] --repeating_ranged-weapons_$@{wid}_ranged_ammoT|[[{0,@{ranged_ammoT}-@{ranged_magT}}kh1]]">Rechargement</button>
        </div>
        <div class="sheet-row">
          <label>Chargeur</label>
          <input type="number" name="attr_ranged_magA" title="Chargeur Actuel" />
          <label>/</label>
          <input type="number" name="attr_ranged_magT" title="Chargeur Total" />
          <label>|</label>
          <input type="number" name="attr_ranged_ammoT" title="Munitions Totales" />
          <label>Dégats</label>
          <input type="number" name="attr_ranged_dmgBase" title="Dégats base" />
          <label>/</label>
          <input type="number" name="attr_ranged_dmgPlus" title="Dégats additionels" />
          <label>Spécial</label>
          <input type="text" name="attr_ranged_special" title="Spécial" />
    <button type='roll' class="sheet-skillbutton" title ="Tir simple" value="&{template:d10Shooting}{{name=@{ranged_weaponname}}}{{subtags=@{typename}}} {{attack=[[?{Dices}d10<[[@{ranged_type_select}+?{Seuil|4}+@{ranged_accuracy}]]cs1cf11]]}} {{mode=Single Shot}}  {{damage=@{ranged_dmgBase}/+@{ranged_dmgPlus}}} {{usedammo=@{ranged_single}}} {{magsize=@{ranged_magT}}} {{ammocurrent=[[@{ranged_magA}-@{ranged_single}]]}} {{ammototal=@{ranged_ammoT}}} {{special=@{ranged_special}}} !modattr --name @{character_name} --repeating_ranged-weapons_$@{wid}_ranged_magA|-@{ranged_single}!!!">S</button>
    <button type='roll' class="sheet-skillbutton" title ="Rafale" value="&{template:d10Shooting}{{name=@{ranged_weaponname}}}{{subtags=@{typename}}} {{attack=[[[[?{Dices}+1]]d10<[[@{ranged_type_select}+?{Seuil|4}+@{ranged_accuracy}]]cs1cf11]]}} {{mode=Burst}}  {{damage=@{ranged_dmgBase}/@{ranged_dmgPlus}}} {{usedammo=@{ranged_burst}}} {{magsize=@{ranged_magT}}} {{ammocurrent=[[@{ranged_magA}-@{ranged_burst}]]}} {{ammototal=@{ranged_ammoT}}} {{special=@{ranged_special}}} !modattr --name @{character_name} --repeating_ranged-weapons_$@{wid}_ranged_magA|-@{ranged_burst}!!!">B</button>
    <button type='roll' class="sheet-skillbutton" title ="Automatique" value="&{template:d10Shooting}{{name=@{ranged_weaponname}}}{{subtags=@{typename}}} {{attack=[[?{Dices}d10<[[@{ranged_type_select}+?{Seuil|4}+@{ranged_accuracy}]]cs1cf11]]}} {{mode=Auto}}  {{damage=@{ranged_dmgBase}/@{ranged_dmgPlus}}} {{usedammo=@{ranged_auto}}} {{magsize=@{ranged_magT}}} {{ammocurrent=[[@{ranged_magA}-@{ranged_auto}]]}} {{ammototal=@{ranged_ammoT}}} {{special=@{ranged_special}}} !modattr --name @{character_name} --repeating_ranged-weapons_$@{wid}_ranged_magA|-@{ranged_auto}!!!">A</button>
      </div> </div>
    </fieldset>
"""
        return ret


class MELEE(generator.Node):
    """MELEE Weapons"""

    def __init__(self, name,nb):
        super(MELEE, self).__init__(name,nb)

    def content(self):
        ret="""    <!--  Melée -->
    <fieldset class="repeating_melee-weapons">
      <div class="quickborder">
        <div class="sheet-row">
         <input class="sheet-skill_name" type="number" name="attr_wid" title="Numero de ligne" />
         <input class="sheet-skill_name" type="text" name="attr_melee_weaponname" title="Nom de l'arme" />
         <label>P</label>
         <input type="number" name="attr_melee_accuracy" title="Précision" />
        </div>
        <div class="sheet-row">
          <label>Type</label>
          <input type="text" name="attr_typename" title="Type d'arme" />
          <select class="sheet-weapon_type_select" name="attr_melee_type_select">
           <option value="@{combat_skilllevel_armescontandantes}">Arme Contandante</option>
           <option value="@{combat_skilllevel_armestranchantes}">Arme Tranchante</option>
           <option value="0">Aucune spécialité</option>
          </select>
        </div>
        <div class="sheet-row">
          <label>Dégats</label>
          <input type="number" name="attr_melee_dmgBase" title="Dégats base" />
          <label>/</label>
          <input type="number" name="attr_melee_dmgPlus" title="Dégats additionels" />
          <label>Spécial</label>
          <input type="text" name="attr_melee_special" title="Spécial" />
          <button type='roll' class="sheet-skillbutton" title ="Attaque" value="&{template:d10Shooting}{{name=@{melee_weaponname}}}{{subtags=@{typename}}} {{attack=[[?{Dices}d10<[[@{melee_type_select}+?{Seuil|4}+@{melee_accuracy}]]cs1cf11]]}} {{damage=@{melee_dmgBase}/+@{melee_dmgPlus}}} {{special=@{melee_special}}}">Attaque</button>
          <button type='roll' class="sheet-skillbutton" title ="Dégats"  value="&{template:d10Shooting}{{name=@{melee_weaponname}}}{{subtags=@{typename}}} {{damagedone=[[(?{Sucesses}-1)*@{melee_dmgPlus}+@{melee_dmgBase}]]}}">Dégats</button>
      </div> </div>
    </fieldset>
"""
        return ret

class CONSOMMABLE(generator.Node):
    """CONSUMMABLES"""

    def __init__(self, name,nb):
        super(CONSOMMABLE, self).__init__(name,nb)

    def content(self):
        return """    <fieldset class="repeating_consumables">
      <div class="quickborder">
        <div class="sheet-row">
         <input class="sheet-skill_name" type="number" name="attr_wid" title="Numero de ligne" />
         <input class="sheet-skill_name" type="text" style="width:250px" name="attr_consumable_name" title="Nom du consommable" />
         <input class="sheet-skill_name" type="text" style="width:200px" name="attr_consumable_type" title="Type de consommable" />
         <label>Nb</label>
         <input type="number" name="attr_consumable_nb" title="Quantité" />
         <button type='roll' class="sheet-skillbutton" title ="Utilisation" value="&{template:d10Shooting}{{name=@{consumable_name}}}{{subtags=@{consumable_type}}} {{special=@{consumable_effect}}} !modattr --name @{character_name} --repeating_consumables_$@{wid}_consumable_nb|-1!!!">Utiliser</button>
        </div>
        <div class="sheet-row">
          <input type="text" style="" name="attr_consumable_effect" style="width:100%" title="Description (short)" />
      </div> </div>
    </fieldset>
"""
