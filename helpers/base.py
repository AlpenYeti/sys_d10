head="""<head>
  <link rel="stylesheet" type="text/css" href="style.css"/>
  <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet"/>
"""
script="""  <script type="text/worker">
  // Life_Points
// on("change:base-Force change:base-Agilite change:base-Volonte change:general_skilllevel_Endurance_surnaturelle", function() {
//   getAttrs(["base-Force","base-Agilite","base-Volonte","general_skilllevel_Endurance_surnaturelle"], function(values) {
//     setAttrs({"Life_Points_max":Number(values['base-Force'])+Number(values['base-Volonte'])+Number(values['base-Agilite'])+Number(values.general_skilllevel_Endurance_surnaturelle)*2+10});
//     setAttrs({"Life_Points_maximum":Number(values['base-Force'])+Number(values['base-Volonte'])+Number(values['base-Agilite'])+Number(values.general_skilllevel_Endurance_surnaturelle)*2+10});
//   });
// });
// Endurance_Points
on("change:base-Force change:base-Agilite change:general_skilllevel_Endurance_surnaturelle", function() {
  getAttrs(["base-Force","base-Agilite","general_skilllevel_Endurance_surnaturelle"], function(values) {
    setAttrs({"Endurance_Points_maximum":Number(values['base-Force'])*4});
    setAttrs({"Endurance_Points_max":Number(values['base-Force'])*4});
  });
});
// undescored_name
// on("change:character_name change:character_race", function() {
//   getAttrs(["character_name"], function(values) {
//     setAttrs({"undescored_name":values.character_name.replace(/ /g,"_").replace(/'/g,"/")});
//   });
// });
// dice_with_tanscendance
  </script>
"""
header="""
<div class="sheet-content">
  <div class="sheet-center">
    <input type="text" class="sheet-bigname" name="attr_character_name" placeholder="Nom"/>
    <span style="color:#ffffff;" name="attr_undescored_name" /><span/><br/>
    <input type="text" class="sheet-mediumname" name="attr_character_race" placeholder="Race"/>
  </div>
  <br/>
  <div class="sheet-2colrow">
    <div class='sheet-col'>
      <h3 class="sheet-center">Ressources</h3>
      <table class="sheet-center sheet-black">
        <tr>
          <td><h4>Points de Vie</h4></td>
          <td><input type="number" class="sheet-trait" name="attr_Life_Points_head" title="Tête" value="0"/></td>
          <td><input type="number" class="sheet-trait" name="attr_Life_Points_body" title="Torse" value="0"/></td>
          <td><input type="number" class="sheet-trait" name="attr_Life_Points_left_arm" title="Bras gauche" value="0"/></td>
          <td><input type="number" class="sheet-trait" name="attr_Life_Points_right_arm" title="Bras droit" value="0"/></td>
          <td><input type="number" class="sheet-trait" name="attr_Life_Points_left_leg" title="Jambe gauche" value="0"/></td>
          <td><input type="number" class="sheet-trait" name="attr_Life_Points_right_leg" title="Jambe droite" value="0"/></td>
          <!-- <td><input class="sheet-trait" disabled="true" name="attr_mirror_Life_Points" value="@{Life_Points_maximum}"/></td> -->
        </tr>
        <tr>
          <td><h4>Points de Fatigue</h4></td>
          <td><input type="number" class="sheet-trait" name="attr_Endurance_Points" value="0"/></td>
          <td><input class="sheet-trait" disabled="true" name="attr_mirror_Endurance_Points" value="@{Endurance_Points_maximum}"/></td>
        </tr>
      </table>
    </div>
    <div class="sheet-col">
      <table class="sheet-center sheet-black">
        <tr>
          <td><h3 class="sheet-center">Points de compétence :</h3></td>
          <br/>
        </tr>
        <tr>
          <td><input type="number" class="sheet-trait" name="attr_Character_points_spent" value="0"/> Utilisés</td>
          <td rowspan="2">
            <select class="sheet-dice_select sheet-dice" name="attr_dice">
              <option value="2">d2</option>
              <option value="4">d4</option>
              <option value="6">d6</option>
              <option value="8">d8</option>
              <option value="10" selected>d10</option>
              <option value="12">d12</option>
              <option value="20">d20</option>
              <option value="30">d30</option>
              <option value="100">d100</option>
              <option value="1000">d1000</option>
              <option value="10000">d10000</option>
            </select>
          </td>
        </tr>
        <tr>
          <td><input type="number" class="sheet-trait" name="attr_Character_points_unspent" value="0"/> Restants</td>
        </tr>
      </table>
    </div>
  </div>
  <div class='sheet-2colrow'>
    <div class='sheet-col'>
      <h3 class="sheet-center">Caractéristiques</h3>
      <table class="">
        <tr>
          <th>Carac</th>
          <th>Valeur</th>
          <th>Bonus</th>
          <th colspan="2">Lancer</th>
        </tr>
        <tr>
          <td>Force</td>
          <td><input type="number" class="sheet-trait" name="attr_base-Force" title="Force de base" value="0" min="0" max="10" /></td>
          <td><input type="number" class="sheet-trait" name="attr_exal-Force" title="Modificateur" value="0" /></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Force}} {{dice_name=@{dice}}} {{result=[[(@{base-Force}+@{exal-Force})*2-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Force}+@{exal-Force})*2]]}}"></button></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Force brute}} {{dice_name=@{dice}}} {{result=[[(@{base-Force}+@{exal-Force})-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Force}+@{exal-Force})]]}}">Brut</button></td>
        </tr>
        <tr>
          <td>Agilité</td>
          <td><input type="number" class="sheet-trait" name="attr_base-Agilite" title="Agilité de base" value="0" min="0" max="10"/></td>
          <td><input type="number" class="sheet-trait" name="attr_exal-Agilite" title="Modificateur" value="0"/></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Agilité}} {{dice_name=@{dice}}} {{result=[[(@{base-Agilite}+@{exal-Agilite})*2-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Agilite}+@{exal-Agilite})*2]]}}"></button></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Agilité}} {{dice_name=@{dice}}} {{result=[[(@{base-Agilite}+@{exal-Agilite})-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Agilite}+@{exal-Agilite})]]}}">Brut</button></td>
        </tr><tr>
          <td>Perception</td>
          <td><input type="number" class="sheet-trait" name="attr_base-Perception" title="Perception de base" value="0" min="0" max="10"/></td>
          <td><input type="number" class="sheet-trait" name="attr_exal-Perception" title="Modificateur" value="0"/></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Perception}} {{dice_name=@{dice}}} {{result=[[(@{base-Perception}+@{exal-Perception})*2-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Perception}+@{exal-Perception})*2]]}}"></button></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Perception}} {{dice_name=@{dice}}} {{result=[[(@{base-Perception}+@{exal-Perception})-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Perception}+@{exal-Perception})]]}}">Brut</button></td>
        </tr><tr>
          <td>Charisme</td>
          <td><input type="number" class="sheet-trait" name="attr_base-Charisme" title="Charisme de base" value="0" min="0" max="10"/></td>
          <td><input type="number" class="sheet-trait" name="attr_exal-Charisme" title="Modificateur" value="0"/></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Charisme}} {{dice_name=@{dice}}} {{result=[[(@{base-Charisme}+@{exal-Charisme})*2-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Charisme}+@{exal-Charisme})*2]]}}"></button></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Charisme}} {{dice_name=@{dice}}} {{result=[[(@{base-Charisme}+@{exal-Charisme})-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Charisme}+@{exal-Charisme})]]}}">Brut</button></td>
        </tr>
      </table>
    </div>
    <div class='sheet-col'>
      <h3 class="sheet-center">&nbsp;</h3>
      <table class="">
        <tr>
          <th>Carac</th>
          <th>Valeur</th>
          <th>Bonus</th>
          <th colspan="2">Lancer</th>
        </tr>
        <tr>
          <td>Intelligence</td>
          <td><input type="number" class="sheet-trait" name="attr_base-Intelligence" title="Intelligence de base" value="0" min="0" max="10" /></td>
          <td><input type="number" class="sheet-trait" name="attr_exal-Intelligence" title="Modificateur" value="0" /></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Intelligence}} {{dice_name=@{dice}}} {{result=[[(@{base-Intelligence}+@{exal-Intelligence})*2-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Intelligence}+@{exal-Intelligence})*2]]}}"></button></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Intelligence brute}} {{dice_name=@{dice}}} {{result=[[(@{base-Intelligence}+@{exal-Intelligence})-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Intelligence}+@{exal-Intelligence})]]}}">Brut</button></td>
        </tr>
        <tr>
          <td>Volonté</td>
          <td><input type="number" class="sheet-trait" name="attr_base-Volonte" title="Volonté de base" value="0" min="0" max="10"/></td>
          <td><input type="number" class="sheet-trait" name="attr_exal-Volonte" title="Modificateur" value="0"/></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Volonté}} {{dice_name=@{dice}}} {{result=[[(@{base-Volonte}+@{exal-Volonte})*2-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Volonte}+@{exal-Volonte})*2]]}}"></button></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Volonté}} {{dice_name=@{dice}}} {{result=[[(@{base-Volonte}+@{exal-Volonte})-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Volonte}+@{exal-Volonte})]]}}">Brut</button></td>
        </tr><tr>
          <td>Psyché</td>
          <td><input type="number" class="sheet-trait" name="attr_base-Psyche" title="Psyché de base" value="0" min="0" max="10"/></td>
          <td><input type="number" class="sheet-trait" name="attr_exal-Psyche" title="Modificateur" value="0"/></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Psyché}} {{dice_name=@{dice}}} {{result=[[(@{base-Psyche}+@{exal-Psyche})*2-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Psyche}+@{exal-Psyche})*2]]}}"></button></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Psyché}} {{dice_name=@{dice}}} {{result=[[(@{base-Psyche}+@{exal-Psyche})-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Psyche}+@{exal-Psyche})]]}}">Brut</button></td>
        </tr><tr>
          <td>Chance</td>
          <td><input type="number" class="sheet-trait" name="attr_base-Chance" title="Chance de base" value="0" min="0" max="10"/></td>
          <td><input type="number" class="sheet-trait" name="attr_exal-Chance" title="Modificateur" value="0"/></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Chance}} {{dice_name=@{dice}}} {{result=[[(@{base-Chance}+@{exal-Chance})*2-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Chance}+@{exal-Chance})*2]]}}"></button></td>
          <td><button type='roll' class="sheet-trait_roll" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=Chance}} {{dice_name=@{dice}}} {{result=[[(@{base-Chance}+@{exal-Chance})-d@{dice}cs1cf@{dice}]]}} {{threshold=[[(@{base-Chance}+@{exal-Chance})]]}}">Brut</button></td>
        </tr>
      </table>
    </div>
  </div>
  <br/>
"""

