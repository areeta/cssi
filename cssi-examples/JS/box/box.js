
let rightButton = document.querySelector("#right");
rightButton.addEventListener("click", e=> {
  let box = document.querySelector("#box");
  let currentLeft = box.style.left;
  let newLeft = parseInt(currentLeft) + 10;
  box.style.left = newLeft + "px";
});

let leftButton = document.querySelector("#left");
leftButton.addEventListener("click", e=> {
  let box = document.querySelector("#box");
  let currentRight = box.style.left;
  let newRight = parseInt(currentRight) - 10;
  box.style.left = newRight + "px";
});

let upButton = document.querySelector("#up");
upButton.addEventListener("click", e=> {
  let box = document.querySelector("#box");
  let currentUp = box.style.top;
  let newUp = parseInt(currentUp) - 10;
  box.style.top = newUp + "px";
});

let downButton = document.querySelector("#down");
downButton.addEventListener("click", e=> {
  let box = document.querySelector("#box");
  let currentDown = box.style.top;
  let newDown = parseInt(currentDown) + 10;
  box.style.top = newDown + "px";
});
