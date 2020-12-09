'use strict';

document.querySelector('#update-saved-race-button').addEventListener('click', (evt) => {
    evt.preventDefault();
    
    const formInputs = {
      currentRaceId: $(evt.target).val(),
      'update_signup_status': $('#signup-status-field:checked').val(),
      'update_notes': $('#notes-field').val()
      
    }
  
    $.post(`/update-saved/${formInputs.currentRaceId}`, formInputs, (res) => {

      Toastify({
          text: res,
          duration: 3000,
          backgroundColor: "linear-gradient(to right, #f22e8a, #ebccda)"
          }
    
          ).showToast();
      });
    // console.log('called!')
    // console.log(formInputs)
    setTimeout(() => window.location.replace('/current-races') , 2000);
  });
