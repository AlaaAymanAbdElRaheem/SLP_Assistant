#!/usr/bin/node

$(document).ready(function () {
  $(".age-range").change(function () {
    const id = $(this).find("option:selected").data("id");
    console.log(id);
    let value = $(this).val();

    $(".age-result-text").text(value);
    $(".result-container").css("visibility", "visible");
    $.ajax({
      url: "http://localhost:5001/api/v1/milestones/" + id,
      type: "GET",
      dataType: "json",
      success: addMilestones,
    });
  });

  function addMilestones(data) {
    let listeningText = "<ul class='list'>";
    let receptiveLanguageText = "<ul class='list'>";
    let expressiveLanguageText = "<ul class='list'>";
    let speechText = "<ul class='list'>";
    let cognitionText = "<ul class='list'>";
    let socialCommunicationText = "<ul class='list'>";

    $.each(data, function (index, milestone) {
      switch (milestone.type) {
        case "Listening":
          listeningText += "<li class='li'>" + milestone.value + "</li>";
          break;
        case "Receptive Language":
          receptiveLanguageText +=
            "<li class='li'>" + milestone.value + "</li>";
          break;
        case "Expressive Language":
          expressiveLanguageText +=
            "<li class='li'>" + milestone.value + "</li>";
          break;
        case "Speech":
          speechText += "<li class='li'>" + milestone.value + "</li>";
          break;
        case "Cognition":
          cognitionText += "<li class='li'>" + milestone.value + "</li>";
          break;
        case "Social Communication":
          socialCommunicationText +=
            "<li class='li'>" + milestone.value + "</li>";
          break;
      }
    });

    $(".listening").html(listeningText);
    $(".receptive_language").html(receptiveLanguageText);
    $(".expressive_language").html(expressiveLanguageText);
    $(".speech").html(speechText);
    $(".cognition").html(cognitionText);
    $(".social_communication").html(socialCommunicationText);

    $(".list").css("margin-left", "10px");
    $(".li").css("margin-bottom", "5px");
  }
});
