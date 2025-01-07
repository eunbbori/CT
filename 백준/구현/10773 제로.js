let fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "백준/run/input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
input.shift();
let stack = [];
let sum = 0;

const N = input.length;

for (let i = 0; i < N; i++) {
  let el = Number(input[i]);
  if (el === 0) {
    stack.pop();
  } else {
    stack.push(el);
  }
}

for (let i = 0; i < stack.length; i++) {
  sum += stack[i];
}

console.log(sum);
