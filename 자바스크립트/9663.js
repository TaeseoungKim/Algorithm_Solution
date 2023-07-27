const isPossible = (curRow, curCol) => {
  for (let prevRow = 0; prevRow < curRow; prevRow++) {
    const prevCol = rows[prevRow];
    if (curCol === prevCol) return false;
    else if (curRow - prevRow === Math.abs(curCol - prevCol)) return false;
  }
  return true;
};

const dfs = (curRow) => {
  if (curRow === N) {
    wayCnt += 1;
    return;
  }

  for (let col = 0; col < N; col++)
    if (isPossible(curRow, col)) {
      rows[curRow] = col;
      dfs(curRow + 1);
      rows[curRow] = 0;
    }
};

const fs = require("fs");
const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "/Users/kimtaeseong/Documents/Algorithm_Solution/자바스크립트/input.txt";

const N = Number(fs.readFileSync(filePath).toString());
let wayCnt = 0;
const rows = Array(N).fill(0);
dfs(0);
console.log(wayCnt);
