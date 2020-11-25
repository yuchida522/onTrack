"use strict";


document.querySelector('#login-button').addEventListener('click', (evt) => {
  evt.preventDefault();

  $.post('/login', (res) => {
    Toastify({
      text: res,
      duration: 3000,
      }

      ).showToast();
  });

});



// delete log button
document.querySelector('#delete-log-button').addEventListener('click', (evt) => {
  evt.preventDefault();

  const formInputs = {
    training_log_id: $(evt.target).val()
  }

  $.post(`/delete-training-log/${formInputs.training_log_id}`, formInputs, (res) => {

    Toastify({
      text: res,
      duration: 3000,
      }

      ).showToast();
  });
  // console.log("CALLED");
  const trainingLogId = $(`#${formInputs.training_log_id}`)[0];
  trainingLogId.style.display = "none";

});


