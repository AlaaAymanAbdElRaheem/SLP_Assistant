#!/usr/bin/node

$(document).ready(function () {
  $(".age-range").change(function () {
    // let id = $(this).attr("data-id");
    let value = $(this).val();
    let age_from = value.split("to")[0];
    $.ajax({
      url: "http://localhost:5001/api/v1/age_range_id/" + age_from,
      type: "GET",
      dataType: "json",
      success: function (data) {
        let id = data.age_range_id;

        let flag = 0;
        if (window.location.href === "http://127.0.0.1:5000/slp_assistant") {
          window.location.href = "http://127.0.0.1:5000/slp_assistant/result";
          window.location.href =
            "http://127.0.0.1:5000/slp_assistant/result?value=" +
            encodeURIComponent(value) +
            "&id=" +
            id;
          flag = 1;
        }

        if (flag == 1) {
          // const urlParams = new URLSearchParams(window.location.search);
          // value = urlParams.get("value");
          // console.log(value);
          // id = urlParams.get("id");
          let params = new URL(document.location).searchParams;
          value = params.get("value");
          id = params.get("id");
        }

        $(".age-result-text").text(value);
        $.ajax({
          url: "http://localhost:5001/api/v1/milestones/" + id,
          type: "GET",
          dataType: "json",
          success: addMilestones,
        });
      },
    });
  });

  function addMilestones(data) {
    let listeningText = "";
    let receptiveLanguageText = "";
    let expressiveLanguageText = "";
    let speechText = "";
    let cognitionText = "";
    let socialCommunicationText = "";

    $.each(data, function (index, milestone) {
      switch (milestone.type) {
        case "Listening":
          listeningText += milestone.value + "<br>";
          break;
        case "Receptive Language":
          receptiveLanguageText += milestone.value + "<br>";
          break;
        case "Expressive Language":
          expressiveLanguageText += milestone.value + "<br>";
          break;
        case "Speech":
          speechText += milestone.value + "<br>";
          break;
        case "Cognition":
          cognitionText += milestone.value + "<br>";
          break;
        case "Social Communication":
          socialCommunicationText += milestone.value + "<br>";
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
