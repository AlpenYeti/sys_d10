#!/usr/bin/python
# -*- coding: utf-8 -*-

# Not actually part of the project; just easier to maintain everything here

import sys,os
try:
    import Blessings
except:
    #print("Blessings not found, no pretty printing")
    pass

try:
    args=sys.argv[1:]
    command=sys.argv[1]
except:
    print("No command specified, just outputing the list")
    command="print"


"""var d_vars={"nb_dices":0,"perfection":0,"defense_i_0":0,"defense_i_1":0,"defense_i_2":0,"rempart_p":0,
"technique_m":0,"coup_d":0,"coup_d_results":[],"fauchage":0,"exploiter_p_0":0,"exploiter_p_1":0,
"exploiter_p_2":0,"tir_p_0":0,"tir_p_1":0,"tir_i":0,"charge":0,"charge_i":0,"nb_2add":0,"nb_2sub":0,
"relances":0,"seuil":0,"nb_flat_dices":0,"action":"","flat_dices":[],"results":[],"technique_result":0,
"cleave":[],"on_hit_c":0,"attribute":0,"encaissement":0,"encaissement_dices":"","encaissement_result":0,
"replace":-1,"add_to_all":0,"max_dices":-1,"player_name":""};"""

list=[]
#list.append(['varname','Pretty name','nb_args','type','code','id','default'])
list.append(['perfection','Perfection',1,'int','P',0,0])
list.append(['defense_i_0','Defence impénétrable simple',2,'int','I',1,0])
list.append(['defense_i_1','Defence impénétrable expert',2,'int','I',2,0])
list.append(['defense_i_2','Defence impénétrable meta',2,'int','I',4,0])
list.append(['rempart_p','Rempart parfait',1,'int','R',0,0])
list.append(['technique_m','Perfection',1,'int','M',0,0])
list.append(['coup_d','Coup_déchirant',1,'int','D',0,0])
list.append(['fauchage','Fauchage',1,'int','F',0,0])
list.append(['exploiter_p_0','Exploiter_les_points_faibles simple',2,'int','E',1,0])
list.append(['exploiter_p_1','Exploiter_les_points_faibles expert',2,'int','E',2,0])
list.append(['exploiter_p_2','Exploiter_les_points_faibles meta',2,'int','E',4,0])
list.append(['tir_p_0','Tir_précis expert',2,'int','T',2,0])
list.append(['tir_p_1','Tir_précis meta',2,'int','T',4,0])
list.append(['tir_i','Tir_implacable',1,'int','i',0,0])
list.append(['charge','Charge',1,'int','C',0,0])
list.append(['charge_i','Charge_indomptable',1,'int','N',0,0])
list.append(['nb_2add','Nombre à ajouter',1,'int','+',0,0])
list.append(['nb_2sub','Nombre a soustraire',1,'int','-',0,0])
list.append(['relances','Relances',1,'int','r',0,0])
list.append(['seuil','Seuil',1,'int','s',0,0])
list.append(['action','Type d\'Action',1,'str','a',0,'""'])
list.append(['flat_dices','Des fixes',1,'int','d',0,"[]",
"@flat_dices[@flat_dices]=type({tab+1});\n@nb_flat_dices++;"])
list.append(['on_hit_c','Dégats a l\'impact critique',1,'int','H',0,0])
list.append(['attribute','Caractéristique',1,'int','A',0,0])
list.append(['encaissement','Encaissement',2,'int','S',0,0,])
list.append(['replace','Des de substitution',1,'int','L',0,-1])
list.append(['add_to_all','Valeur d\'ajout aux des',1,'int','l',0,0])
list.append(['max_dices','Nombre de des max',1,'int','m',0,-1])
list.append(['player_name','Nom du joueur',1,'int',':',0,'""'])

list.append(['nb_dices','Nombre de des',1,'int','',0,0])
list.append(['nb_flat_dices','Nombre de des fixes',1,'int','',0,0])
list.append(['encaissement_dices','Perfection',1,'int','',0,'""'])
list.append(['results','Resultats',1,'int','',0,"[]"])
list.append(['cleave','Fauchage',1,'int','',0,"[]"])
list.append(['encaissement_result','Resultat d\'encaissement',1,'int','',0,0])
list.append(['technique_result','Dégats technique martiale',1,'int','',0,0])
list.append(['coup_d_results','Coup déchirant results',1,'int','',0,"[]"])

## Commands
def initialise(args):
    text="var d_vars={"
    for line in list:
        text+='"{}":{},'.format(line[0],line[6])
    text=text[:-1]+'};'
    print(text)
    return text

def pprint(args):
    for i in list:
        print(i)

