
$(document).ready(function () {
    $('#login_button').on('click', function() {
        const form = document.getElementById('loginForm')
        const email = document.getElementById('email')
        const password = document.getElementById('password')
        const csrf = document.getElementsByName('csrfmiddlewaretoken')
        console.log(csrf)

        const url = ""

        form.addEventListener('submit', e=>{
            
            $.ajax({
                type: 'POST',
                url: url,
                enctype: 'multipart/form-data',
                data: fd,
                success: function(response){
                    console.log(response)
                    setTimeout(()=>{
                        email.value = ""
                        password.value = ""
                    }, 0)
                },
                error: function(error){
                    console.log(error)
                    
                },
                cache: false,
                contentType: false,
                processData: false,
            })

        })

    
    });
});



