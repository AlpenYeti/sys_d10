on("chat:message", function(msg) {
  //This allows players to enter !sr <number> to roll a number of d6 dice with a target of 4.

  if(msg.type == "api" && msg.content.indexOf("!crit ") !== -1) {
    var sndr=msg.who;
    var raw_msg = msg.content.replace("!crit ", "");
    var result='';

    //Variables a initialiser par parse
    var nb_dices=0;
    var nb_2add=0; //+
    var nb_2sub=0; //-

    var relances=0; //r
    var perfection=0; //P

    var defense_i_0=0; // I_1
    var defense_i_0=0; // I_2
    var defense_i_0=0; // I_4
    var rempart_p=0; //R
    var technique_m_0=0; //M_1
    var technique_m_1=0; //M_2
    var coup_d=0;        //D

    var fauchage=0; //F

    var exploiter_p_0=0; //E_1
    var exploiter_p_1=0; //E_2
    var exploiter_p_2=0; //E_4

    var tir_p_0=0;  //T_1
    var tir_p_1=0; //T_2
    var tir_i=0;  // O
    var charge=0; //C
    var charge_i=0; //N

    // Parsing
    // Parse a string formated in the following fashion
    // 4 P 2 I 2 4 E 4 1 T 1 4 + 11 - 22
    // And add everithing in the related Variables

    var tab=raw_msg.split(" ");
    log(tab);
    log(tab.length);
    var i;



    var msg_roll=nb_dices+"d10"+"+"+nb_2add+"-"+nb_2sub;

    for (i = 0; i < tab.length;) {
        while(i == 0) {
            nb_dices=tab[i];
            i++;
        }

        switch(tab[i]) {
          case "+":
              nb_2add=tab[i+1];
              i+=2;
              break;

          case "-":
              nb_2sub=tab[i+1];
              i+=2;
              break;

          case "P":
              perfection=tab[i+1];
              i+=2;
              break;

          case "I":
              switch (tab[i+1]) {
                  case "1":
                      defense_i_0=tab[i+2];
                      break;

                  case "2":
                      defense_i_1=tab[i+2];
                      break;

                  case "4":
                      defense_i_2=tab[i+2];
                      break;
              }
              i+=3;
              break;

          case "E":
              switch (tab[i+1]) {
                  case "1":
                      exploiter_p_0=tab[i+2];
                      break;

                  case "2":
                      exploiter_p_1=tab[i+2];
                      break;

                  case "4":
                      exploiter_p_2=tab[i+2];
                      break;
             }
             i+=3;
             break;

          case "T":
              switch (tab[i+1]) {
                  case "1":
                      tir_p_0=tab[i+2];
                      break;

                  case "2":
                      tir_p_1=tab[i+2];
                      break;
              }
              i+=3;
              break;

          case "R":
              rempart_p=tab[i+1];
              i+=2;
              break;

          case "C":
              charge=tab[i+1];
              i+=2;
              break;

          case "M":
              switch (tab[i+1]) {
                  case "1":
                      technique_m_0=tab[i+2];
                      break;

                  case "2":
                      technique_m_1=tab[i+2];
                      break;
              }
              i+=3;
              break;

          case "D":
              coup_d=tab[i+1];
              i+=2;
              break;

          case "F":
              fauchage=tab[i+1];
              i+=2;
              break;

          case "N":
              charge_i=tab[i+1];
              i+=2;
              break;

          case "O":
              tir_i=tab[i+1];
              i+=2;
              break;

          case "r":
              relance=tab[i+1];
              i+=2;
              break;

          default:
              console.log("None of the above");
              i++;
  }

console.log(i);
}
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
