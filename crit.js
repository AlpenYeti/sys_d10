on("chat:message", function(msg) {
//This allows players to enter !sr <number> to roll a number of d6 dice with a target of 4.
if(msg.type == "api" && msg.content.indexOf("!crit ") !== -1) {

    var sndr=msg.who;
    var raw_msg = msg.content.replace("!crit ", "");

    //Marking the log, note that if logit is disabled, nothing will be shown
    logit("Following results will track the session of "+msg.who);
    logit("The command input was : "+raw_msg);

    //Parsing all Variables from the prompt
    var d_vars=parse_command(raw_msg);
    //d_vars.results=new Array(Number(d_vars.nb_dices));
    d_vars.perfection=Math.min(10,d_vars.perfection);
    d_vars.rempart_p=Math.min(10,d_vars.rempart_p);
    d_vars.nb_dices+=d_vars.tir_p_0+d_vars.tir_p_1;

    d_vars.seuil=Math.max(d_vars.seuil-d_vars.tir_i,0);

    // Let's be honests no one really cares if it's a defensive or offensive perfection
    d_vars.perfection=Math.max(d_vars.perfection,d_vars.rempart_p);
    logit(d_vars);

    //Initialisation
    var nb_sides=10-d_vars.perfection; //If the sides turns out to be 0 we could do a skip tho...
    var msg_roll="/roll "+d_vars.nb_dices+"d"+nb_sides;
    if (d_vars.technique_m!=0) msg_roll+="+1d10"; // Let's have one more dice for the test, ugly but meh
    //var to_add=d_vars.nb_2add-d_vars.nb_2sub;

    // Original launch
    sendChat(msg.who,msg_roll,function(ops) {
        // ops will be an ARRAY of command results.

        var rollresult = JSON.parse(ops[0]["content"])["rolls"][0]["results"];
        if (d_vars.technique_m!=0) {
            d_vars.technique_result = JSON.parse(ops[0]["content"])["rolls"][2]["results"][0]["v"];
            var t = Math.max(0,d_vars.technique_m-d_vars.technique_result);
            if (d_vars.technique_result==1) d_vars.technique_result=t*2;
            else d_vars.technique_result=t;
        }
        for(var i=0,len = rollresult.length ; i<len ; i++){
            // results is now an Array of all rolls
           d_vars.results[i]=Number(rollresult[i]["v"])+Number(d_vars.perfection);
        };
        // Merge the array and add all the flat_dices
        d_vars.results=d_vars.results.concat(d_vars.flat_dices);
        d_vars.nb_rolls+=d_vars.nb_flat_dices;

        // Sort the array, for futur usees
        //d_vars.results.sort(function(a, b){return a-b});
        logit(d_vars.results);

        //Now rerolls for every reroll available and show the result
        reroll(msg.who,d_vars);
    });

}});

function reroll(who,d_vars){
    //Upgrade the results with a reroll
    if (d_vars.relances==0) return show_rolls(who,d_vars);
    var msg_roll="/roll "+d_vars.relances+"d"+(10-d_vars.perfection);
    var rerolls=[];
    sendChat(who,msg_roll,function(ops) {
        var rollresult = JSON.parse(ops[0]["content"])["rolls"][0]["results"];
        for(var i=0,len = rollresult.length ; i<len ; i++){
           rerolls[i]=Number(rollresult[i]["v"])+Number(d_vars.perfection);
        };

        //Merge the rerolls to the results, then drop the d_vars.rerolls lower ones (this method is equivalent to n consecutives rerolls)
        for(var i=0;i<d_vars.relances ; i++){
            // Find the smallest element and Place the reroll in it's place
            d_vars.results[indexOfSmallest(d_vars.results)]=rerolls[i];
        }
        // Now we can split the cleave from the rolls
        if (d_vars.fauchage!=0){
            d_vars.cleave=d_vars.results.splice(d_vars.results.length-d_vars.fauchage).sort(function(a, b){return a-b});
        }
        d_vars.results.sort(function(a, b){return a-b});
        //logit(d_vars.results);
        show_rolls(who,d_vars);
    });
}

