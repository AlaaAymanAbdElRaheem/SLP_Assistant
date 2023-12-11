#!/usr/bin/node

$(document).ready(function () {
  let id = 0;
  function fetchMilestones() {
    $.ajax({
      url: "/api/v1/milestones/" + id,
      type: "GET",
      dataType: "json",
      success: addMilestones,
    });
  }

  // event handler for when the user selects a new age range
  $(".age-range").change(function () {
    id = $(this).find("option:selected").data("id");
    const value = $(this).val();

    $(".age-result-text").text(value);
    $(".result-container").css("visibility", "visible");
    fetchMilestones(id);

    // Enable/disable buttons based on option availability
    let $selectedOption = $(this).find("option:selected");
    $(".next-age-button").prop(
      "disabled",
      !$selectedOption.next("option").length
    );
    $(".prev-age-button").prop(
      "disabled",
      !$selectedOption.prev("option").length
    );
  });

  // Event handlers for next and prev buttons
  $(".next-age-button").click(function () {
    let $select = $(".age-range");
    let $selectedOption = $select.find("option:selected");
    let $nextOption = $selectedOption.next("option");

    if ($nextOption.length > 0) {
      $selectedOption.prop("selected", false);
      $nextOption.prop("selected", true);
      $select.trigger("change"); // Trigger change event
    }
  });

  $(".prev-age-button").click(function () {
    let $select = $(".age-range");
    let $selectedOption = $select.find("option:selected");
    let $prevOption = $selectedOption.prev("option:not([disabled])"); // Ignore disabled options

    if ($prevOption.length > 0) {
      $selectedOption.prop("selected", false);
      $prevOption.prop("selected", true);
      $select.trigger("change");
    }
  });

  //adding data to the table in html
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

    // Styling the list
    $(".list").css("padding-left", "0px");
    $(".list").css("margin-left", "10px");
    $(".li").css("margin-bottom", "5px");
  }
});
