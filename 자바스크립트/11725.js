const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let n = Number(input[0]);
let edges = Array.from(Array(n + 1), () => Array());
let parents = new Array(n + 1).fill(0);

for (let i = 1; i < n; i++) {
  [x, y] = input[i].split(" ").map((value) => Number(value));
  edges[x].push(y);
  edges[y].push(x);
}

const bfs = () => {
  let queue = new Array();
  queue.push(1);
  while (queue.length > 0) {
    const cur = queue.shift();

    for (let i = 0; i < edges[cur].length; i++)
      if (parents[edges[cur][i]] === 0) {
        queue.push(edges[cur][i]);
        parents[edges[cur][i]] = cur;
      }
  }
};

bfs();
let result = "";
parents.slice(2).forEach((ans) => {
  result += ans + "\n";
});
console.log(result);
