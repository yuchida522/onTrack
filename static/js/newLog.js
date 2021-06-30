'use strict';

// // create log button

document.querySelector('#create-new-btn').addEventListener('click', (evt) => {
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
  
    $.post('/save-new-log', formInputs, (res) => {
  
      Toastify({
        text: res,
        duration: 3000,
        backgroundColor: "linear-gradient(to right, #f22e8a, #ebccda)"
        }
  
        ).showToast();
        setTimeout(() => window.location.replace('/training-log') , 2000);
    });

  });