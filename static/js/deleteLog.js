"use strict";


// delete log button

// list of all the delete buttons on the page
const lst = document.querySelectorAll('.delete-log-button')

for (let deleteButton of lst) {
  deleteButton.addEventListener('click', (evt) => {
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
        backgroundColor: "linear-gradient(to right, #f22e8a, #ebccda)"
        }
  
        ).showToast();
      
    });
    console.log("CALLED");
    const traingLogId = $(`#${formInputs.trainingLogId}`)[0];
    traingLogId.style.display = "none";
  });
  
}







