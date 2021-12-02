# -*- coding: utf-8 -*-


# content skills sections and others from a file, on the long run, it should be able to content the whole sheet

import argparse, sys, os
import string
# from unidecode import unidecode
# import unicode

def remove_non_ascii(text):
    return "".join([c for c in text if c in string.ascii_letters]).strip(" ")
    # return unidecode(text)

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
        ret+="\n{\n display: block;\n}\n"
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
        ret='<!--  {self.pname} -->\n<div class="sheet-tab-content sheet-tab{self.number}">\n'.format(self=self) # And add all content
        for child in self.children:
            ret+=child.header()
        for child in self.children:
            ret+=child.content()
        return ret

    def css(self):
        ret=" "
        for child in self.children:
            ret+="\ninput.sheet-secondary_{node.pname}_tab{child.number}:checked ~ div.sheet-secondary_{node.pname}_tab{child.number},".format(child=child,node=self)
        ret=ret[:-1]
        ret+="\n{\n display: block;\n}"
        return ret

class SubTab(Node):
    def __init__(self,name,nb):
        super(SubTab,self).__init__(name,nb)

    def header(self):
        return """  <input type="radio" name="secondary_{self.parent.pname}_tab" class="small_tab secondary_{self.parent.pname}_tab{self.number}" value="{self.number}" {self.checked} title="{self.name}" />\n""".format(self=self)

    def content(self):
        ret= '  <div class="sheet-tab-content sheet-secondary_{self.parent.pname}_tab{self.number}">\n'.format(self=self)
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
      <input type="number" min="0" value="0" name="attr_{self.parent.pname}_skillcost_{self.pname}" title="Coût de la compétence" />
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
      <button type='roll' class="sheet-skillbutton" value="&{{template:d10skillcheck}} {{{{name=@{{character_name}}}}}} {{{{roll_name=@{{{self.parent.pname}_skill_{self.pname}}}}}}} {{{{dice_name=@{{dice}}}}}} {{{{result=[[@{{{self.parent.pname}_skilllevel_{self.pname}}}+(@{{skill_{self.parent.pname}_attribute_select_{self.pname}}})-d@{{dice}}cs1cf@{{dice}}]]}}}} {{{{threshold=[[@{{{self.parent.pname}_skilllevel_{self.pname}}}+(@{{skill_{self.parent.pname}_attribute_select_{self.pname}}})]]}}}}"></button>
      <br/>\n""".format(self=self)
        return ret

class SubSkill(Node):
    """Print a subskill."""
    def __init__(self, name,nb,superskill):
        super(SubSkill, self).__init__(name,nb)
        self.superskill=superskill
        print(name,superskill.pname)
    def content(self): # {self.parent.pname} is not needed, else _skilllevel_ cause a confict, legacy keeping I guess ?
        ret="""      <!--{self.name} -->
      <input class="sheet-skill_name" style="margin-right: 4px;" type="text" name="attr_{self.parent.pname}_skill_{self.pname}" disabled="true" value="{self.name}" />
      <input type="number" min="0" value="0" name="attr_{self.parent.pname}_skillcost_{self.pname}" title="Coût de la compétence" />
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
      <button type='roll' class="sheet-skillbutton" value="&{{template:d10skillcheck}} {{{{name=@{{character_name}}}}}} {{{{roll_name=@{{{self.parent.pname}_skill_{self.pname}}}}}}} {{{{dice_name=@{{dice}}}}}} {{{{result=[[@{{{self.parent.pname}_skilllevel_{self.pname}}}+(@{{skill_{self.parent.pname}_attribute_select_{self.pname}}}+@{{{self.parent.pname}_skilllevel_{self.superskill.pname}}})-d@{{dice}}cs1cf@{{dice}}]]}}}} {{{{threshold=[[@{{{self.parent.pname}_skilllevel_{self.pname}}}+@{{{self.parent.pname}_skilllevel_{self.superskill.pname}}}+(@{{skill_{self.parent.pname}_attribute_select_{self.pname}}})]]}}}}"></button>
      <br/>\n""".format(self=self)
        return ret

class Repeating(Node):
    """Repeating section"""

    def __init__(self, name,nb):
        super(Repeating, self).__init__(name,nb)

    def content(self):
        ret="""      <!-- {node.pname} -->
      <fieldset class="repeating_{node.pname}-skills">
      <input class="sheet-skill_name" type="text" name="attr_{node.pname}_skillname" />
      <input type="number" name="attr_{node.pname}_skillcost" title="Coût de la compétence" />
      <input type="number" min="-10" max="10" name="attr_{node.pname}_skilllevel" title="Niveau dans la compétence" />
      <select class="sheet-skill_select" name="attr_{node.pname}_attribute_select">
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
      <button type='roll' class="sheet-skillbutton" value="&{{template:d10skillcheck}}\
 {{{{name=@{{character_name}}}}}}\
 {{{{roll_name=@{{{node.pname}_skillname}}}}}}\
 {{{{dice_name=@{{dice}}}}}}\
 {{{{result=[[@{{{node.pname}_skilllevel}}+(@{{{node.pname}_attribute_select}})-d@{{dice}}cs1cf@{{dice}}]]}}}}\
 {{{{threshold=[[@{{{node.pname}_skilllevel}}+(@{{{node.pname}_attribute_select}})]]}}}}">\
      </button>
      </fieldset> 
      <br/>\n""".format(node=self)
        return ret

if __name__ == '__main__':
    # filen=sys.argv[1]
    # filen="light.txt"
    import customs as custom_skills
    filen="cyberpnk.txt"
    output="systemd10cyberpunk.html"
    outcss="systemd10cyberpunk.css"
    def parse(filen):
        root=Root()
        active_tab,active_subtab=None,None
        tab_nb,subtab_nb,skill_nb,repeating_nb=1,1,1,1
        mainskill=None
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
                    elif line[0]=="=":
                        tech_content=Skill(line[1:-1],skill_nb)
                        active_subtab.addchild(tech_content)
                        mainskill=tech_content
                        skill_nb+=1
                    elif line[0]=="-":
                        tech_content=SubSkill(line[1:-1],skill_nb,mainskill)
                        active_subtab.addchild(tech_content)
                        skill_nb+=1
                    elif line[0]==".":
                        tech_content=Repeating(line[1:-1],repeating_nb)
                        active_subtab.addchild(tech_content)
                        repeating_nb+=1
                    elif line[0]=="#":
                        skill=custom_skills.__getattribute__(line[2:-1])("","")
                        active_subtab.addchild(skill)
                        repeating_nb+=1 # ???
        except FileNotFoundError:
            print(filen,"was not found")
        return root
    root=parse(filen)
    import base
    with open(output,"w",encoding="utf-8") as f:
        f.write(base.head)
        f.write(base.script)
        f.write(base.header)
        f.write(root.content())
        f.write(base.footer)
    with open(outcss,"w",encoding="utf-8") as f:
        f.write(root.css())
        f.write(base.css_footer)
