# Generate skills sections and others from a file, on the long run, it should be able to generate the whole sheet

import argparse, sys, os

#
#   <input type="radio" name="attr_tab" class="sheet-tab sheet-tab2" value="2" title="Magie" /><span></span>
#   <input type="radio" name="attr_tab" class="sheet-tab sheet-tab3" value="3" title="Combat" /><span></span>

def printable(name):
    return name.replace(" ","").lower()

def checked(b):
    if b==1:
        return 'checked="checked"'
    return ""

def gen_tab(name,tab_nb):
    return '<input type="radio" name="attr_tab" class="sheet-tab sheet-tab{nb}" value="{nb}" title="{name}" {checked} /><span></span>'.format(name=name,nb=tab_nb,checked=checked(tab_nb))


# <div class="sheet-tab-content sheet-tab1">
#     <div class='sheet-col'>
#       <input type="radio" name="secondary_skills_tab" class="small_tab secondary_skills_tab1" checked="checked" value="1" title="Générales" />
#       <input type="radio" name="secondary_skills_tab" class="small_tab secondary_skills_tab2" value="2" title="Sociales" />
#       <input type="radio" name="secondary_skills_tab" class="small_tab secondary_skills_tab3" value="3" title="Intellectuelles" />

def gen_subtab(name,secname,tab_nb,subtab_nb):
    if subtab_nb==1:
        intro="""<div class="sheet-tab-content sheet-tab{}">
    <div class='sheet-col'>""".format(tab_nb)
    else:
        intro=""
    line="""<input type="radio" name="secondary_skills_tab" class="small_tab secondary_skills_tab{nb}" {check} value="{nb}" title="{name}" />""".format(name=name,nb=subtab_nb,check=checked(subtab_nb))
    return intro+line

 # <!--INTELECTUELLES -->
 #        <h3>Compétences Intellectuelles</h3>
 #        <fieldset class="repeating_intelect-skills">
 #          <input class="sheet-skill_name" type="text" name="attr_intelect_skillname" />
 #          <input type="number" name="attr_intelect_skillcost" title="Coût de la compétence" />
 #          <input type="number" min="-10" max="10" name="attr_intelect_skilllevel" title="Niveau dans la compétence" />
 #          <select class="sheet-skill_select" name="attr_intelect_attribute_select">
 #            <option value="@{base-Force} + @{exal-Force}">For</option>
 #            <option value="@{base-Agilite} + @{exal-Agilite}">Agi</option>
 #            <option value="@{base-Perception} + @{exal-Perception}">Per</option>
 #            <option value="@{base-Charisme} + @{exal-Charisme}">Cha</option>
 #            <option value="@{base-Intelligence} + @{exal-Intelligence}">Int</option>
 #            <option value="@{base-Perception} + @{exal-Perception}">Per</option>
 #            <option value="@{base-Volonte} + @{exal-Volonte}">Vol</option>
 #            <option value="@{base-Psyche} + @{exal-Psyche}">Psy</option>
 #            <option value="@{base-Chance} + @{exal-Chance}">Chn</option>
 #          </select>
 #          <button type='roll' class="sheet-skillbutton" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=@{intelect_skillname}}} {{dice_name=@{dice}}} {{result=[[@{intelect_skilllevel}+(@{intelect_attribute_select})-d@{dice}cs1cf@{dice}]]}} {{threshold=[[@{intelect_skilllevel}+(@{intelect_attribute_select})]]}}"></button>
 #        </fieldset>
 #      </div>

def gen_repeating(name):
    pass

# <!--Fauchage -->
#       <input class="sheet-skill_name" style="margin-right: 4px;" type="text" name="attr_general_skill_Fauchage" disabled="true" value="Fauchage" />
#       <input type="number" min="0" value="0" name="attr_skillcost_Fauchage" title="Coût de la compétence" />
#       <input class="sheet-skill_name" value="0" style="margin-right: 4px;" type="number" min="0" max="10" name="attr_general_skilllevel_Fauchage" title="Niveau dans la compétence" />
#       <select class="sheet-skill_select" style="margin-right:4px" name="attr_Skill_general_attribute_select_Fauchage">
#         <option value="@{base-Force} + @{exal-Force}">For</option>
#         <option value="@{base-Agilite} + @{exal-Agilite}">Agi</option>
#         <option value="@{base-Perception} + @{exal-Perception}">Per</option>
#         <option value="@{base-Charisme} + @{exal-Charisme}">Cha</option>
#         <option value="@{base-Intelligence} + @{exal-Intelligence}">Int</option>
#         <option value="@{base-Perception} + @{exal-Perception}">Per</option>
#         <option value="@{base-Volonte} + @{exal-Volonte}">Vol</option>
#         <option value="@{base-Psyche} + @{exal-Psyche}">Psy</option>
#         <option value="@{base-Chance} + @{exal-Chance}">Chn</option>
#       </select>
#       <button type='roll' class="sheet-skillbutton" value="&{template:d10skillcheck}{{name=@{character_name}}} {{roll_name=@{general_skill_Fauchage}}} {{dice_name=@{dice}}} {{result=[[@{general_skilllevel_Fauchage}+(@{Skill_general_attribute_select_Fauchage})-d@{dice}cs1cf@{dice}]]}} {{threshold=[[@{general_skilllevel_Fauchage}+(@{Skill_general_attribute_select_Fauchage})]]}} "></button>
#       <input type="checkbox" class="sheet-skill_activation" style="margin-right: 4px;" value="1" name="attr_skill_Fauchage_activation" />
#       <input class="sheet-skill_hidden" value="0" type="number" name="attr_general_effective_Fauchage" />
#       <br/>

# <div class="sheet-tab-content sheet-secondary_skills_tab1">
def gen_technique(name,tab_name,tab_nb,first_technique):

    if first_technique:
        intro="""<div class="sheet-tab-content sheet-secondary_skills_tab{}">""".format(name)
    else:
        intro=""
    pass


if __name__ == '__main__':
    # filen=sys.argv[1]
    filen="cyberpnk.txt"

    def parse(filen):
        tab,subtab="",""
        tab_nb,subtab_nb=0,0
        first_technique=True
        try:
            with open(filen) as f:
                for line in f.readlines():
                    if line[0]=="#": # section
                        first_technique=True
                        subtab_content=gen_tab(line[1:],tab_nb)
                        tab=printable(line[1:])
                        print(tab,subtab_content)
                        tab_nb+=1
                    elif line[0]=="@":
                        # first_technique=True
                        subtab_content=gen_subtab(line[1:],tab,tab_nb,subtab_nb)
                        subtab=printable(line[1:])
                        print(subtab,subtab_content)
                    elif line[0]==":":
                        tech_content=gen_technique(line[1:],tab,tab_nb,first_technique)
                        # tech=printable()
        except FileNotFoundError:
            print(filen,"was not found")

    parse(filen)
