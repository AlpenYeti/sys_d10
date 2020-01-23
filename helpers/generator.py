# -*- coding: utf-8 -*-


# content skills sections and others from a file, on the long run, it should be able to content the whole sheet

import argparse, sys, os
from unidecode import unidecode
# import unicode

def remove_non_ascii(text):
    return unidecode(text)

class Node(object):
    """Generic Node."""
    def __init__(self, name,nb):
        self.name = name#name.strip(" ")
        self.number=nb
        self.children=[]
        self.checked=""
        self.parent=None
        self.pname=u""+remove_non_ascii(self.name.replace(" ","")).lower()
        if nb==1:
            self.checked='checked="checked"'

    def content(self):
        return ""

    def header(self):
        return ""

    def css(self):
        return ""

    def addchild(self,child):
        self.children+=[child]
        child.parent=self

class Root(Node):
    """docstring for Root."""
    def __init__(self):
        super(Root,self).__init__("",0)

    def generate(self):
        "Return the whole tree, printable"
        return self.content()

    def content(self):
        ret=""
        for child in self.children:
            ret+=child.header() # Ligne de chaque tab direct, puis tout
        for child in self.children:
            ret+=child.content()
            ret+="</div>\n"
        return ret

    def css(self):
        "Return the whole css, printable"
        ret="div.sheet-tab-content { display: none; }"
        for child in self.children:
            ret+="\ninput.sheet-tab{node.number}:checked ~ div.sheet-tab{node.number},".format(node=child)
        ret=ret[:-1]
        ret+="\n{display: block;}\n"
        for child in self.children:
            ret+=child.css()
        return ret

class Tab(Node):
    """Tab node, contains"""

    def __init__(self, name,nb):
        super(Tab, self).__init__(name,nb)

    def header(self): # Comes first
        return '<input type="radio" name="attr_tab" class="sheet-tab sheet-tab{self.number}" value="{self.number}" title="{self.name}" {self.checked}/><span></span>\n'.format(self=self)

    def content(self):
        ret='<div class="sheet-tab-content sheet-tab{self.number}">\n  <div class="sheet-col">\n'.format(self=self) # And add all content
        for child in self.children:
            ret+=child.header()
        ret+="  </div>\n"
        for child in self.children:
            ret+=child.content()
        return ret
    def css(self):
        ret=" "
        for child in self.children:
            ret+="\ninput.sheet-{node.pname}{child.number}:checked ~ div.sheet-{node.pname}{child.number},".format(child=child,node=self)
        ret=ret[:-1]
        ret+="\n{display: block;}\n"
        return ret
class SubTab(Node):
    def __init__(self,name,nb):
        super(SubTab,self).__init__(name,nb)

    def header(self):
        return """    <input type="radio" name="secondary_tab_{self.parent.pname}" class="small_tab secondary_tab_{self.parent.pname}{self.number}" {self.checked} value="{self.number}" title="{self.name}" />\n""".format(self=self)

    def content(self):
        ret= '  <div class="sheet-tab-content sheet-secondary_tab_{self.parent.pname}{self.number}">\n'.format(self=self)
        ret+="    <!-- {self.name} -->\n    <h3>{self.name}</h3>\n".format(self=self)
        for child in self.children:
            ret+=child.content()
        ret+="  </div>\n"
        return ret
    def css(self):
        return ""

