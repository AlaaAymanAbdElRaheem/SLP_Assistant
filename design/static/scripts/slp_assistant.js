#!/usr/bin/node

$(document).ready(function () {
  $(".age-range").change(function () {
    const id = $(this).find('option:selected').data('id');
    console.log(id);
    let value = $(this).val();
    if(window.location.pathname == "/") {
      window.location.href = "/results/" + id;
    }
    $(".age-result-text").text(value);
    $.ajax({
      url: "http://localhost:5001/api/v1/milestones/" + id,
      type: "GET",
      dataType: "json",
      success: addMilestones
    });
  });

  function addMilestones(data) {
    let listeningText = "<ul>";
    let receptiveLanguageText = "<ul>";
    let expressiveLanguageText = "<ul>";
    let speechText = "<ul>";
    let cognitionText = "<ul>";
    let socialCommunicationText = "<ul>";

    $.each(data, function (index, milestone) {
      switch (milestone.type) {
        case "Listening":
          listeningText += "<li>" + milestone.value + "</li>";
          break;
        case "Receptive Language":
          receptiveLanguageText += "<li>" + milestone.value + "</li>";
          break;
        case "Expressive Language":
          expressiveLanguageText += "<li>" + milestone.value + "</li>";
          break;
        case "Speech":
          speechText += "<li>" + milestone.value + "</li>";
          break;
        case "Cognition":
          cognitionText += "<li>" + milestone.value + "</li>";
          break;
        case "Social Communication":
          socialCommunicationText += "<li>" + milestone.value + "</li>";
          break;
      }
    });

    $(".listening").html(listeningText);
    $(".receptive_language").html(receptiveLanguageText);
    $(".expressive_language").html(expressiveLanguageText);
    $(".speech").html(speechText);
    $(".cognition").html(cognitionText);
    $(".social_communication").html(socialCommunicationText);
  }
});
