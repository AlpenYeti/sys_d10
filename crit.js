on("chat:message", function(msg) {
  //This allows players to enter !sr <number> to roll a number of d6 dice with a target of 4.

  if(msg.type == "api" && msg.content.indexOf("!crit ") !== -1) {
    var sndr=msg.who;
    var raw_msg = msg.content.replace("!crit ", "");

    //Variables a initialiser par parse
    /*var nb_dices=0;
    var nb_2add=0;              //+
    var nb_2sub=0;               //-

    var relances=0;             //r
    Perfection					P

    Defense
    Défense_impénétrable	   I_1
    Défense_impénétrable	   I_2
    Défense_impénétrable	   I_4
    Rempart_parfait				R

    Offense
    Technique_martiale			M_1
    Technique_martiale			M_2
    Coup_déchirant					D
    Fauchage						F
    Exploiter_les_points_faibles	E_1
    Exploiter_les_points_faibles	E_2
    Exploiter_les_points_faibles	E_4

    Spécial
    Tir_précis				      	T_1
    Tir_précis				      	T_2
    Tir_implacable			       i
    Charge							C
    Charge_indomptable	             N
    Seuil                           s
    */

    var d_vars=parse_command(raw_msg);

    logit(d_vars);
    //Initialisation
    d_vars.perfection=Math.min(10,d_vars.perfection);
    var nb_sides=10-d_vars.perfection; //If the sides turns out to be 0 we could do a skip tho...
    var msg_roll="/roll "+d_vars.nb_dices+"d"+nb_sides
    var to_add=d_vars.nb_2add-d_vars.nb_2sub;
    var results=new Array(Number(d_vars.nb_dices));
    /*logit("to roll: "+msg_roll);
    logit("to add: "+to_add);
    logit(nb_sides);
    logit(results);*/

    sendChat(msg.who,msg_roll,function(ops) {
        // ops will be an ARRAY of command results.
        var rollresult = JSON.parse(ops[0]["content"])["rolls"][0]["results"];
        //logit("len: "+rollresult.length);
        for(var i=0,len = rollresult.length ; i<len ; i++){
           results[i]=Number(rollresult[i]["v"])+Number(d_vars.perfection);
        };
        results.sort(function(a, b){return a-b});
        // results is now an Array of all rolls
        logit(results);
        eval_crit(d_vars,results);
    });

  }
});


// All utilities are below here

function eval_crit(d_vars,results){
    // Eval the roll, is it a crit (aka all dices above the crit threshold (7) and the hit threshold)
    var crit_threshold=7; // You need to be above this threshold to score a crit
    var hit_percent=0.5; // You need at least this much to score a hit

    var return_data={
        'keep_table':[], //Results that must be kept
        'relances_table':[], //Array of all the dices over the threshold
        'nb_hit':0, //Number of dices above the hit threshold
        'nb_crit':0, //Number of dices that are a crit
        'nb_ncrit':0, //Number of dices that are NOT a crit
        'nb_relances':0, //Number of used re-rolls
        'is_crit':0, //Is the roll a crit
        'is_hit':0 //Is the roll a hit
    };

    if (d_vars.relances>0){
        return_data.relances_table=new Array(Math.min(d_vars.relances,d_vars.nb_dices));
        return_data.keep_table=new Array(Math.max(0,d_vars.nb_dices-d_vars.relances));
    }

    var len=results.length;
    return_data.nb_ncrit=len;
    var is_crit=0;
    var needed_to_crit=len-d_vars.exploiter_p_2;;

    // Analyse wether it's a hit/miss and if it's critical

    for (i=0;i<len; i++){
       if (results[i]>crit_threshold){ // It's a crit
           return_data.nb_ncrit--;
           return_data.nb_crit++;
       }
       if (results[i]>d_vars.seuil){
           //logit(results[i]+">"+d_vars.seuil+(results[i]>d_vars.seuil));
           return_data.nb_hit++;
       }
    }

    logit(needed_to_crit);
    if (return_data.nb_hit>=Math.floor(hit_percent*len)){
        return_data.is_hit=1;
    }
    if (return_data.nb_crit>=needed_to_crit){
        return_data.is_crit=1;
    }

    //Separate the re-rolls, just in case
    var keep=0;
    for (i=0;i<len ; i++){
        if (d_vars.relances>0){
            return_data.relances_table[return_data.nb_relances]=results[i];
            return_data.nb_relances++;
            d_vars.relances--;
        } else {
            // No more re-rolls
            return_data.keep_table[keep]=results[i];
            keep++;
        }
    }

    //logit("Re-rolls");
    //logit(return_data.relances_table);
    //logit("keeps");
    //logit(return_data.keep_table);
    //logit("Nb crit dices: "+(return_data.nb_crit)+" Nb ncrit dices: "+(return_data.nb_ncrit)+" total: "+len+ " is_hit "+return_data.is_hit+" Nb hit dices: "+(return_data.nb_hit)+" is_crit:"+return_data.is_crit);
    var hm=string_hitmiss(return_data.relances_table,d_vars.seuil);
    /*
    var msg_hit="";
    var add=""
    if (d_vars.seuil!=0){
        var mss="l'attaque manque";
        if (d_vars.is_hit){
            mss="l'attaque touche";
        }
        msg_hit=" seuil "+d_vars.seuil+"  "+mss;
        add="les des "+hm.str_m+"ne touchent pas";
    }
    sendChat(msg.who,"lances "+d_vars.nb_dices+" des")*/
    string_hitmiss(return_data.relances_table,d_vars.seuil);
    return return_data;
}

