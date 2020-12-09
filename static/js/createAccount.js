'use strict';

//create account button

document.querySelector('#create-new-user-btn').addEventListener('click', (evt) => {
    evt.preventDefault();
  
    const formInputs = {
      'fname': $('#fname-field').val(),
      'lname': $('#lname-field').val(),
      'email': $('#email-field').val(),
      'password': $('#password-field').val()
    }
    
    $.post('/create-new-user', formInputs, (res) => {
      
      if (res === "False") {
        console.log(res)
        Toastify({
          text: "User already exists",
          duration: 3000,
          backgroundColor: "linear-gradient(to right, #f22e8a, #ebccda)"
          }
    
          ).showToast();
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