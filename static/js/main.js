$(document).ready(function(){
    $("#upload").click(function(e){
        e.preventdDefault();
        $.post("/newword",
        {
        word:'helo',
        mean:'world',
        note:'wow'
        },
        function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        });
    });
});