# Not actually part of the project; just easier to maintain everything here
import sys,os
try:
    import Blessings
except:
    print("Blessings not found, no pretty printing")

try:
    args=sys.argv[1:]
    command=sys.argv[0]
except:
    print("No command specified, just outputing the list")


var d_vars={"nb_dices":0,"perfection":0,"defense_i_0":0,"defense_i_1":0,"defense_i_2":0,"rempart_p":0,
"technique_m":0,"coup_d":0,"coup_d_results":[],"fauchage":0,"exploiter_p_0":0,"exploiter_p_1":0,
"exploiter_p_2":0,"tir_p_0":0,"tir_p_1":0,"tir_i":0,"charge":0,"charge_i":0,"nb_2add":0,"nb_2sub":0,
"relances":0,"seuil":0,"nb_flat_dices":0,"action":"","flat_dices":[],"results":[],"technique_result":0,
"cleave":[],"on_hit_c":0,"attribute":0,"encaissement":0,"encaissement_dices":"","encaissement_result":0,
"replace":-1,"add_to_all":0,"max_dices":-1,"player_name":""};

list=[]
list=['varname','Pretty name','nb_args','type','code','id','default']
list+=['perfection','Perfection',1,'int','P',0,0]
list+=['defense_i_0','Defence impénétrable simple',2,'int','I',1,0]
list+=['defense_i_1','Defence impénétrable expert',2,'int','I',2,0]
list+=['defense_i_2','Defence impénétrable meta',2,'int','I',4,0]
list+=['rempart_p','Rempart parfait',1,'int','R',0,0]
list+=['technique_m','Perfection',1,'int','P',0,0]
list+=['coup_d','Perfection',1,'int','P',0,0]
list+=['coup_d_results','Perfection',1,'int','P',0,0]
list+=['fauchage','Perfection',1,'int','P',0,0]
list+=['exploiter_p_0','Perfection',1,'int','P',0,0]
list+=['exploiter_p_1','Perfection',1,'int','P',0,0]
list+=['exploiter_p_2','Perfection',1,'int','P',0,0]
list+=['tir_p_0','Perfection',1,'int','P',0,0]
list+=['tir_p_1','Perfection',1,'int','P',0,0]
list+=['tir_p_2','Perfection',1,'int','P',0,0]
list+=['tir_i','Perfection',1,'int','P',0,0]
list+=['charge','Perfection',1,'int','P',0,0]
list+=['charge_i','Perfection',1,'int','P',0,0]
list+=['nb_2add','Perfection',1,'int','P',0,0]
list+=['nb_2sub','Perfection',1,'int','P',0,0]
list+=['relances','Perfection',1,'int','P',0,0]
list+=['seuil','Perfection',1,'int','P',0,0]
list+=['nb_flat_dices','Perfection',1,'int','P',0]
list+=['action','Perfection',1,'int','P',0,0]
list+=['flat_dices','Perfection',1,'int','P',0]
list+=['results','Perfection',1,'int','P',0,0]
list+=['technique_result','Perfection',1,'int','P',0,0]
list+=['cleave','Perfection',1,'int','P',0,0]
list+=['on_hit_c','Perfection',1,'int','P',0,0]
list+=['attribute','Perfection',1,'int','P',0,0]
list+=['encaissement','Perfection',1,'int','P',0,0]
list+=['encaissement_dices','Perfection',1,'int','P',0,0]
list+=['encaissement_result','Perfection',1,'int','P',0,0]
list+=['replace','Perfection',1,'int','P',0,0]
list+=['add_to_all','Perfection',1,'int','P',0,0]
list+=['max_dices','Perfection',1,'int','P',0,0]
list+=['player_name','Perfection',1,'int','P',0,0]

list+=['nb_dices',''=0;
Action          a a e d
var all_dices       d*
var nb_2add=0;       //+
var nb_2sub=0;        //-

var relances=0;        //r
Perfection        P

Defense
Défense_impénétrable      I 1
Défense_impénétrable      I 2 - Rappel
Défense_impénétrable      I 4
Rempart_parfait       R

Offense
Technique_martiale      M 1
Technique_martiale      M 2
Coup_déchirant       D
Fauchage        F
Exploiter_les_points_faibles   E 1
Exploiter_les_points_faibles   E 2 - Rappel
Exploiter_les_points_faibles   E 4

Spécial
Tir_précis        T 1
Tir_précis        T 2
Tir_implacable        i
Charge         C
Charge_indomptable      N - (Sur la feuille de perso)
Seuil         s
On Hit crit        H
Attribute values      A
Encaissement       S
]
