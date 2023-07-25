const grade = {
  "A+": 4.5,
  A0: 4.0,
  "B+": 3.5,
  B0: 3.0,
  "C+": 2.5,
  C0: 2.0,
  "D+": 1.5,
  D0: 1.0,
  F: 0.0,
};

const fs = require("fs");
const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "/Users/kimtaeseong/Documents/Algorithm_Solution/자바스크립트/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const N = input.length;

const test = input.map((v) => {
  const i = v.split(" ");
  if (i[2] !== "P") return i[1] * grade[i[2]];
  else return 0;
});

const sumV = test.reduce((sum, num) => sum + num, 0);
const sumNumber = input.reduce((sum, seq) => {
  const i = seq.split(" ");
  if (i[2] !== "P") return sum + i[1] * 1;
  else return sum;
}, 0);

console.log(sumV / sumNumber);
