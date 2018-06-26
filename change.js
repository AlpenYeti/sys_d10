on("chat:message", function(msg) {
    //This allows players to enter !sr <number> to roll a number of d6 dice with a target of 4.
    if(msg.type == "api" && msg.content.indexOf("!change ") !== -1) {
        var sndr=msg.who;
        var raw_msg = msg.content.replace("!change ", "");

        //Marking the log, note that if logit is disabled, nothing will be shown
        logit("Following results will track the session of "+msg.who);
        logit("The command input was : "+raw_msg);

        var cmd=message.split(" ");
        if (cmd.length<2){
          return null;
        };
        var cmd_name=cmd[0];
        var cmd_val=cmd[1];
        var auth=[" attr_Life_Points",
        "attr_Endurance_Points",
        "attr_general_item_weapon1",
        "attr_general_item_weapon2",
        "attr_general_item_weapon3",
        "attr_base_damage_dices",
        "attr_exal_damage_dices"]
        for (var i = 0; i < auth.length; i++) {
          if (auth[i].indexOf(cmd_name)!==-1){
            var attribObj = findObjs({ type: 'attribute', characterid: character.id, name: auth[i] })[0];
            if (attribObj){attribObj.set('current', cmd_val);};
          }
        }
    };
};

function logit(txt){
    //Due to the restriction of console.log()
    log(txt);
};
