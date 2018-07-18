console.log("Hello");

let name = "Ciera";
let daysLeft = 4;

console.log("Hello, " + name);
console.log("There are " + daysLeft + " days left in CSSI!");

if (daysLeft <  6) {
  console.log("Good luck on your final project");;
}

if (daysLeft <  6 && name == "Matthew") {
  console.log("Remember to help with final projects");;
}

if (name == "Ciera" || name == "Matthew"  || name == "Rachel") {
  console.log("You are an instructor");
} else if (name == "Julia" || name == "Jess") {
  console.log("You are a site lead");
} else if (name == "Logan" || name == "Sharon") {
  console.log("You are a TA");
} else {
  console.log("You are a student");
}

for (let i = 10; i >= 0 ; i--) {
  console.log(i);
}

console.log("Blast off");

// DRY - DON'T REPEAT YOURSELF

function greet(name) {
  console.log("Welcome, " + name + "!");
}

function fullName(firstName, lastName) {
  return (firstName + " " + lastName);
}

fullName("Alvin", "Ng");
fullName("Erin", "Wu");

greet("Alvin Ng");
greet("Erin Wu");

function square(number) {
  return  number * number;
}

square(8) + square(120);

let cSquared = square(3) + square(4);
console.log(cSquared);

function fourthPower(number) {
  return square(square(number));
}

console.log(fourthPower(2));
