// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log("Running Window Events Script");

let purpleBox = document.querySelector("#box6");

// insert a function that prints out the key code of a key pressed
window.addEventListener("keypress", e=> {
  if (e.keyCode == 99) {
    purpleBox.style.borderRadius = "50%";
    purpleBox.style.transform = "scale(0.5,0.5)";
  } else if (e.keyCode == 115) {
    purpleBox.style.borderRadius = "";
    purpleBox.style.transform = "scale(1,1)";
  }
});

let rectan = document.querySelector("#rect");

//When you scroll down 50px, have the rectangle on your page turn black.
window.addEventListener("scroll", e=> {
  if (window.pageYOffset <= 50) {
    rectan.style.backgroundColor = "black";
  }
})
