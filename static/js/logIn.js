'use strict';

//Log In button

document.querySelector('#login-button').addEventListener('click', (evt) => {
  evt.preventDefault();

  const formInputs = {
    'login-email': $('#login-email-field').val(),
    'login-password': $('#login-password-field').val()
  }

  $.post('/login', formInputs, (res) => {
    console.log(formInputs)
    if (res === 'True') {
      Toastify({
        text: 'Welcome!',
        duration: 3000,
        backgroundColor: "linear-gradient(to right, #f22e8a, #ebccda)"
        }
  
        ).showToast();
        console.log(res)
        setTimeout(() => window.location.replace('/profile') , 1000);
      } else {
      Toastify({
        text: res,
        duration: 3000,
        backgroundColor: "linear-gradient(to right, #f22e8a, #ebccda)"
        }
  
        ).showToast();
    }      
  });
  
});

