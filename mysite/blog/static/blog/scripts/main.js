


    $(document).on('submit', '#post-form',function(e){
    
        e.preventDefault();
        $.ajax({
            type:'POST',
            url:'/blog/create-post/',
            data:{
                title:$('#title').val().toLowerCase(),
                description:$('#salary-ranges').val().toLowerCase(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            success:function(json){
                console.log(json)
                //$( "#result" ).empty().append(json.title + "-"+json.description);
                $( "#result" ).empty().append("Gracias por enviar su información");
                window.dataLayer = window.dataLayer || [];
                dataLayer.push({'field1':json.title,'field2':json.description})
                $('#title').val('')   
                
            },
            error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
        });
    });









