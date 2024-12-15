// 방법1
let fs = require("fs");
// "/dev/stdin"
const input = fs.readFileSync("/dev/stdin").toString();
let num = 666;
let count = 1;

while (count < input) {
  num++;
  if (String(num).includes("666")) count++;
}
console.log(num);

// 방법2
const N = +require("fs").readFileSync("/dev/stdin").toString().trim();

let counter = 0;
let num2 = 665;
while (counter < N) {
  // 자리수를 하나씩 줄이는 방법
  // 원래 수에 10을 나눈다.
  num2++;
  let temp = num2;
  while (temp >= 666) {
    if (temp % 1000 === 666) {
      counter++;
      break;
    }
    temp = Math.floor(temp / 10);
  }
}

console.log(num2);