function indexOfSmallest(a) {
    var lowest = 0;
    for (var i = 1; i < a.length; i++) {
        if (a[i] < a[lowest]) lowest = i;
    }
    return lowest;
}
// All utilities are below here
function eval_crit(d_vars){
    // Eval the roll, is it a crit (aka all dices above the crit threshold (7) and the hit threshold)
    var crit_threshold=7; // You need to be above this threshold to score a crit
    var hit_percent=0.5; // You need at least this much to score a hit

    var return_data={
        'nb_hit':0, //Number of dices above the hit threshold
        'nb_crit':0, //Number of dices that are a crit
        'nb_ncrit':0, //Number of dices that are NOT a crit
        'nb_relances':0, //Number of used re-rolls
        'is_crit':0, //Is the roll a crit
        'is_hit':0 //Is the roll a hit
    };

    var len=d_vars.results.length;
    return_data.nb_ncrit=len;
    var needed_to_crit=len-Math.max(d_vars.exploiter_p_2,d_vars.defense_i_2);

    // Analyse wether it's a hit/miss and if it's critical
    for (i=0;i<len; i++){
       if (d_vars.results[i]>crit_threshold){ // It's a crit
           return_data.nb_ncrit--;
           return_data.nb_crit++;
       }
       if (d_vars.results[i]>d_vars.seuil){
           return_data.nb_hit++;
       }
    }

    if (return_data.nb_hit>=Math.floor(hit_percent*len)){
        return_data.is_hit=1;
    }
    if (return_data.nb_crit>=needed_to_crit){
        return_data.is_crit=1;
    }

    //logit("Nb crit dices: "+(return_data.nb_crit)+" Nb ncrit dices: "+(return_data.nb_ncrit)+" total: "+len+ " is_hit "+return_data.is_hit+" Nb hit dices: "+(return_data.nb_hit)+" is_crit: "+return_data.is_crit+" needed_to_crit "+needed_to_crit);
    //logit(return_data);
    return return_data;
}

function to_p_number(nb){
    // Convert to number or return 0
    var tmp=Number(nb);
    if (isNaN(tmp)) return 0;
    return Math.abs(tmp);
}

function to_number(nb){
    // Convert to number or return 0
    var tmp=Number(nb);
    if (isNaN(tmp)) return 0;
    return tmp;
}

function show_rolls(who,d_vars){
    //Return a beautiful table showing the results and some information depending on the type of action "e":Dodge "a":Attack "d":Defense

    var msg_head="<div style='border-radius: 6px; border: 2px solid #898989;'> <table style='text-align: left;' width=100% border='0' cellpadding='2' cellspacing='0'> <tbody>"
    var msg="<tr><td style='background-color: #999999;'>";
    var msg_foot="</tr></td></table></div>";
    var msg_adds="";

    var sum=0;
    var m_esq=1,m_crit=1; //The multiplier from dodge or crit

    //Eval the rolls to determine if it's a crit
    var dice_stats=eval_crit(d_vars);
    logit(dice_stats);

    switch(d_vars.action){
        case "a":
            msg+=who+" attaque</span></td><tr><td>";
            break;
        case "e":
            msg+=who+" esquive</span></td><tr><td>";
            m_esq=2; // It's a hit
            break;
        case "d":
            msg+=who+" se defend</span></td><tr><td>";
            break;
        default:
            msg+=who+" lance "+d_vars.nb_dices+" dés</span></td><tr><td>";
    }
    if (dice_stats.is_crit) m_crit=2; // It's a crit

    //Add the rolls
    msg+=add_thoose_dices(d_vars,d_vars.results,m_esq,m_crit);
    if (d_vars.coup_d!=0) msg_adds="Coup déchirant: "+d_vars.coup_d; // Coup déchirant
    if (d_vars.technique_m!=0) msg_adds="Technique martiale: "+d_vars.technique_result; // Technique martiale
    if (msg_adds!="") msg_adds="<tr><td>"+msg_adds+"</tr></td>";    // Close this line

    if (dice_stats.is_crit==1) msg+="<tr><td>L'action est une réussite critique</tr></td>";
    if (dice_stats.is_hit==1){
        if (d_vars.seuil!=0){
            if (d_vars.action=="a"){
                msg+="<tr><td>L'attaque parvient a toucher sa cible</tr></td>";
            } else if (d_vars.action=="d"||d_vars.action=="e"){
                // Can't miss a block or a dodge, can be shitty tho
            } else {
                msg+="<tr><td>L'action est un succes</tr></td>";
            }
        }
    } else {
        if (d_vars.action=="a"){
            msg+="<tr><td>L'attaque ne touche pas sa cible</tr></td>";
        } else if (d_vars.action=="d"||d_vars.action=="e"){
            // Can't miss a block or a dodge
        } else {
            msg+="<tr><td>L'action est un echec</tr></td>";
        }
    }
    msg+=msg_adds;
    sendChat(who,msg_head+msg+msg_foot);
    //logit(msg_head+msg+msg_foot);
}

