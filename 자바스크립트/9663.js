// const isPossible = (x, y, queenDict) => {
//     const cx = Number(x)
//     const cy = Number(y)

//   for (const key in queenDict) {
//     const tx = Number(queenDict[key][0] + queenDict[key][1]);
//     const ty = Number(queenDict[key][2] + queenDict[key][3]);

//     if cx=tx
//   }

//   if tx-ty === Math(tx)-

//   for (let i = 0; i < 8; i++) {
//     const [tx, ty] = move[i];
//     let nx = x;
//     let ny = y;
//     for (let d = 0; d < N; d++) {
//       nx += tx;
//       ny += ty;

//       const strNx = nx < 10 ? "0" + nx : nx.toString();
//       const strNy = ny < 10 ? "0" + ny : ny.toString();

//       if (0 <= nx && nx < N && 0 <= ny && ny < N && strNx + strNy in queenDict)
//         return false;
//     }
//   }
//   return true;
// };

// const dfs = (x, queenDict) => {
//   for (let i = 0; i < N; i++) {
//     if (isPossible(x + 1, i, queenDict))
//       if (x + 1 === N - 1) {
//         wayCnt += 1;
//         continue;
//       } else {
//         const strNx = x + 1 < 10 ? "0" + (x + 1) : (x + 1).toString();
//         const strNy = i < 10 ? "0" + i : i.toString();
//         queenDict[strNx + strNy] = true;
//         dfs(x + 1, queenDict);
//         delete queenDict[strNx + strNy];
//       }
//   }
// };

// const fs = require("fs");
// const filePath =
//   process.platform === "linux"
//     ? "/dev/stdin"
//     : "/Users/kimtaeseong/Documents/Algorithm_Solution/자바스크립트/input.txt";

// // 모두를 true로 하지 말고, 그냥 퀸이 닿는거리에 있는지만 확인하면 되지않나?

// const N = Number(fs.readFileSync(filePath).toString());
// const move = [
//   [0, 1],
//   [1, 0],
//   [0, -1],
//   [-1, 0],
//   [1, 1],
//   [-1, -1],
//   [-1, 1],
//   [1, -1],
// ];

// isQueenDict = {};

// let wayCnt = 0;

// for (let i = 0; i < N; i++) {
//   isQueenDict["00" + (i < 10 ? "0" + i : i.toString())] = true;
//   dfs(0, isQueenDict);
//   delete isQueenDict["00" + (i < 10 ? "0" + i : i.toString())];
// }
// console.log(wayCnt);
