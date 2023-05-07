
    const theButton = document.querySelector(".btn.btn-primary");
    var firstInput = $("#title")
    var secondInput = $("#salary-ranges") 
    theButton.addEventListener("click", (event) => {
        if(firstInput.val() == "" || secondInput.val() == 'select'){
            event.preventDefault()
            theButton.classList.add("button--loading")
            setTimeout(() => {
                        theButton.classList.remove("button--loading");
                        $('#title').val('');
                        $('#salary-ranges').prop('selectedIndex', 0);
                        }, 400)
            setTimeout(() => {snackBar("Introduce información en los 2 campos")}, 400)

        }else{

            // AJAX call
            $(document).one('submit', '#post-form',function(e){
            e.preventDefault();
            $.ajax({
                type:'POST',
                url:'/blog/feedback/',
                data:{
                    title:$('#title').val().toLowerCase(),
                    description:$('#salary-ranges').val().toLowerCase(),
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    action: 'post'
                },
                success:function(json){
                    console.log(json)
                    //$( "#result" ).empty().append(json.title + "-"+json.description);
                    //setTimeout(() => {$( "#result" ).empty().append("Gracias por enviar su información");}, 1600)
            
                    window.dataLayer = window.dataLayer || [];
                    dataLayer.push({'field1':json.title,'field2':json.description})    
                    
                    },
                error : function(xhr,errmsg,err){
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    }
                });
            });

            theButton.classList.add("button--loading")
            setTimeout(() => {
                            theButton.classList.remove("button--loading");
                            $('#salary-ranges').prop('selectedIndex', 0);
                            $('#title').val('')
                                }, 1600)
            setTimeout(() => {snackBar("Información enviada")}, 1600)


        }


    });

    function snackBar(text) {
        // Get the snackbar DIV
        var notificationDiv = document.getElementById("snackbar"); 
        // Add Info to the DIV
        $("#snackbar").empty().append(text);
        // Add the "show" class to DIV
        notificationDiv.className = "show";
        // After 3 seconds, remove the show class from DIV
        setTimeout(function(){ notificationDiv.className = notificationDiv.className.replace("show", "");}, 2000);
    }

