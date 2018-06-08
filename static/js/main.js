$(document).ready(function(){
 
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