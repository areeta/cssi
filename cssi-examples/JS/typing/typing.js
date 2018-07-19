console.log("Hi");

// let box = document.querySelector("#box");
let boxes = document.querySelectorAll("div");

boxes.forEach(box => {
  //Passing "e" (the click event) and triggering a function
  box.addEventListener("mouseenter", e => {
    box.classList.add("spin");
  });

  //Passing "e" (the click event) and triggering a function
  box.addEventListener("mouseleave", e => {
    box.classList.remove("spin");
  });

});

window.addEventListener("keydown", e => {
  if (e.key == "g" || e.key == "G") {
    boxes.forEach(box => {
      box.classList.remove("red");
      box.classList.add("green");
    });
  } else if (e.key == "b" || e.key == "B") {
    boxes.forEach(box => {
      box.classList.remove("red", "green");
      box.classList.add("blue");
    });
  } else if (e.key == "r" || e.key == "R") {
    boxes.forEach(box => {
      box.classList.remove("blue", "green");
      box.classList.add("red");
    });
  }
});
