console.log("something");

let score1 = 97;
let score2 = 92;
let score3 = 90;

//Array
let scores = [97, 92, 90, 87, 88, 100, 99, 105];

// First thing in parameter is index putting in, second is what deleting, third is replacement.
// scores.splice(1, 0, 93);

//.push() adds a value in and .pop() takes off the last value

//Find the maximum number
let maxNum = scores[0];
for (let i = 0; i < scores.length; i++) {
  if (scores[i] > maxNum) {
    maxNum = scores[i];
  }
}
console.log("The maximum score is " + maxNum);

//Write a loop that calculates the total + log out the total;
let total = 0;
for (let i = 0; i < scores.length; i++) {
  total += scores[i];
}
console.log("The total is " + total);

//Welcome everyone
let names = ["Savion", "Jenny", "Olivia", "Joshua"];
names.forEach(name => {
  console.log("Welcome, " + name);
});

//JavaScript objects

//Can go into each element by doing matthew["firstName"] or matthew.firstName
let matthew = {
  "firstName": "Matthew",
  "lastName": "Levine",
  "university": "Dartmouth",
  "culture": "Harry Potter",
};
console.log(matthew.university);

let yojairo = {
  "firstName": "Yojairo",
  "lastName": "Morales",
  "university": "USC",
  "culture": "Kendrick Lamar",
};

let people = [matthew, yojairo];

people.forEach(person => {
  console.log(person.firstName + " really likes " + person.culture + ".");
});
