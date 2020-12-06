'use strict';

//create account button

document.querySelector('#create-new-user-button').addEventListener('click', (evt) => {
    evt.preventDefault();
  
    const formInputs = {
      'fname': $('#fname-field').val(),
      'lname': $('#lname-field').val(),
      'username': $('#username-field').val(),
      'email': $('#email-field').val(),
      'password': $('#password-field').val()
    }
    console.log(formInputs)
    $.post('/create-new-user', formInputs, (res) => {
  
      Toastify({
        text: res,
        duration: 3000,
        backgroundColor: "linear-gradient(to right, #f22e8a, #ebccda)"
        }
  
        ).showToast();
    });

  });