// 백트래킹인줄 알았으나, DFS였음
function solution(info, edges) {
  let MaxSheep = 1;
  n = edges.length;
  // 서로 연결된 정보를 담고 있는 2차원 배열
  board = new Array(n + 1).fill().map((_) => []);
  visited = new Array(n + 1).fill().map((_) => false);

  // board에 연결정보 입력
  edges.forEach((element) => {
    const [n1, n2] = element;
    board[n1].push(n2);
  });

  function DFS(curInfo, nextNodes) {
    let [curNode, sheep, wolf] = curInfo;
    const curNodeIdx = nextNodes.indexOf(curNode);

    sheep += !info[curNode];
    wolf += info[curNode];
    MaxSheep = Math.max(MaxSheep, sheep);

    if (wolf === sheep) return;

    nextNodes.splice(curNodeIdx, 1);
    nextNodes.push(...board[curNode]);

    nextNodes.forEach((nextNode) =>
      DFS([nextNode, sheep, wolf], [...nextNodes])
    );
  }

  DFS([0, 0, 0], [0]);
  return MaxSheep;
}
