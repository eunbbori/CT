// 방법 1
// let fs = require("fs");
// const filePath =
//   process.platform === "linux" ? "/dev/stdin" : "백준/run/input.txt";

// const input = fs.readFileSync(filePath).toString().trim().split("\n");

// // 입력 처리
// const [originLen, newNum, limitLen] = input[0].split(" ").map(Number);
// const originArr = input[1] ? input[1].split(" ").map(Number) : [];

// // 배열 정렬
// const sortedArr = originArr.sort((a, b) => b - a);

// let rank = 1;
// let answer = -1;

// if (originLen === 0) {
//   // 기존 배열이 비었으면 바로 1등
//   answer = 1;
// } else {
//   for (let i = 0; i <= sortedArr.length; i++) {
//     // 새로운 숫자가 배열 끝에 도달하거나 삽입 가능한 위치를 찾은 경우
//     if (i === sortedArr.length || sortedArr[i] < newNum) {
//       if (rank <= limitLen) {
//         answer = rank; // 제한 안에 순위가 들어가면 답 설정
//       }
//       break;
//     }

//     // 동점 처리
//     if (sortedArr[i] > newNum) {
//       rank++;
//       if (rank > limitLen) {
//         answer = -1; // 제한을 초과하면 답은 -1
//         break;
//       }
//     }
//   }

//   // 동점으로 끝나도 배열이 꽉 찼으면 -1 반환
//   if (originLen >= limitLen && sortedArr[sortedArr.length - 1] === newNum) {
//     answer = -1;
//   }
// }

// console.log(answer);

//방법 2
let fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "백준/run/input.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

// 입력 처리
const [originLen, newNum, limitLen] = input[0].split(" ").map(Number);
const originArr = input[1] ? input[1].split(" ").map(Number) : [];

// 태수의 점수를 리스트에 삽입
originArr.push(newNum);

// 리스트를 내림차순으로 정렬
const arrSorted = originArr.sort((a, b) => b - a);

// 태수의 점수와 동일한 값들의 인덱스를 구함
let indexes = [];
for (let i = 0; i < arrSorted.length; i++) {
  if (arrSorted[i] === newNum) {
    indexes.push(i + 1); // 인덱스를 1부터 시작하도록 1을 더함
  }
}

// 태수의 점수가 랭킹 리스트 밖에 있는지 확인
if (indexes[indexes.length - 1] > limitLen) {
  console.log(-1); // 랭킹 밖이면 -1 출력
} else {
  console.log(indexes[0]); // 첫 번째 인덱스(최고 순위)를 출력
}
