'use strict';

document.querySelector('#update-saved-race-button').addEventListener('click', (evt) => {
    evt.preventDefault();
    
    const formInputs = {
      currentRaceId: $(evt.target).val(),
      'update_signup_status': $('#signup-status-field').val(),
      'update_completed_status': $('#completed-status-field').val(),
      'update_notes': $('#notes-field').val()
    }
  
    $.post(`/update-saved/${formInputs.currentRaceId}`, formInputs, (res) => {

      Toastify({
          text: res,
          duration: 3000,
          }
    
          ).showToast();
      });
    console.log('called!')
    console.log(formInputs)
    const currentRaceId = $(`#${formInputs.currentRaceId}`);
    console.log(currentRaceId)
    currentRaceId.load('/current-races')
  });
