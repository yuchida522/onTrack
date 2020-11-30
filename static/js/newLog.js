'use strict';

// create log button

document.querySelector('#create-new-log-button').addEventListener('click', (evt) => {
    evt.preventDefault();
  
    const formInputs = {
      'training_date': $('#training-date-field').val(),
      'mileage_run': $('#training-mileage-field').val(),
      'run_time_hr': $('#h-field').val(),
      'run_time_min': $('#m-field').val(),
      'run_time_sec': $('#s-field').val(),
      'effort': $('#training-effort-field:checked').val(),
      'comments': $('#training-comment-field').val()
    }
    console.log(formInputs)
    $.post('/save-new-log', formInputs, (res) => {
  
      Toastify({
        text: res,
        duration: 3000,
        }
  
        ).showToast();
    });

  });