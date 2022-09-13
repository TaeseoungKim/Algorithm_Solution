let board = [
  [1, 0, 0, 3],
  [2, 0, 0, 0],
  [0, 0, 0, 2],
  [3, 0, 1, 0],
];
let r = 1;
let c = 0;

let curPos = [r, c];

// 상하좌우
const move = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

const direction = [
  [-2, -1],
  [-2, 1],
  [0, -2],
  [0, 2],
  [2, -1],
  [2, 1],
];

const FindCard_bfs = (curPos, board) => {
  const visited = Array.from(Array(4), () => Array(4).fill(0));
  let CardPos = false;
  // y좌표, x좌표 , 횟수
  const queue = [[...curPos, 0]];
  console.log("queue", queue);
  // 첫 좌표 방문 처리
  visited[curPos[0]][curPos[1]] = 1;
  while (queue.length) {
    const [y, x, cnt] = queue.shift();
    visited[y][x] = 1;
    console.log("y,x,cnt", y, x, cnt);
    let endPoint = [
      [0, x],
      [y, 0],
      [3, x],
      [y, 3],
    ];

    visited.forEach((element) => {
      console.log("element", element);
    });

    console.log("endPoint", endPoint);
    for (let [ty, tx] of endPoint) {
      console.log("[ty, tx]", ty, tx);
      if (visited[ty][tx] == 0) {
        visited[ty][tx] = 1;
        if (board[ty][tx] != 0) {
          CardPos = [ty, tx, cnt + 1];
          return [ty, tx, cnt + 1];
        } else queue.push([ty, tx, cnt + 1]);
      }
    }

    visited.forEach((element) => {
      console.log("element", element);
    });

    for (let [yi, xi] of move) {
      let ny = y + yi;
      let nx = x + xi;

      while (nx > 0 && ny > 0 && nx < 3 && ny < 3 && !visited[ny][nx]) {
        visited[ny][nx] = 1;
        //카드일 경우 반복문 종료
        if (board[ny][nx] != 0) {
          CardPos = [ny, nx, cnt + 1];
          return [ty, tx, cnt + 1];
        }

        queue.push([nx, ny, cnt + 1]);
        ny += yi;
        nx += xi;
      }
    }
  }
};

console.log(curPos);
console.log(FindCard_bfs(curPos, board));

// // 현재 위치랑 가장 가까운(이동 횟수가 가장 적은) 카드를 찾는 함수
// function findNearCard(curPos, board) {
//   let newQueue = new Queue();
//   for (let move of moves) {
//     let [y, x] = curPos;
//     let [ty, tx] = move;

//     while (0 <= y && y <= 3 && 0 <= x && x <= 3) {
//       y += ty;
//       x += tx;
//       // 카드 찾으면 위치 리턴
//       if (board[y][x] != 0) {
//         return [y, x];
//       }
//     }
//     // 카드 못 찾으면 끝 위치 리턴
//     return [y, x];
//   }
// }

// function solution(board, r, c) {
//   var answer = 0;
//   return answer;
// }
