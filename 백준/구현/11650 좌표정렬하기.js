// 방법 1

let fs = require("fs");
// "/dev/stdin"
const input = fs.readFileSync("input.txt").toString().trim().split("\n");
const N = Number(input[0]);
let arr = [];

for (let i = 1; i <= N; i++) {
  let [a, b] = input[i].split(" ").map(Number);
  arr.push([a, b]);
}

arr.sort((a, b) => {
  if (a[0] !== b[0]) return a[0] - b[0];
  else return a[1] - b[1];
});

let answer = "";
for (let i = 0; i < N; i++) {
  answer += arr[i][0] + " " + arr[i][1] + "\n";
}
console.log(answer);

// 방법 2
