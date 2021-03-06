'use strict';

document.querySelector('#save-race-btn').addEventListener('click', (evt) => {
    evt.preventDefault();

    const formInputs = {
        'race_name': $('#race-name-field').val(),
        'date': $('#race-date-field').val(),
        'city_name': $('#race-city-field').val(),
        'zipcode': $('#race-zipcode-field').val(),
        'race_url': $('#race-url-field').val(),
        'race_description': $('#race-description-field').val(),
        'organization_name': $('#race-organization-field').val(),
        'signup_status': $('#race-signup-field:checked').val(),
        'notes': $('#race-notes-field').val(),
      }
    $.post('/race-saved', formInputs, (res) => {

    Toastify({
          text: res,
          duration: 3000,
          backgroundColor: "linear-gradient(to right, #f22e8a, #ebccda)"
          }
    
          ).showToast();
      });
    
  });