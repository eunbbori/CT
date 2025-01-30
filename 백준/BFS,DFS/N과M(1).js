//방법 - 재귀
let fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "백준/run/input.txt";

const input = fs.readFileSync(filePath).toString().trim().split(" ");

const [N, M] = input.map(Number);

const visited = new Array(N + 1).fill(false);
const array = [];

const dfs = (cnt) => {
  if (cnt === M) {
    console.log(array.join(" "));
    return;
  }
  for (let i = 1; i <= N; i++) {
    if (!visited[i]) {
      visited[i] = true;
      array[cnt] = i;
      dfs(cnt + 1);
      visited[i] = false;
    }
  }
};

dfs(0);
