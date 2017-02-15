on("chat:message", function(msg) {
  //This allows players to enter !sr <number> to roll a number of d6 dice with a target of 4.
 
  if(msg.type == "api" && msg.content.indexOf("!crit ") !== -1) {
    var sndr=msg.who;
    var numdice = msg.content.replace("!crit ", "");
    var result='';
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
   
  }
});