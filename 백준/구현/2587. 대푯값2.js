let fs = require("fs");
// "/dev/stdin"
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const numArr = input
  .map((el) => Number(el))
  .sort(function (a, b) {
    return a - b;
  });
const average = Math.floor(numArr.reduce((a, b) => a + b) / numArr.length);
const median = numArr[Math.floor(numArr.length / 2)];
console.log(average);
console.log(median);
