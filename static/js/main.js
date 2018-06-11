$(document).ready(function(){
    
    $("i.material-icons").click(function(){
        // console.log($(this).closest("div.card").siblings("h3").html());
        var msg = new SpeechSynthesisUtterance($(this).closest("div.card").siblings("h3").html());
        window.speechSynthesis.speak(msg)
    });

    $("#upload").click(function(e){       
        e.preventDefault();
        $.ajax({
            url:'/newword',
            type:'post',
            data:$('#uploadForm').serialize(),
            success:function(){
                swal({
                    position: 'top-end',
                    type: 'success',
                    title: 'You have successfully uploaded the word!',
                    showConfirmButton: false,
                    timer: 1500 
                  }).then(function(){
                      window.location.href = '/';
                  }, function(){
                    console.log("Oh, upload failed..."); 
                  });
            }
        });
    });

});