def check_init(args):
    try:
        test_values=args[1]
    except:
        test_values={"nb_dices":0,"perfection":0,"defense_i_0":0,"defense_i_1":0,
        "defense_i_2":0,"rempart_p":0,"technique_m":0,"coup_d":0,"coup_d_results":"[]",
        "fauchage":0,"exploiter_p_0":0,"exploiter_p_1":0,"exploiter_p_2":0,"tir_p_0":0,
        "tir_p_1":0,"tir_i":0,"charge":0,"charge_i":0,"nb_2add":0,"nb_2sub":0,"relances":0,
        "seuil":0,"nb_flat_dices":0,"action":'""',"flat_dices":"[]","results":"[]","technique_result":0,
         "cleave":"[]","on_hit_c":0,"attribute":0,"encaissement":0,"encaissement_dices":'""',
         "encaissement_result":0,"replace":-1,"add_to_all":0,"max_dices":-1,"player_name":'""'}
    a=len(test_values)
    b=len(list)
    try:
        dict_list={}
        for l in list:
            dict_list[l[0]]=l[6]
    except Exception as ex:
        print(ex)

    fails=0
    if a<b:
        print("Too many values in the list")
        for l in dict_list.keys():
            if l not in test_values:
                fails+=1
                print("{} is in the list but not in the test template".format(l))
    elif b<a:
        print("Too few values in the list")
        for t,v in test_values.items():
            if t not in dict_list.keys():
                fails+=1
                print("{} is missing from the list (supposed value: {})".format(t,v))
    else:
        for l,vl in dict_list.items():
            if l in test_values.keys():
                if test_values[l]!=vl:
                    fails+=1
                    print("Element invalid, expected {} for {} in the list, got {}".format(test_values[l],l,vl))
            else:
                fails+=1
                print("Element invalid, {} is not in the test values".format(l))
    if fails:
        print("{} errors occured")
    else:
        print("Init: All test sucessfull")
    return fails

def returns(args):
    pass

def check_returns(args):
    pass


commands={"init":initialise,"print":pprint,"test_init":check_init}

if __name__ == '__main__':
    try:
        commands[command](args)
    except Exception,err:
        print("Couldn't execute command "+command)
        print(err)

"""
var msg_relance="<a class='sheet-rolltemplate-d10fight' href='!crit 0 P "+d_vars.perfection+" I 0 "+d_vars.defense_i_0+" I 1 "+d_vars.defense_i_1+
" I 4 "+d_vars.defense_i_2+" R "+d_vars.rempart_p+" F "+d_vars.fauchage+
" E 0 "+d_vars.exploiter_p_0+" E 1 "+d_vars.exploiter_p_1+" E 4 "+d_vars.exploiter_p_2+" T 0 "+d_vars.tir_p_0+" T 2 "+d_vars.tir_p_1+
" i "+d_vars.tir_i+" C "+d_vars.charge+" N "+d_vars.charge_i+" + "+(d_vars.nb_2add+d_vars.technique_result+d_vars.encaissement_result)+" - "+d_vars.nb_2sub+
" r ?{Relances ?} "+" s "+d_vars.seuil+" a "+d_vars.action+" H "+d_vars.on_hit_c+" A "+d_vars.attribute+" L "+d_vars.replace+" l "+d_vars.add_to_all+" m "+d_vars.max_dices+" : "+d_vars.player_name;
for (var i=0,len=d_vars.results.length;i<len;i++) msg_relance+=" d "+d_vars.results[i];
msg_relance+="'>Relancer ce jet</a>";

case "d":
d_vars.flat_dices[d_vars.nb_flat_dices]=to_p_number(tab[i+1]);
d_vars.nb_flat_dices++;
i.append(2;
break;

case "S":
d_vars.encaissement=to_number(tab[i+1]);
        d_vars.encaissement_dices="d20";
        if (tab[i+2]=="4") d_vars.encaissement_dices="d10";
i.append(3;

case "I":
switch (tab[i+1]) {
    case "1":
        d_vars.defense_i_0=to_p_number(tab[i+2]);
        break;
    case "2":
        d_vars.defense_i_1=to_p_number(tab[i+2]);
        break;
    case "4":
        d_vars.defense_i_2=to_p_number(tab[i+2]);
        break;
}
i.append(3;
break;
case "E":
switch (tab[i+1]) {
    case "1":
        d_vars.exploiter_p_0=to_p_number(tab[i+2]);
        break;
    case "2":
        d_vars.exploiter_p_1=to_p_number(tab[i+2]);
        break;
    case "4":
        d_vars.exploiter_p_2=to_p_number(tab[i+2]);
        break;
}
i.append(3;
break;
case "T":
switch (tab[i+1]) {
    case "2":
        d_vars.tir_p_0=to_p_number(tab[i+2]);
        break;
    case "4":
        d_vars.tir_p_1=to_p_number(tab[i+2]);
        break;
}
i.append(3;

default:
logit("Argument "+tab[i]+" unknown.");
"""
