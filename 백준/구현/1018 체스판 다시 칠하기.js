let fs = require("fs");
// "/dev/stdin"
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number); // N: 행 , M: 열
const board = input.slice(1);

function countRepaints(board, startX, startY, isWhiteStart) {
  let repaintCount = 0;
  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      const isWhite = (i + j) % 2 === 0;
      const expected = isWhiteStart === isWhite ? "W" : "B";
      if (board[startX + i][startY + j] !== expected) {
        // 현재 칸의 색상과 정상적인 체스판 비교
        repaintCount++;
      }
    }
  }
  return repaintCount;
}

let minRepaint = Infinity;
for (let i = 0; i <= N - 8; i++) {
  for (let j = 0; j <= M - 8; j++) {
    const repaintWhite = countRepaints(board, i, j, true);
    const repaintBlack = countRepaints(board, i, j, false);
    minRepaint = Math.min(minRepaint, repaintWhite, repaintBlack);
  }
}

console.log(minRepaint);
