const fs = require(`fs`);
const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "/Users/kimtaeseong/Documents/Algorithm_Solution/자바스크립트/input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

const [R, C, T] = input[0].split(" ").map((v) => Number(v));
[_, ...input] = input;
let board = input.map((v) => v.split(" ").map((num) => Number(num)));

const move = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];
const airCleaner = [];
for (let x = 0; x < R; x++)
  for (let y = 0; y < C; y++) if (board[x][y] === -1) airCleaner.push([x, y]);

for (let i = 0; i < T; i++) {
  const tempBoard = Array.from(Array(R)).map((v) => Array(C).fill(0));
  tempBoard[airCleaner[0][0]][airCleaner[0][1]] = -1;
  tempBoard[airCleaner[1][0]][airCleaner[1][1]] = -1;
  for (let x = 0; x < R; x++) {
    for (let y = 0; y < C; y++) {
      if (board[x][y] > 0) {
        const adjacentV = parseInt(board[x][y] / 5);
        let expandCnt = 0;

        for (const [tx, ty] of move) {
          const nx = x + tx;
          const ny = y + ty;

          if (
            0 <= nx &&
            nx < R &&
            0 <= ny &&
            ny < C &&
            !(board[nx][ny] == -1)
          ) {
            tempBoard[nx][ny] += adjacentV;
            expandCnt++;
          }
        }
        tempBoard[x][y] += board[x][y] - adjacentV * expandCnt;
      }
    }
  }

  airCleanerMove(tempBoard);
  board = tempBoard.map((v) => [...v]);
}
function airCleanerMove(tempBoard) {
  const [top, bottom] = airCleaner;
  const [tx, ty] = top;
  const [bx, by] = bottom;
  // top
  for (let x = tx - 1; x > 0; x--) {
    tempBoard[x][0] = tempBoard[x - 1][0];
  }
  for (let y = 0; C - 1 > y; y++) {
    tempBoard[0][y] = tempBoard[0][y + 1];
  }

  for (let x = 0; tx > x; x++) {
    tempBoard[x][C - 1] = tempBoard[x + 1][C - 1];
  }
  for (let y = C - 1; y > 1; y--) {
    tempBoard[tx][y] = tempBoard[tx][y - 1];
  }
  // bottom
  for (let x = bx + 1; x < R - 1; x++) {
    tempBoard[x][0] = tempBoard[x + 1][0];
  }
  for (let y = 0; y < C - 1; y++) {
    tempBoard[R - 1][y] = tempBoard[R - 1][y + 1];
  }
  for (let x = R - 1; x > bx; x--) {
    tempBoard[x][C - 1] = tempBoard[x - 1][C - 1];
  }
  for (let y = C - 1; y > 1; y--) {
    tempBoard[bx][y] = tempBoard[bx][y - 1];
  }
  tempBoard[tx][1] = 0;
  tempBoard[bx][1] = 0;
}

let sumV = 0;
for (let x = 0; x < R; x++) {
  for (let y = 0; y < C; y++) {
    if (board[x][y] !== -1) sumV += board[x][y];
  }
}

console.log(sumV);
