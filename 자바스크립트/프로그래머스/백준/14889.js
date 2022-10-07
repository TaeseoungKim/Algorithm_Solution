// 4
// 0 1 2 3
// 4 0 5 6
// 7 1 0 2
// 3 4 5 0

const fs = require("fs");
const filePath =
  "/Users/kimtaeseong/Documents/Algorithm_Solution/자바스크립트/프로그래머스/백준/input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
const N = Number(input[0]);
const board = input.splice(1).map((v) => v.split(" "));
// 사실상 고려해야 될게, 1~4 에서의 순서쌍인거네
// 1,2 1,3 1,4
// 2,3 2,4
// 3,4 4,3

// 이 중에서 2가지, 2가지를 선택하는 경우의 수를 구하고,
// 각 경우의 사이의 차이마다 최소를 구하는 거야
// (1,4) (4,1)
// (2,4) (4,2)

function recursion(start, link, visited) {
  if (start == N / 2 && link == N / 2) return;
  else {
    if (start < N / 2) {
      recursion(start + 1, link);
    }
    if (link < N / 2) return;
  }
}

console.log(board);
