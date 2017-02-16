on("chat:message", function(msg) {
  //This allows players to enter !sr <number> to roll a number of d6 dice with a target of 4.

  if(msg.type == "api" && msg.content.indexOf("!crit ") !== -1) {
    var sndr=msg.who;
    var raw_msg = msg.content.replace("!crit ", "");
    var result='';

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
    */

    var d_vars=parse_command(raw_msg);


    var msg_roll=d_vars.nb_dices+"d10"+"+"+d_vars.nb_2add+"-"+d_vars.nb_2sub;


    /*
    log(msg);
    sendChat(msg.who,'/roll 4d10',function(ops) {
        // ops will be an ARRAY of command results.
        sendChat(sndr,numdice);
        var rollresult = JSON.parse(ops[0]["content"])["rolls"][0]["results"];
        for(var i=0,len = rollresult.length ; i<len ; i++){
           result+=','+rollresult[i]["v"];
        };
        log(result);
        sendChat(sndr,result);
        //log(rollresult);
        //Now do something with rollresult, just like you would during a chat:message event...

    });
    */
  }
});

function to_number(nb){
    var tmp=Number(nb);
    if (isNaN(tmp)) return 0;
    return tmp;
}

function parse_command(message){
    // Parsing
    // Parse a string formated in the following fashion
    // 4 P 2 I 2 4 E 4 1 T 1 4 + 11 - 22
    // And add everithing in the related Variables
    var d_vars={"nb_dices":0,"perfection":0,"defense_i_0":0,"defense_i_1":0,"defense_i_2":0,"rempart_p":0,
              "technique_m_0":0,"technique_m_1":0,"coup_d":0,"fauchage":0,"exploiter_p_0":0,"exploiter_p_1":0,
              "exploiter_p_2":0,"tir_p_0":0,"tir_p_1":0,"tir_i":0,"charge":0,"charge_i":0,"nb_2add":0,"nb_2sub":0,"relances":0};
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
    log(txt);
};
