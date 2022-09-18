function solution(n, s, a, b, fares) {
  // 플로이드 와샬 알고리즘 구현을 위한 dp 배열
  const board = new Array(n).fill().map((_) => new Array(n).fill(Infinity));

  // 각 노드의 자기 자신에 대한 가중치 값 0으로 초기화
  for (let i = 0; i < n; i++) {
    board[i][i] = 0;
  }

  // 각 노드가 가진 간선의 가중치 값 초기화
  fares.forEach((element) => {
    const [n1, n2, wei] = element;
    board[n1 - 1][n2 - 1] = wei;
    board[n2 - 1][n1 - 1] = wei;
  });

  // 각 노드에서 나머지 모든 노드까지의 최단경로 초기화
  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (board[i][j] > board[i][k] + board[k][j])
          board[i][j] = board[i][k] + board[k][j];
      }
    }
  }

  // 기본 결괏값을 A,B가 따로 갈 경우로 초기화
  let result = board[s - 1][a - 1] + board[s - 1][b - 1];

  // 각 노드를 돌며 합승 지점까지 들렸다 헤어지는게 더 빠르다면 결괏값 변경
  for (let i = 0; i < n; i++) {
    result = Math.min(
      result,
      board[s - 1][i] + board[i][a - 1] + board[i][b - 1]
    );
  }
  return result;
}
