// 방법 1

let fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const count = Number(input[0]);

let answer = 0;

for (i = 1; i <= count; i++) {
  let word = input[i];
  let flag = true;
  let used = [];
  for (let j = 0; j < word.length; j++) {
    const char = word[j];
    if (!used.includes(char)) {
      used.push(char);
    } else if (char !== word[j - 1]) {
      flag = false;
      break;
    }
  }
  if (flag) answer++;
}

console.log(answer);

// 방법 2

const fs = require("fs");
const input2 = fs.readFileSync("/dev/stdin").toString().split("\n");

const N = Number(input2[0]);
let count2 = N;
let word;

for (let i = 1; i <= N; i++) {
  word = input2[i];
  for (let j = 0; j < word.length - 1; j++) {
    if (word[j] != word[j + 1] && !!word.slice(j + 1).includes(word[j])) {
      count2--;
      break;
    }
  }
}
console.log(count2);
