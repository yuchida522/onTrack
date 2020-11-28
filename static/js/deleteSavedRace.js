"use strict";


// delete saved race button
document.querySelector('#delete-saved-race-button').addEventListener('click', (evt) => {
  evt.preventDefault();

  const formInputs = {
    currentRaceId: $(evt.target).val()
  }

  $.post(`/delete-race/${formInputs.currentRaceId}`, formInputs, (res) => {

    Toastify({
      text: res,
      duration: 3000,
      }

      ).showToast();
  });
  // console.log("CALLED");
  const currentRaceId = $(`#${formInputs.currentRaceId}`)[0];
  currentRaceId.style.display = "none";

});