function SortNumber(a, b) {
  return a - b;
}

const fs = require("fs");
const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "/Users/kimtaeseong/Documents/Algorithm_Solution/자바스크립트/input.txt";
const input = fs.readFileSync(filePath).toString().split("\n");
const [N, K] = [Number(input[0]), Number(input[1])];
const board = input[2]
  .split(" ")
  .map((v) => Number(v))
  .sort(SortNumber);
const dist = [];

board.forEach((v, idx) => {
  if (idx === 0) return;
  dist.push(board[idx] - board[idx - 1]);
});

dist.sort((a, b) => {
  return b - a;
});
let answer = 0;
for (let i = K - 1; i < N - 1; i++) {
  answer += dist[i];
}
console.log(answer);
