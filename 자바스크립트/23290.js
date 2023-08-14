const moviDir = [
  [0, -1],
  [-1, -1],
  [-1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
  [1, 0],
  [1, -1],
];

function moveFish(fx, fy, fd) {
  let fishDir = fd;

  for (let i = 0; i < 8; i++) {
    if (i !== 0)
      if (fishDir == 0) fishDir = 7;
      else fishDir = fishDir - 1;

    const [tx, ty] = moviDir[fishDir];
    const [nx, ny] = [tx + fx, ty + fy];

    if (
      0 <= nx &&
      nx < 4 &&
      0 <= ny &&
      ny < 4 &&
      smellBoard[nx][ny] == 0 &&
      !(sharkPos[0] === nx && sharkPos[1] === ny)
    ) {
      return [nx, ny, fishDir];
    }
  }
  return [fx, fy, fd];
}

const sharkDir = [
  [-1, 0],
  [0, -1],
  [1, 0],
  [0, 1],
];

function moveShark() {
  let eatArr = [];
  let feed = 0;

  for (let i = 0; i < 4; i++) {
    for (let d = 0; d < 4; d++)
      for (let x = 0; x < 4; x++) {
        const [x1, y1] = sharkDir[i];
        const [x2, y2] = sharkDir[d];
        const [x3, y3] = sharkDir[x];
        const [nx1, ny1] = [sharkPos[0] + x1, sharkPos[1] + y1];
        const [nx2, ny2] = [nx1 + x2, ny1 + y2];
        const [nx3, ny3] = [nx2 + x3, ny2 + y3];

        if (
          0 <= nx1 &&
          nx1 < 4 &&
          0 <= ny1 &&
          ny1 < 4 &&
          0 <= nx2 &&
          nx2 < 4 &&
          0 <= ny2 &&
          ny2 < 4 &&
          0 <= nx3 &&
          nx3 < 4 &&
          0 <= ny3 &&
          ny3 < 4
        ) {
          let tempFeed = 0;
          if (nx1 === nx3 && ny1 === ny3) {
            tempFeed = fishboard[nx1][ny1].length + fishboard[nx2][ny2].length;
          } else {
            tempFeed =
              fishboard[nx1][ny1].length +
              fishboard[nx2][ny2].length +
              fishboard[nx3][ny3].length;
          }

          if (eatArr.length === 0) {
            feed = tempFeed;
            eatArr.push([nx1, ny1, fishboard[nx1][ny1].length]);
            eatArr.push([nx2, ny2, fishboard[nx2][ny2].length]);
            eatArr.push([nx3, ny3, fishboard[nx3][ny3].length]);
          } else if (feed < tempFeed) {
            feed = tempFeed;
            eatArr = [];
            eatArr.push([nx1, ny1, fishboard[nx1][ny1].length]);
            eatArr.push([nx2, ny2, fishboard[nx2][ny2].length]);
            eatArr.push([nx3, ny3, fishboard[nx3][ny3].length]);
          }
        }
      }
  }

  for (let i = 0; i < 3; i++) {
    const [nx, ny, eaten] = eatArr[i];
    if (eaten !== 0) {
      smellBoard[nx][ny] = 3;
      fishboard[nx][ny] = [];
    }
  }
  sharkPos = [eatArr[2][0], eatArr[2][1]];
}
function deepCopy(arr) {
  let copy = [];
  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
      copy[i] = deepCopy(arr[i]); // 재귀적으로 깊은 복사 수행
    } else {
      copy[i] = arr[i];
    }
  }
  return copy;
}

const fs = require("fs");
const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "/Users/kimtaeseong/Documents/Algorithm_Solution/자바스크립트/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const baseBoard = Array.from(Array(4), (v) => Array.from(Array(4), () => []));
const [M, S] = input[0].split(" ").map((v) => Number(v));
let fishboard = Array.from(Array(4), (v) => Array.from(Array(4), () => []));
const smellBoard = Array.from(Array(4), (v) => Array.from(Array(4), () => 0));

for (let i = 1; i <= M; i++) {
  const [x, y, d] = input[i].split(" ").map((v) => Number(v));
  fishboard[x - 1][y - 1].push(d - 1);
}

let sharkPos = input[input.length - 1].split(" ").map((v) => Number(v) - 1);

for (let i = 1; i <= S; i++) {
  const copyBoard = deepCopy(fishboard); // 1번
  const tempBoard = [];
  for (let x = 0; x < 4; x++)
    for (let y = 0; y < 4; y++) {
      const fishLen = fishboard[x][y].length;
      for (let d = 0; d < fishLen; d++) {
        const fd = fishboard[x][y].pop();
        const res = moveFish(x, y, fd);
        tempBoard.push(res);
      }
    }
  fishboard = deepCopy(baseBoard);
  for (let d = 0; d < tempBoard.length; d++) {
    const [fx, fy, fd] = tempBoard[d];
    fishboard[fx][fy].push(fd);
  } // 2번 완료

  moveShark(); // 3번
  for (let x = 0; x < 4; x++)
    for (let y = 0; y < 4; y++)
      if (smellBoard[x][y] !== 0) smellBoard[x][y] -= 1; // 4번

  for (let x = 0; x < 4; x++)
    for (let y = 0; y < 4; y++) {
      fishboard[x][y] = [...copyBoard[x][y], ...fishboard[x][y]];
    }
}

let sumV = 0;
for (let x = 0; x < 4; x++)
  for (let y = 0; y < 4; y++) {
    sumV += fishboard[x][y].length;
  }

console.log(sumV);
