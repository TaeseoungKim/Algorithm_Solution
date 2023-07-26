const isPossible = (x, y, board) => {
  for (let i = 0; i < 8; i++) {
    const [tx, ty] = move[i];
    let nx = x;
    let ny = y;
    for (let d = 0; d < N; d++) {
      nx += tx;
      ny += ty;
      if (0 <= nx && nx < N && 0 <= ny && ny < N && board[nx][ny] === true)
        return false;
    }
  }
  return true;
};

const dfs = (x, board) => {
  console.log("before x+1", x + 1);
  for (let i = 0; i < N; i++) {
    if (isPossible(x, i, board))
      if (x === N - 1) {
        wayCnt += 1;
        continue;
      } else {
        board[x + 1][i] = true;
        dfs(x + 1, board);
        board[x + 1][i] = false;
      }
  }
};

const fs = require("fs");
const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "/Users/kimtaeseong/Documents/Algorithm_Solution/자바스크립트/input.txt";

// 모두를 true로 하지 말고, 그냥 퀸이 닿는거리에 있는지만 확인하면 되지않나?

const N = Number(fs.readFileSync(filePath).toString());
const move = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
  [1, 1],
  [-1, -1],
  [-1, 1],
  [1, -1],
];

isQueenArr = Array.from(Array(N), () => Array.from(Array(N).fill(false)));
let wayCnt = 0;

for (let i = 0; i < N; i++) {
  isQueenArr[0][i] = true;
  dfs(i, isQueenArr);
  isQueenArr[0][i] = false;
}

console.log(wayCnt);
