const robot = document.getElementById("robot");
const dog = document.getElementById("dog");

function startDance() {
  // Robot breakdance
  robot.classList.add("robot-spin-floor");
  document.querySelector(".robot .arm.left").classList.add("robot-arm-flail-left");
  document.querySelector(".robot .arm.right").classList.add("robot-arm-flail-right");
  document.querySelector(".robot .leg.left").classList.add("robot-leg-spin-left");
  document.querySelector(".robot .leg.right").classList.add("robot-leg-spin-right");

  // Dog reacts
  dog.classList.add("dog-bounce");
  document.querySelectorAll(".dog-leg").forEach(leg => leg.classList.add("dog-leg-flap"));
}

function stopDance() {
  // Robot stop
  robot.classList.remove("robot-spin-floor");
  document.querySelector(".robot .arm.left").classList.remove("robot-arm-flail-left");
  document.querySelector(".robot .arm.right").classList.remove("robot-arm-flail-right");
  document.querySelector(".robot .leg.left").classList.remove("robot-leg-spin-left");
  document.querySelector(".robot .leg.right").classList.remove("robot-leg-spin-right");

  // Dog stop
  dog.classList.remove("dog-bounce");
  document.querySelectorAll(".dog-leg").forEach(leg => leg.classList.remove("dog-leg-flap"));
}