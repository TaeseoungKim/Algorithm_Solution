const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

class node {
  constructor() {
    this.parent = null;
  }
}
// 아 처음부터 bfs로 접근해야 하는 문제였음.. 접근 순서가 중요하기 떄문이다
let n = Number(input[0]);
let edges = Array.from(Array(n + 1), () => Array());
let nodes = Array.from(Array(n + 1), () => new node());

for (let i = 1; i < n; i++) {
  [x, y] = input[i].split(" "); // 구조분해 할당
  edges[x].push(y);
  edges[y].push(x);
}

for (let i = 1; i <= n; i++) {
  console.log(`edges${i}:`, edges[i]);
  for (let d = 0; d < edges[i].length; d++) {
    if (nodes[edges[i][d]].parent === null && edges[i][d] != 1) {
      nodes[edges[i][d]].parent = i;
      console.log(`edges${edges[i][d]}의 부모는:${i}`);
    }
  }
  console.log();
}

console.log("nodes", nodes);
for (let i = 2; i <= n; i++) {
  console.log(nodes[i].parent);
}
