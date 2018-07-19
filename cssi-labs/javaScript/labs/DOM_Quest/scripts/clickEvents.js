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

console.log("Running Click Events Script");

let red = document.querySelector("#box1");
let pink = document.querySelector("#box2");
let orange = document.querySelector("#box3");

let colors = [red, pink, orange];

colors.forEach(color => {

  red.addEventListener("click", e => {
    pink.style.backgroundColor = "red";
    orange.style.backgroundColor = "red";
    red.style.backgroundColor = "red";
  });

  pink.addEventListener("click", e => {
    red.style.backgroundColor = "pink";
    orange.style.backgroundColor = "pink";
    pink.style.backgroundColor = "pink";
  });

  orange.addEventListener("click", e => {
    pink.style.backgroundColor = "orange";
    red.style.backgroundColor = "orange";
    orange.style.backgroundColor = "orange";

  });


});

//2nd Challenge

let yellow = document.querySelector("#box4");
let blue = document.querySelector("#box5");

yellow.addEventListener("click", e => {
  yellow.classList.toggle("active");
});

blue.addEventListener("click", e => {
  blue.classList.toggle("active");
});
