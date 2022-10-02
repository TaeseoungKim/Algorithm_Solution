function solution(board) {
  const N = board.length;
  // 목적지의 좌표 문자열값은 "NN"이 될 것
  const goal = N + "" + N;
  // [ [ 왼쪽좌표, 오른쪽좌표, deps ] ] 구조의 queue
  const queue = [[[1, 1], [1, 2], 0]];
  // 초기 점유 좌표 문자열은 "1112"
  const visit = new Set(["1112"]);
  // board.length + 2 크기의 2차원 배열 생성
  // 초기 상태는 모두 1(벽)으로 초기화
  const new_board = new Array(N + 2)
    .fill()
    .map((_) => new Array(N + 2).fill(1));
  // board 값에 해당하는 좌표는 다시 기존 board 값으로 갱신
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      new_board[i + 1][j + 1] = board[i][j];
    }
  }

  while (queue.length) {
    const [left, right, count] = queue.shift();
    // 로봇의 양 좌표 중 하나라도 목적지에 도달하면 종료
    if (left.join("") === goal || right.join("") === goal) return count;

    const nextPosition = getNextPosition(left, right, new_board);
    // 구한 경로를 방문할 수 있는지 없는지를 체크
    for (const next of nextPosition) {
      const [next_left, next_right] = next;
      const key = next_left.join("") + next_right.join("");
      if (!visit.has(key)) {
        queue.push([next_left, next_right, count + 1]);
        visit.add(key);
      }
    }
  }
}

const getNextPosition = (left, right, board) => {
  // X와 Y좌표 상수값 지정 (주어진 배열에서 둘의 위치에 주의하자)
  const X = 1;
  const Y = 0;
  // 로봇의 이동/회전이 끝난 후의 좌표를 저장할 배열
  const result = [];
  // 각 이동 경로 좌표 (상, 하, 좌, 우)
  const moves = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  for (const move of moves) {
    // dy, dx는 각각 상,하,좌,우로 이동을 적용하기 위한 값
    const [dy, dx] = move;
    // 전달받은 left와 right에 이동방향 적용
    const next_left = [left[Y] + dy, left[X] + dx];
    const next_right = [right[Y] + dy, right[X] + dx];

    // 이동이 끝난 좌표에 벽이 없다면 결과값에 추
    if (
      board[next_left[Y]][next_left[X]] === 0 &&
      board[next_right[Y]][next_right[X]] === 0
    ) {
      result.push([next_left, next_right]);
    }
  }

  // 로봇은 한 점을 기준으로 회전하기 때문에
  // 회전 경로 파악을 위해서는 현재 로봇의 위치를 기준으로
  // 가로 방향이면 위쪽과 아래쪽, 세로 방향이면 왼쪽과 오른쪽이
  // 모두 벽이 없는 상태여야 회전이 가능하다.
  const toward = [-1, 1];

  // 로봇이 가로로 배치된 경우
  if (left[Y] === right[Y]) {
    // 로봇의 위치를 기준으로 위쪽과 아래쪽을 확인
    for (const dy of toward) {
      // 위쪽 또는 오른쪽에 모두 벽이 없다면
      if (
        board[left[Y] + dy][left[X]] === 0 &&
        board[right[Y] + dy][right[X]] === 0
      ) {
        // 기존 왼쪽 좌표를 기준으로 상향 또는 하향 회전한 경로
        result.push([left, [left[Y] + dy, left[X]]]);
        // 기존 오른쪽 좌표를 기준으로 상향 또는  하향 회전한 경로
        result.push([[right[Y] + dy, right[X]], right]);
      }
    }
  }
  // 로봇이 세로로 배치된 경우
  else {
    // 로봇의 위치를 기준으로 왼쪽과 오른쪽을 확인
    for (const dx of toward) {
      // 왼쪽 또는 오른쪽에 모두 벽이 없다면
      if (
        board[left[Y]][left[X] + dx] === 0 &&
        board[right[Y]][right[X] + dx] === 0
      ) {
        // 기존 왼쪽 좌표를 기준으로 우향 또는 좌향 회전한 경로
        result.push([[left[Y], left[X] + dx], left]);
        // 기존 오른쪽 좌표를 기준으로 우향 또는 좌향 회전한 경로
        result.push([right, [right[Y], right[X] + dx]]);
      }
    }
  }

  return result;
};
