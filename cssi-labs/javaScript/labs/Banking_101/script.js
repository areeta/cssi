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

let customer_name;
let balance;
let logged_in = false;
let customer_password;

function openAccount(name, startingBalance = 0, password){
  balance = startingBalance;
  // Set the value for customer_name equal to name below
  customer_name = name;
  customer_password = password;
  return customer_name + " has opened a new account with a balance of $" + balance; //write the statment you need to return here
}

function deposit(value){
  // update the value of balance
  //return the correct statement
  balance += value;
  return customer_name + " has deposited " + value + ". " + customer_name + "'s total balance is $" + balance;
}

function withdraw(value){
  //update the value of balance
  //return the correct statement
  balance -= value;
  return customer_name + " has withdrawn " + value + ". " + customer_name + "'s has $" + balance + " remaining.";
}

function logIn(name, password) {
  if (name == customer_name && password == customer_password) {
    logged_in = true;
    return name + " has logged in.";
  } else {
    logged_in = false;
    return "Incorrect log in";
  }
}

// Write your script below

console.log(openAccount("Areeta", 300, "apples"));
console.log(deposit(50));
console.log(withdraw(500));
console.log(logIn("Areeta", "apples"));
