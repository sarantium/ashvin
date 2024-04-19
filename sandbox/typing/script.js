// script.js
document.getElementById("typing-area").addEventListener("input", function () {
  var sourceText = document.getElementById("source-text").textContent;
  var userInput = this.value;

  if (userInput === sourceText) {
    document.getElementById("feedback").textContent = "Well done!";
    this.style.borderColor = "green";
  } else {
    document.getElementById("feedback").textContent = "Keep typing...";
    this.style.borderColor = "red";
  }
});
