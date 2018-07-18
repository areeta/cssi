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

console.log("script is running...");

function My_Alarm(time) {
  console.log("Hey, Areeta, wake up! It's " + time + ".");
}

console.log(My_Alarm("8:00AM"));

function Mom_Alarm(time) {
  console.log("Hey, Mom, wake up! It's " + time + ".");
}

console.log(Mom_Alarm("8:00AM"));

function Family_Alarm(time, name) {
  return "Hey, " + name + " , wake up! It's " + time+ ".";
}

console.log(Family_Alarm("Iris", "8:00AM"));

function Important_Alarm(message) {
  return message.toUpperCase();
}

console.log(Important_Alarm("wake upppp"));

function Snooze_Alarm(numTime) {
  let newTime = numTime++;
  return "The alarm for " + numTime + " has been changed to " + newTime;
}

console.log(Snooze_Alarm("8"));

function People_Alarm(peopleNum) {
  for (let i = 0; i < peopleNum; i++) {
    console.log("Wake up!");
  }
}

People_Alarm(5);
