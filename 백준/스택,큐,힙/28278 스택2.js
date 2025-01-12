let fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "백준/run/input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
input.shift();
let stack = [];
let result = [];

const N = input.length;

for (let i = 0; i < N; i++) {
  let command = input[i].split(" ");

  switch (command[0]) {
    case "1":
      // push X
      stack.push(Number(command[1]));
      break;
    case "2":
      result.push(stack.length ? stack.pop() : -1);
      break;
    case "3":
      result.push(stack.length);
      break;
    case "4":
      result.push(stack.length ? 0 : 1);
      break;
    case "5":
      result.push(stack.length ? stack[stack.length - 1] : -1);
      break;
  }
}

console.log(result.join("\n"));
