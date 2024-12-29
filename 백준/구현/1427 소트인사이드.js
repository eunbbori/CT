let fs = require("fs");
// "/dev/stdin"
const input = fs
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("")
  .map((item) => Number(item));

input.sort((a, b) => b - a);

console.log(input.join(""));
