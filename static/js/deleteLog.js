"use strict";


// delete log button
document.querySelector('#delete-log-button').addEventListener('click', (evt) => {
  evt.preventDefault();

  const formInputs = {
    training_log_id: $(evt.target).val()
  }
  
  console.log(formInputs)
  $.post(`/delete-training-log/${formInputs.training_log_id}`, formInputs, (res) => {
    console.log(res)
    Toastify({
      text: res,
      duration: 3000,
      }

      ).showToast();
      setTimeout(() => window.location.replace('/training-log') , 1000);
  });
  console.log("CALLED");

});

// document.querySelector('#delete-log-button').addEventListener('submit', (evt) => {
//   evt.preventDefault();

//   const formInputs = {
//     'delete-log': $('#delete-log-button').val()
//   }
  
//   console.log(formInputs)
//   $.post('/delete-training-log', formInputs, (res) => {

//     Toastify({
//       text: res,
//       duration: 3000,
//       }

//       ).showToast();
//       setTimeout(() => window.location.replace('/training-log') , 1000);
//   });
//   console.log("CALLED");

// });





