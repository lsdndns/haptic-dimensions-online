const timeline = [
  {
    type: jsPsychHtmlButtonResponse,
    stimulus: "<p>Welcome! Click a button to continue.</p>",
    choices: ["Start"]
  },
  {
    type: jsPsychHtmlButtonResponse,
    stimulus: "<p>Which item doesn't fit?</p>",
    choices: ["Apple", "Banana", "Car"]
  }
];

jsPsych.run(timeline).then(() => {
  document.body.innerHTML = "<h2>Experiment finished!</h2>";
});


