'use strict';

document.querySelector('#edit-log-button').addEventListener('click', (evt) => {
    evt.preventDefault();
    
    const formInputs = {
      training_log_id: $(evt.target).val(),
      'edited_training_date': $('#date-field').val(),
      'edited_training_mileage': $('#mileage-field').val(),
      'edited_training_effort': $('#effort-field').val(),
      'edited_training_comment': $('#comment-field').val()
    }
  
    $.post(`/save-changes/${formInputs.training_log_id}`, formInputs, (res) => {

      Toastify({
          text: res,
          duration: 3000,
          }
    
          ).showToast();
      });
    console.log('called!')
    console.log(formInputs)
    const trainingLogId = $(`#${formInputs.training_log_id}`);
    console.log(trainingLogId)
    trainingLogId.load('/training-log')
  });