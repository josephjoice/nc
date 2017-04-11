$(document).ready(function(){
  window.setInterval(function(){
    console.log("ca;lling");
    $.ajax({ type: "GET",   
      url: "/count",
      success: function(text){
        $("#count").text(text);
      } 
    });
  },2000);
});
