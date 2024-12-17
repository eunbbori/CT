//방법 1
let fs = require("fs");
// "/dev/stdin"
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

const numArr = input.slice(1).map((el) => Number(el));

const uniqueSortedArr = Array.from(numArr).sort((a, b) => a - b);

console.log(uniqueSortedArr.join("\n"));

//방법 2
console.log(
  require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .slice(1)
    .sort(function (a, b) {
      return a - b;
    })
    .join("\n")
);
