// 방법 1 - 브루트포스
let fs = require("fs");
// "/dev/stdin"
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const cards = input[1].split(" ").map((el) => Number(el));
const N = input[0].split(" ")[0];
const M = input[0].split(" ")[1];

let answer = 0;

for (let i = 0; i < N; i++) {
  for (let j = i + 1; j < N; j++) {
    for (let k = j + 1; k < N; k++) {
      const sum = cards[i] + cards[j] + cards[k];
      const gap = M - sum;
      if (gap >= 0 && answer <= sum) {
        answer = sum;
      }
    }
  }
}
console.log(answer);

// 방법 2 - 투포인터
const fs = require("fs");
const buf = fs.readFileSync(0, "utf-8").toString().trim();

const inputs = buf.split("\n").map((input) => input.split(" ").map(Number));
const [n, m] = inputs[0];
const nums = inputs[1];

let result = 0;

nums.sort((a, b) => a - b);

for (let i = 0; i < n - 2; i++) {
  let left = i + 1;
  let right = n - 1;

  while (left < right) {
    const sum = nums[i] + nums[left] + nums[right];

    if (sum > m) {
      right--;
    } else {
      if (sum > result) {
        result = sum;
      }
      left++;
    }
  }

  if (result === m) {
    break;
  }
}

console.log(result);
