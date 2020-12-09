"use strict";


// delete saved race button
const deleteSavedRaceButtonlist = document.querySelectorAll('.delete-saved-race-button')

for (let deleteSavedRaceBtn of deleteSavedRaceButtonlist) {
  deleteSavedRaceBtn.addEventListener('click', (evt) => {
    evt.preventDefault();
  
    const formInputs = {
      currentRaceId: $(evt.target).val()
    }
  
    $.post(`/delete-race/${formInputs.currentRaceId}`, formInputs, (res) => {
  
      Toastify({
        text: res,
        duration: 3000,
        backgroundColor: "linear-gradient(to right, #f22e8a, #ebccda)"
        }
  
        ).showToast();
    });
    
    setTimeout(() => window.location.replace('/current-races') , 2000);
  
  });
}