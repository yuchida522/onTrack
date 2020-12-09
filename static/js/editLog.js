'use strict';

document.querySelector('#edit-log-button').addEventListener('click', (evt) => {
    evt.preventDefault();
    
    const formInputs = {
      training_log_id: $(evt.target).val(),
      'edited_training_date': $('#edited-date-field').val(),
      'edited_training_mileage': $('#edited-mileage-field').val(),
      'edited_training_effort': $('#edited-effort-field:checked').val(),
      'edited_training_comment': $('#edited-comment-field').val(),
      'edited_run_time_hr': $('#edited-h-field').val(),
      'edited_run_time_min': $('#edited-m-field').val(),
      'edited_run_time_sec': $('#edited-s-field').val()
    }
  
    $.post(`/save-changes/${formInputs.training_log_id}`, formInputs, (res) => {

      Toastify({
          text: res,
          duration: 3000,
          backgroundColor: "linear-gradient(to right, #f22e8a, #ebccda)"
          }
    
          ).showToast();
          setTimeout(() => window.location.replace('/training-log') , 2000);
      });
  
  });