function add_thoose_dices(d_vars,results,m_esq,m_crit){
    var dices="";
    var is_below=0,is_acrit=0;
    var sum=0;
    var t_hit=d_vars.seuil,t_crit=Math.max(7,d_vars.seuil); //The crit threshold can change if the hit threshold is higher

    for (var i=0,len=results.length;i<len;i++){
        //Is it under the threshold?
        if (results[i]<t_hit && is_below==0){
            dices+="<span style='color: #999999;'>"; //Start greying everithing
            is_below=1;
        }
        if (results[i]>t_hit && is_below==1){
            dices+="</span>"; //Stop greying everithing
            is_below=2;
        }
        if (results[i]>t_crit&&is_acrit==0){
            dices+="<span style='color: #009900;'>"; //Start greening everithing
            is_acrit=1;
        }
        // Only add to the sum if you pass the threshold
        if (results[i]>t_hit) sum+=results[i];
        dices+=results[i]+" ";
    }

    if (is_acrit==1){
        dices+="</span>"; //Stop greening everything
        is_acrit=2;
    }
    // Add everything to the sum
    sum=((sum*m_esq)+d_vars.nb_2add)*m_crit-d_vars.nb_2sub;
    sum+=d_vars.defense_i_0+d_vars.exploiter_p_0+d_vars.charge;

    dices+="<tr><td>Resultat: "+sum+"</tr></td>";

    logit(dices);
    return dices;
};

function parse_command(message){
    // Parsing
    // Parse a string formated in the following fashion
    // 4 P 2 I 2 4 E 4 1 T 1 4 + 11 - 22 s 2 d 4 d 5 d 8 d 1
    // And add everithing in the related Variables
    var d_vars={"nb_dices":0,"perfection":0,"defense_i_0":0,"defense_i_1":0,"defense_i_2":0,"rempart_p":0,
              "technique_m":0,"coup_d":0,"fauchage":0,"exploiter_p_0":0,"exploiter_p_1":0,
              "exploiter_p_2":0,"tir_p_0":0,"tir_p_1":0,"tir_i":0,"charge":0,"charge_i":0,"nb_2add":0,"nb_2sub":0,
              "relances":0,"seuil":0,"nb_flat_dices":0,"action":"","flat_dices":[],"results":[],"technique_result":0,"cleave":[]};
    var tab=message.split(" ");
    var len_args=tab.length;
    var i;
    //logit(tab);
    //logit(tab.length);

    if (len_args>0){
      d_vars.nb_dices=to_p_number(tab[0]);
    }
    for (i = 1; i < len_args;) {
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
                d_vars.perfection=to_p_number(tab[i+1]);
                i+=2;
                break;
            case "r":
                d_vars.relances=to_p_number(tab[i+1]);
                i+=2;
                break;
            case "s":
                d_vars.seuil=to_p_number(tab[i+1]);
                i+=2;
                break;
            case "d":
                d_vars.flat_dices[d_vars.nb_flat_dices]=to_p_number(tab[i+1]);
                d_vars.nb_flat_dices++;
                i+=2;
                break;
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
                i+=3;
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
               i+=3;
               break;
            case "T":
                switch (tab[i+1]) {
                    case "1":
                        d_vars.tir_p_0=to_p_number(tab[i+2]);
                        break;
                    case "2":
                        d_vars.tir_p_1=to_p_number(tab[i+2]);
                        break;
                }
                i+=3;
                break;
            case "R":
                d_vars.rempart_p=to_p_number(tab[i+1]);
                i+=2;
                break;
            case "C":
                d_vars.charge=to_p_number(tab[i+1]);
                i+=2;
                break;
            case "M": // Both act likewise, we don't care the level in the script
                d_vars.technique_m=to_p_number(tab[i+2]);
                i+=3;
                break;
            case "D":
                d_vars.coup_d=to_p_number(tab[i+1]);
                i+=2;
                break;
            case "F":
                d_vars.fauchage=to_p_number(tab[i+1]);
                i+=2;
                break;
            case "N":
                d_vars.charge_i=to_p_number(tab[i+1]);
                i+=2;
                break;
            case "O":
                d_vars.tir_i=to_p_number(tab[i+1]);
                i+=2;
                break;
            case "r":
                d_vars.relance=to_p_number(tab[i+1]);
                i+=2;
                break;
            case "a":
                d_vars.action=tab[i+1];
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