class Skill(Node):
    """Print a skill."""
    def __init__(self, name,nb):
        super(Skill, self).__init__(name,nb)

    def content(self): # {self.parent.pname} is not needed, else _skilllevel_ cause a confict, legacy keeping I guess ?
        ret="""      <!--{self.name} -->
      <input class="sheet-skill_name" style="margin-right: 4px;" type="text" name="attr_{self.parent.pname}_skill_{self.pname}" disabled="true" value="{self.name}" />
      <input type="number" min="0" value="0" name="attr_skillcost_Fauchage" title="Coût de la compétence" />
      <input class="sheet-skill_name" value="0" style="margin-right: 4px;" type="number" min="0" max="10" name="attr_{self.parent.pname}_skilllevel_{self.pname}" title="Niveau dans la compétence" />
      <select class="sheet-skill_select" style="margin-right:4px" name="attr_skill_{self.parent.pname}_attribute_select_{self.pname}">
        <option value="@{{base-Force}} + @{{exal-Force}}">For</option>
        <option value="@{{base-Agilite}} + @{{exal-Agilite}}">Agi</option>
        <option value="@{{base-Perception}} + @{{exal-Perception}}">Per</option>
        <option value="@{{base-Charisme}} + @{{exal-Charisme}}">Cha</option>
        <option value="@{{base-Intelligence}} + @{{exal-Intelligence}}">Int</option>
        <option value="@{{base-Perception}} + @{{exal-Perception}}">Per</option>
        <option value="@{{base-Volonte}} + @{{exal-Volonte}}">Vol</option>
        <option value="@{{base-Psyche}} + @{{exal-Psyche}}">Psy</option>
        <option value="@{{base-Chance}} + @{{exal-Chance}}">Chn</option>
      </select>
      <button type='roll' class="sheet-skillbutton" value="&{{template:d10skillcheck}} {{{{name=@{{character_name}}}}}} {{{{roll_name=@{{{self.parent.pname}_skill_{self.pname}}}}}}} {{{{dice_name=@{{dice}}}}}} {{{{result=[[@{{{self.parent.pname}_skilllevel_{self.pname}}}+(@{{skill_{self.parent.pname}_attribute_select_{self.pname}}})-d@{{{{dice}}cs1cf@{{dice}}]]}}}} {{{{threshold=[[@{{{self.parent.pname}_skilllevel_{self.pname}}}+(@{{skill_{self.parent.pname}_attribute_select_{self.pname}}})]]}}}}"></button>
      <br/>\n""".format(self=self)
        return ret

#
 # <!--INTELECTUELLES -->
 #        <h3>Compétences Intellectuelles</h3>
 #        <fieldset class="repeating_intelect-skills">
 #          <input class="sheet-skill_name" type="text" name="attr_intelect_skillname" />
 #          <input type="number" name="attr_intelect_skillcost" title="Coût de la compétence" />
 #          <input type="number" min="-10" max="10" name="attr_intelect_skilllevel" title="Niveau dans la compétence" />
 #          <select class="sheet-skill_select" name="attr_intelect_attribute_select">
 #            <option value="@{{base-Force}} + @{{exal-Force}}">For</option>
 #            <option value="@{{base-Agilite}} + @{{exal-Agilite}}">Agi</option>
 #            <option value="@{{base-Perception}} + @{{exal-Perception}}">Per</option>
 #            <option value="@{{base-Charisme}} + @{{exal-Charisme}}">Cha</option>
 #            <option value="@{{base-Intelligence}} + @{{exal-Intelligence}}">Int</option>
 #            <option value="@{{base-Perception}} + @{{exal-Perception}}">Per</option>
 #            <option value="@{{base-Volonte}} + @{{exal-Volonte}}">Vol</option>
 #            <option value="@{{base-Psyche}} + @{{exal-Psyche}}">Psy</option>
 #            <option value="@{{base-Chance}} + @{{exal-Chance}}">Chn</option>
 #          </select>
 #          <button type='roll' class="sheet-skillbutton" value="&{template:d10skillcheck}{{name=@{{character_name}}}} {{roll_name=@{{intelect_skillname}}}} {{dice_name=@{{dice}}}} {{result=[[@{{intelect_skilllevel}}+(@{{intelect_attribute_select}})-d@{{dice}}cs1cf@{{dice}}]]}} {{threshold=[[@{{intelect_skilllevel}}+(@{{intelect_attribute_select}})]]}}"></button>
 #        </fieldset>
 #      </div>


if __name__ == '__main__':
    # filen=sys.argv[1]
    # filen="light.txt"
    filen="cyberpnk.txt"
    output="gen.html"
    outcss="gencss.css"
    def parse(filen):
        root=Root()
        active_tab,active_subtab=None,None
        tab_nb,subtab_nb,skill_nb=1,1,1
        try:
            with open(filen,encoding="utf-8") as f:
                for line in f.readlines():
                    if line[0]=="@": # Tab
                        active_tab=Tab(line[1:-1],tab_nb)
                        root.addchild(active_tab)
                        tab_nb+=1
                        subtab_nb=1
                    elif line[0]=="+":
                        active_subtab=SubTab(line[1:-1],subtab_nb)
                        active_tab.addchild(active_subtab)
                        subtab_nb+=1
                        skill_nb=1
                    elif line[0]=="-":
                        tech_content=Skill(line[1:-1],skill_nb)
                        active_subtab.addchild(tech_content)
                        skill_nb+=1
        except FileNotFoundError:
            print(filen,"was not found")
        return root
    root=parse(filen)
    with open(output,"w",encoding="utf-8") as f:
        f.write(root.content())
    with open(outcss,"w",encoding="utf-8") as f:
        f.write(root.css())
