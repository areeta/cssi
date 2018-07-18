console.log("Hello!");

let likeButton = document.querySelector("#like");
likeButton.addEventListener("click", e => {
  likeButton.innerText = "👍";
  likeButton.disabled = true;
});

let growButton = document.querySelector("#grow");
growButton.addEventListener("click", e=> {
  let currentSize = growButton.style.fontSize;
  let newSize = parseInt(currentSize) + 10;
  growButton.style.fontSize = newSize + "px";
})
