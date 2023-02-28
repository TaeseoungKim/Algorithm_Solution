const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let n = Number(input[0]);
let T = [];
let P = [];

let board = new Array(n + 1).fill(0);
for (let i = 1; i <= n; i++) {
  let [t, p] = input[i].split(" ").map((value) => Number(value));
  T.push(t);
  P.push(p);
}

for (let i = n - 1; i >= 0; i--) {
  if (n < i + T[i]) board[i] = board[i + 1];
  else board[i] = Math.max(board[i + 1], P[i] + board[i + T[i]]);
}

console.log(Math.max(...board));
