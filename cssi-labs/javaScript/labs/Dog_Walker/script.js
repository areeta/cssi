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

// Task 1
let dogName1 = "Steve";
let dogType1 = "beagle";

// Complete Task 1 Below

console.log("I will walk " + dogName1 + " today at 12:00pm.")


let dogName2 = "Joe";
let dogType2 = "bulldog";

// Complete Task 2 Below

if (dogType2 == "corgi") {
  console.log("I will walk " + dogName2 + " at 12:00pm.");
} else {
  console.log("I will walk " + dogName2 + " today at 1:00pm.");
}


let dogName = "Lola";
let dogType = "poodle";

// Complete Task 3 Below

if (dogType == "corgi" || dogType == "beagle") {
  console.log("I will walk " + dogName + " at 12:00pm.");
} else if (dogType == "bulldog") {
  console.log("I will walk " + dogName + " at 1:00pm.")
} else {
  console.log("I will walk " + dogName + " today at 2:00pm.")
}


//Extension

let dogOwner = prompt("What is your favorite dog?");
dogOwner.toLowerCase();

if (dogOwner == "spike" ) {
  console.log("I will walk Spike, one of my favorite dogs, today at 3:00pm.");
} else if (dogOwner == "jeremy") {
  console.log("I will walk Jeremy, one of my favorite dogs, today at 4:00pm.");
} else if (dogOwner == "lola") {
  console.log("I will walk Lola, one of my favorite dogs, today at 2:00pm.");
} else if (dogOwner == "peaches") {
  console.log("I will walk Peaches, one of my favorite dogs, today at 5:00pm.");
} else if (dogOwner == "steve") {
  console.log("I will walk Steve, one of my favorite dogs, today at 12:00pm.");
}
