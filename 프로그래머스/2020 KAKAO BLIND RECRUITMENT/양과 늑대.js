// 백트래킹인줄 알았으나, DFS였음

let MaxSheep = 1;
edges = [
  [0, 1],
  [1, 2],
  [1, 4],
  [0, 8],
  [8, 7],
  [9, 10],
  [9, 11],
  [4, 3],
  [6, 5],
  [4, 6],
  [8, 9],
];
info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1];
n = edges.length;
// 서로 연결된 정보를 담고 있는 2차원 배열
board = new Array(n + 1).fill().map((_) => []);
visited = new Array(n + 1).fill().map((_) => false);

// board에 연결정보 입력
edges.forEach((element) => {
  const [n1, n2] = element;
  board[n1].push(n2);
});

const DFS_Stack = [0];
