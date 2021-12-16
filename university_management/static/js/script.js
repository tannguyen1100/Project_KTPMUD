const logIns = document.querySelectorAll('.js-login')
console.log(logIns);
        const modal = document.querySelector('.js__modal')
        const modalClose = document.querySelector('.js-cancel')
        const modalContainer = document.querySelector('.js-close--out')

        function showLogIn(){
            modal.classList.add('qldt__modal-open')
        }
        function closeLogIn(){
            modal.classList.remove('qldt__modal-open')
        }
       
        for (const logIn of logIns){
            logIn.addEventListener('click', showLogIn)
        }

        modalClose.addEventListener('click', closeLogIn)

        modal.addEventListener('click', closeLogIn)

        modalContainer.addEventListener('click', function(event){
            event.stopPropagation()
        })
