let fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "백준/run/input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");
const testCase = Number(input[0]);

input.shift();
let answer = [];

for (let i = 0; i < testCase; i++) {
  let stack = [];
  let isVPS = true;

  for (let j = 0; j < input[i].length; j++) {
    if (input[i][j] === "(") {
      stack.push("(");
    } else if (input[i][j] === ")") {
      if (stack.length === 0) {
        isVPS = false;
        break;
      }
      stack.pop();
    }
  }

  if (stack.length === 0 && isVPS) {
    answer.push("YES");
  } else {
    answer.push("NO");
  }
}

console.log(answer.join("\n"));
