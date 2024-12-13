// 방법 1

let fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
let answer = [];

let OriginArr = [1, 1, 2, 2, 2, 8];

//킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로
for (let i = 0; i < input.length; i++) {
  answer.push(OriginArr[i] - Number(input[i]));
}

console.log(answer.join(" "));

// 방법 2

const input2 = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const chess = [1, 1, 2, 2, 2, 8];

console.log(input2.map((e, i) => chess[i] - e).join(" "));