footer="""
</div>
<rolltemplate class="sheet-rolltemplate-d10skillcheck">
  <table class="">
    <tr><th class="roll-title">{{name}} &mdash; {{roll_name}}</th></tr>
    <tr><td class="roll-attr"> Test au d{{dice_name}} seuil {{threshold}} </td></tr>
    <tr>
      {{#rollWasCrit() result}}
        <td class="roll-crit">Critique ! {{result}}<span class="inline fullcrit">x2</span> degrés de réussite</td>
      {{/rollWasCrit() result}}
      {{#^rollWasCrit() result}}
        {{#rollWasFumble() result}}
          {{#rollGreater() result 1}}
            <td class="roll-fumble">Échec critique ! {{result}}<span class="inline fullfail">/2</span> degrés de réussite</td>
          {{/rollGreater() result 1}}
          {{#rollBetween() result 0 1}}
            <td class="roll-fumble">Échec critique ! {{result}}<span class="inline fullfail">/2</span> degré de réussite</td>
          {{/rollBetween() result 0 1}}
          {{#rollLess() result 0}}
            <td class="roll-fumble">Échec critique ! {{result}}<span class="inline fullfail">x2</span> degrés d'échec</td>
          {{/rollLess() result 0}}
        {{/rollWasFumble() result}}
        {{#^rollWasFumble() result}}
          {{#rollGreater() result 1}}
            <td class="roll-sucess">{{result}} degrés de réussite</td>
          {{/rollGreater() result 1}}
          {{#rollBetween() result 0 1}}
            <td class="roll-sucess">{{result}} degré de réussite</td>
          {{/rollBetween() result 0 1}}
          {{#rollLess() result 0}}
            <td class="roll-fail">{{result}} degrés d'échec</td>
          {{/rollLess() result 0}}
        {{/^rollWasFumble() result}}
      {{/^rollWasCrit() result}}
    </tr>
  </table>
</rolltemplate>
<rolltemplate class="sheet-rolltemplate-d10init">
  <table class="">
    <tr><th class="roll-title">{{name}} &mdash; {{roll_name}}</th></tr>
    <tr><td class="roll-sucess"> 1d10+{{value}} = {{result}}
      {{#rollWasCrit() result}}
        <span class="inline fullcrit">+{{base}}</span>
      {{/rollWasCrit() result}}
      {{#rollWasFumble() result}}
        {{result}}<span class="inline fullfail">-{{base}}</span>
      {{/rollWasFumble() result}}
    </td></tr>
  </table>
</rolltemplate>
"""
css_footer="""input.sheet-tab{
  -moz-appearance: none;
  width:150px;
  height: 20px;
  top: 5px;
  left: 6px;
  margin: 5px;
  cursor: pointer;
  z-index: 1;
  content: attr(title);
}
input.sheet-tab::before{
  -moz-appearance: none;
  content: attr(title);
  border-radius:.5em;
  border:2px solid black;
  text-align: center;
  display: inline-block;
  background: black;
  color:white;
  width: 150px;
  height: 20px;
  font-size: 18px;
}
input.sheet-tab:checked::before{
  -moz-appearance: none;
  background:#CCCCCC;
  color:black;
  border-radius:.5em;
  border:2px solid black;
}

input.sheet-small_tab{
  -moz-appearance: none;
  width:120px;
  height: 20px;
  cursor: pointer;
  z-index: 1;
  margin:5px;
}
input.sheet-small_tab::before{
  -moz-appearance: none;
  content: attr(title);
  border-radius:.5em;
  text-align: center;
  display: inline-block;
  color:white;
  background:black;
  border:2px solid black;
  width: 120px;
  height:20px;
  font-size: 14px;
}
input.sheet-small_tab:checked::before{
  -moz-appearance: none;
  border:2px solid black;
  background:#CCCCCC;
  color:black;
  border-radius:.5em;
}

input.sheet-skill_name{
  -moz-appearance: none;
  width:400px;
}
input.sheet-skill_hidden{
  visibility: hidden;
}
div.sheet-tab-content{
  border-top-color: #000;
  margin: 2px 0 0 0;
}
select.sheet-skill_select{
  width:55px;
  margin-bottom:-1px;
}
select.sheet-dice_select{
  width:85px;
  margin-bottom:-1px;
}
.sheet-trait{
  width: 30px;
}
.sheet-numberbox {
  width: 50px;
}

.sheet-rolltemplate-d10init table,
.sheet-rolltemplate-d10skillcheck table {
  border-radius: 6px;
  width:100%;
  padding:0px;
  margin:0px;
  padding: 2px;
  border: 1px solid;
  background-color: #ffffff;
  border-width: 1px;
  border-style: solid;
  border-color: #000;
  border-image-source: none;
}
.sheet-rolltemplate-d10init .sheet-roll-title,
.sheet-rolltemplate-d10init th,
.sheet-rolltemplate-d10skillcheck .sheet-roll-title,
.sheet-rolltemplate-d10skillcheck th {
  color: rgb(42, 42, 42);
  padding:0px;
  margin:0px;
  padding-left: 5px;
  font-size: 1.2em;
  text-align: left;
  font-family: "Times New Roman", Times, serif;
  font-variant: small-caps;
  text-transform: capitalize;
  border-width: 0px;
}
.sheet-rolltemplate-d10init .sheet-roll-attr,
.sheet-rolltemplate-d10skillcheck .sheet-roll-attr{
    color: #555555;
    font-size: 1em;
    font-style: italic;
    padding:0px;
    margin:0px;
    padding-left: 9px;
    border-width: 0px;
    margin-top: -10px;
}
.sheet-rolltemplate-d10init .sheet-roll-sucess,
.sheet-rolltemplate-d10skillcheck .sheet-roll-sucess ,
.sheet-rolltemplate-d10skillcheck .sheet-roll-fail {
  padding:0px;
  margin:0px;
  border-width: 0px;
  padding-left: 5px;
}
.sheet-rolltemplate-d10skillcheck .sheet-roll-crit {
  padding:0px;
  margin:0px;
  border-width: 0px;
  padding-left: 5px;
  background-color:#b0d6ad;
}
.sheet-rolltemplate-d10skillcheck .sheet-roll-fumble {
  padding-left: 5px;
  border-width: 0px;
  background-color:#d6adad;
}
.sheet-rolltemplate-d10init .sheet-inline,
.sheet-rolltemplate-d10init .inlinerollresult,
.sheet-rolltemplate-d10skillcheck .sheet-inline,
.sheet-rolltemplate-d10skillcheck .inlinerollresult  {
    background-color: transparent;
    border: none;
    font-weight: bold;
    padding:0px;
    font-family: "Times New Roman", Times, serif;
}
.sheet-rolltemplate-d10skillcheck .sheet-inline.sheet-fullcrit,
.sheet-rolltemplate-d10skillcheck .inlinerollresult.fullcrit {
	color: #3FB315;
    border: none;
}
.sheet-rolltemplate-d10skillcheck .sheet-inline.sheet-fullfail,
.sheet-rolltemplate-d10skillcheck .inlinerollresult.fullfail {
	color: #B31515;
  border: none;
}
.sheet-rolltemplate-d10skillcheck .inlinerollresult.importantroll {
	color: #4A57ED;
  border: none;
}

.sheet-rolltemplate-d10fight-blob{
  border-radius: 6px;
  border: 1px solid #898989;
  z-index: 1;
}
.sheet-rolltemplate-d10fight table{
  padding:0px;
  margin:0px;
  text-align: left;
  width:100%;
  border:none;
  cellpadding:3px;
  cellspacing:0px;
}
.sheet-rolltemplate-d10fight .sheet-sum{
  padding:0px;
  margin:0px;
  border:none;
  text-align: right;
  padding-right:10px;
}
.sheet-rolltemplate-d10fight .sheet-sucess,
.sheet-rolltemplate-d10fight .sheet-line{
  padding:0px;
  margin:0px;
  padding-left: 3px;
  border:none;
}
.sheet-rolltemplate-d10fight .sheet-critical{
  padding:0px;
  margin:0px;
  border:none;
  padding-left: 3px;
  border-radius: 4px;
  background-color:#b0d6ad;
}
.sheet-rolltemplate-d10fight .sheet-hit{
  padding:0px;
  margin:0px;
  padding-left: 3px;
  border-radius: 4px;
  background-color:#b0d6ad;
  border:none;
}
.sheet-rolltemplate-d10fight .sheet-miss{
  padding:0px;
  margin:0px;
  padding-left: 3px;
  border:none;
  border-radius: 4px;
  background-color:#d6adad;
}
.sheet-rolltemplate-d10fight .sheet-name{
  padding:0px;
  padding-left: 3px;
  margin:0px;
  border:none;
  border-radius: 4px;
  border-bottom-left-radius: 2px;
  border-bottom-right-radius: 2px;
  background-color: #999999;
}
.sheet-rolltemplate-d10fight .sheet-additional{
  padding:0px;
  margin:0px;
  border:none;
  padding-left:10px;
}
.sheet-rolltemplate-d10fight-grey{
  color: #999999;
}
.sheet-rolltemplate-d10fight-green{
  color: #009900;
}
.sheet-rolltemplate-d10fight a,
.sheet-rolltemplate-d10fight a[href^="!"],
.sheet-rolltemplate-d10fight a[href^="~"]{
  text-align:right;
  background-color: #999999; !important
}
"""
