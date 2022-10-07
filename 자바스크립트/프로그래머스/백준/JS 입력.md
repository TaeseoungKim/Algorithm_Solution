const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let n = fs.readFileSync(filePath).toString().split("\n");
