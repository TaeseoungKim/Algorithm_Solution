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
let moves = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

const bfs = (graph, startNode) => {
  // x좌표, y좌표 , 횟수
  const queue = [[r1, c1, 0]];
  // 첫 좌표 방문 처리
  visited[r1][c1] = 1;
  while (queue.length) {
    const [x, y, cnt] = queue.shift();
    for (let [xi, yi] of direction) {
      const nx = x + xi;
      const ny = y + yi;
      if (nx >= 0 && ny >= 0 && nx < n && ny < n && !visited[nx][ny]) {
        visited[nx][ny] = 1;
        if (nx === r2 && ny === c2) {
          return cnt + 1;
        }
        queue.push([nx, ny, cnt + 1]);
      }
    }
  }
};

// 현재 위치랑 가장 가까운(이동 횟수가 가장 적은) 카드를 찾는 함수
function findNearCard(curPos, board) {
  let newQueue = new Queue();
  for (let move of moves) {
    let [y, x] = curPos;
    let [ty, tx] = move;

    while (0 <= y && y <= 3 && 0 <= x && x <= 3) {
      y += ty;
      x += tx;
      // 카드 찾으면 위치 리턴
      if (board[y][x] != 0) {
        return [y, x];
      }
    }
    // 카드 못 찾으면 끝 위치 리턴
    return [y, x];
  }
}

function solution(board, r, c) {
  var answer = 0;
  return answer;
}
