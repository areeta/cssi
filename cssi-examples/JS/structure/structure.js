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

let total = 0;
for (let i = 0; i < scores.length; i++) {
  total += scores[i];
}

console.log("The total is " + total);