function to_number(nb){
    // Convert to number or return 0
    var tmp=Number(nb);
    if (isNaN(tmp)) return 0;
    return tmp;
}

function string_hitmiss(table,threshold){
    //Takes an array and a threshold and return two string of missed and hit dices
    var hm={str_h:"[[",str_m:"[["};
    for (var i=0,len=table.length;i<len;i++){
        if (threshold<table[i]){
            if (i!=0){
                hm.str_h+=",";
            }
            hm.str_h+=table[i];
        } else {
            if (i!=0){
                hm.str_m+=",";
            }
            hm.str_m+=table[i];
        }
    }
    hm.str_m+="]]";
    hm.str_h+="]]";
    logit(hm.str_h);
    logit(hm.str_m);
    return hm;
}
function parse_command(message){
    // Parsing
    // Parse a string formated in the following fashion
    // 4 P 2 I 2 4 E 4 1 T 1 4 + 11 - 22
    // And add everithing in the related Variables
    var d_vars={"nb_dices":0,"perfection":0,"defense_i_0":0,"defense_i_1":0,"defense_i_2":0,"rempart_p":0,
              "technique_m_0":0,"technique_m_1":0,"coup_d":0,"fauchage":0,"exploiter_p_0":0,"exploiter_p_1":0,
              "exploiter_p_2":0,"tir_p_0":0,"tir_p_1":0,"tir_i":0,"charge":0,"charge_i":0,"nb_2add":0,"nb_2sub":0,"relances":0,"seuil":0};
    var tab=message.split(" ");
    var len_args=tab.length;
    var i;
    //logit(tab);
    //logit(tab.length);

    if (len_args>0){
      d_vars.nb_dices=tab[0];
    }
    for (i = 1; i < tab.length;) {
        switch(tab[i]) {
            case "+":
                d_vars.nb_2add=to_number(tab[i+1]);
                i+=2;
                break;
            case "-":
                d_vars.nb_2sub=to_number(tab[i+1]);
                i+=2;
                break;
            case "P":
                d_vars.perfection=to_number(tab[i+1]);
                i+=2;
                break;
            case "r":
                d_vars.relances=to_number(tab[i+1]);
                i+=2;
                break;
            case "s":
                d_vars.seuil=to_number(tab[i+1]);
                i+=2;
                break;
            case "I":
                switch (tab[i+1]) {
                    case "1":
                        d_vars.defense_i_0=to_number(tab[i+2]);
                        break;
                    case "2":
                        d_vars.defense_i_1=to_number(tab[i+2]);
                        break;
                    case "4":
                        d_vars.defense_i_2=to_number(tab[i+2]);
                        break;
                }
                i+=3;
                break;
            case "E":
                switch (tab[i+1]) {
                    case "1":
                        d_vars.exploiter_p_0=to_number(tab[i+2]);
                        break;
                    case "2":
                        d_vars.exploiter_p_1=to_number(tab[i+2]);
                        break;
                    case "4":
                        d_vars.exploiter_p_2=to_number(tab[i+2]);
                        break;
               }
               i+=3;
               break;
            case "T":
                switch (tab[i+1]) {
                    case "1":
                        d_vars.tir_p_0=to_number(tab[i+2]);
                        break;
                    case "2":
                        d_vars.tir_p_1=to_number(tab[i+2]);
                        break;
                }
                i+=3;
                break;
            case "R":
                d_vars.rempart_p=to_number(tab[i+1]);
                i+=2;
                break;
            case "C":
                d_vars.charge=to_number(tab[i+1]);
                i+=2;
                break;
            case "M":
                switch (tab[i+1]) {
                    case "1":
                        d_vars.technique_m_0=to_number(tab[i+2]);
                        break;

                    case "2":
                        d_vars.technique_m_1=to_number(tab[i+2]);
                        break;
                }
                i+=3;
                break;
            case "D":
                d_vars.coup_d=to_number(tab[i+1]);
                i+=2;
                break;
            case "F":
                d_vars.fauchage=to_number(tab[i+1]);
                i+=2;
                break;
            case "N":
                d_vars.charge_i=to_number(tab[i+1]);
                i+=2;
                break;
            case "O":
                d_vars.tir_i=to_number(tab[i+1]);
                i+=2;
                break;
            case "r":
                d_vars.relance=to_number(tab[i+1]);
                i+=2;
                break;
            default:
                logit("Argument "+tab[i]+" unknown.");
                i++;
            }
    }
    return d_vars;
};
function logit(txt){
    //Due to the incomprehensible restriction of console. in roll20
    //sendChat("console",txt);
    log(txt);
};
