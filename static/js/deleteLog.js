"use strict";


// delete log button
document.querySelectorAll('.delete-log-button').forEach(addEventListener('click', (evt) => {
  evt.preventDefault();

  const formInputs = {
    trainingLogId: $(evt.target).val()
  }
  
  console.log(formInputs)
  $.post(`/delete-training-log/${formInputs.trainingLogId}`, formInputs, (res) => {
    console.log(res)

    Toastify({
      text: res,
      duration: 3000,
      }

      ).showToast();
    
  });
  console.log("CALLED");
  const traingLogId = $(`#${formInputs.trainingLogId}`)[0];
  traingLogId.style.display = "none";
}));







