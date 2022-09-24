solution();
function solution(n, build_frame) {
  n = 5;
  build_frame = [
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 0, 1],
    [2, 2, 1, 1],
    [5, 0, 0, 1],
    [5, 1, 0, 1],
    [4, 2, 1, 1],
    [3, 2, 1, 1],
  ];

  let board = new Array(n + 1)
    .fill()
    .map((_) => new Array(n + 1).fill().map((_) => 0));

  let curStructure = []; // 현재 설치된 구조물을 담는 배열

  for (let [x, y, a, b] of build_frame) {
    // 삭제일 경우,
    if (b == 0) {
      // 아무것도 없을 경우 무시,
      if (board[x][y] == 0) return;

      // 일단 삭제해보고, 설치된 구조물 들이 possible 아니면 다 지워버림,
      let newBoard = board.map((v) => v.slice());
      let tmp = -1;
      let DeletedIdx = 0;
      newBoard[x][y] = 0;

      for (let [tx, ty, ta] of curStructure) {
        tmp++;
        if (tx == x && ty == y && ta == ta) continue;
        else if (!isPossible([tx, ty, ta], newBoard)) {
          tmp = false;
          break;
        }
      }

      if (tmp) {
        board[x][y] = 0;
        curStructure = [
          ...curStructure.slice(0, DeletedIdx),
          ...curStructure.slice(DeletedIdx),
        ];
      }
    }
    // 설치일 경우,
    else {
      if (isPossible([x, y, a], board)) {
        curStructure.push([x, y, a]);
        if (a === 0) board[x][y] = 1;
        else board[x][y] = 2;
      }
    }
  }
  function isPossible([x, y, a], board) {
    // "기둥"일 경우,
    if (a == 0) {
      // 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
      if (y === 0) return true;
      else if (board[x - 1][y] == 2 || board[x][y] == 2) return true;
      else false;
    }
    // "보"일 경우
    else if (a == 1) {
      // 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
      if (board[x][y - 1] == 1 || board[x + 1][y] == 1) return true;
      else if (board[x - 1][y] == 2 && board[x + 1][y] == 2) return true;
      else false;
    }
  }
}
