
$(document).on('submit', '#post-form',function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'/blog/create-post/',
        data:{
            title:$('#title').val(),
            description:$('#description').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(json){
            console.log(json)
            $( "#result" ).empty().append(json.title);
             
            
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
});



