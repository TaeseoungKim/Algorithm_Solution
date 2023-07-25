const fs = require("fs");
const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "/Users/kimtaeseong/Documents/Algorithm_Solution/자바스크립트/input.txt";
const input = fs.readFileSync(filePath).toString().split("\n");
inputArr = input[0].split(" ").map((v) => parseInt(v));
calendar = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31,
};
day = {
  0: "MON",
  1: "TUE",
  2: "WED",
  3: "THU",
  4: "FRI",
  5: "SAT",
  6: "SUN",
};
dayDiff = 0;
for (let i = 1; i < inputArr[0]; i++) {
  dayDiff += calendar[i];
}

dayDiff += inputArr[1] - 1;
console.log(day[dayDiff % 7]);
