const fs = require("fs");
const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "/Users/kimtaeseong/Documents/Algorithm_Solution/자바스크립트/프로그래머스/백준/input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
let n = Number(input[0]);
let numbers = input[1].split(" ").map((v) => Number(v));
let op = input[2].split(" ").map((v) => Number(v));

let minNum = 10 ** 10;
let maxNum = -(10 ** 10);
let [plus, minus, mul, div] = op;

recursion(numbers[0], 0, [...op]);
console.log(maxNum);
console.log(minNum);

function recursion(number, idx) {
  if (idx == n - 1) {
    maxNum = Math.max(maxNum, number);
    minNum = Math.min(minNum, number);
  } else {
    if (plus > 0) {
      plus -= 1;
      recursion(number + numbers[idx + 1], idx + 1, [plus, minus, mul, div]);
      plus += 1;
    }
    if (minus > 0) {
      minus -= 1;
      recursion(number - numbers[idx + 1], idx + 1, [plus, minus, mul, div]);
      minus += 1;
    }
    if (mul > 0) {
      mul -= 1;
      recursion(number * numbers[idx + 1], idx + 1, [plus, minus, mul, div]);
      mul += 1;
    }
    if (div > 0) {
      div -= 1;
      let newNum =
        number < 0
          ? -parseInt(Math.abs(number) / numbers[idx + 1])
          : parseInt(number / numbers[idx + 1]);
      recursion(newNum, idx + 1, [plus, minus, mul, div]);
      div += 1;
    }
  }
}
