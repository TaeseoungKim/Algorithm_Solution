// 5
// 3 2
// 1 4
// 4 1
// 2 3
// 5 5

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

Set.prototype.intersection = function (set) {
  return new Set([...this].filter((v) => set.has(v)));
};

class Person {
  constructor(myIndex, firstGrade, secondGrade) {
    this.myIndex = myIndex;
    this.firstGrade = firstGrade;
    this.secondGrade = secondGrade;
    this.firstGradeUppers = new Set();
    this.secondGradeUppers = new Set();
  }

  setUpperPeople() {}

  setLowerPeople() {}
}

const testCase = Number(input[0]);
let lineNumber = 0;

for (let i = 0; i < testCase; i++) {
  lineNumber += 1;
  let N = Number(input[lineNumber]);

  let peopleArr = [];
  for (let d = 1; d <= N; d++) {
    const [firstGrade, secondGrade] = input[lineNumber + d].split(" ");
    peopleArr.push(new Person(d, Number(firstGrade), Number(secondGrade)));
  }
  let sortedArrByFirst = [
    ...peopleArr.sort((A, B) => {
      return A.firstGrade - B.firstGrade;
    }),
  ];

  let sortedArrBySecond = [
    ...peopleArr.sort((A, B) => {
      return A.secondGrade - B.secondGrade;
    }),
  ];

  let rank = Array.from(Array(N + 1), () => [new Set(), new Set()]);

  for (let i = 0; i < N; i++) {
    for (let d = 0; d < sortedArrByFirst[i].firstGrade; d++) {
      rank[sortedArrByFirst[i].myIndex][0].add(sortedArrByFirst[d].myIndex);
    }
  }

  for (let i = 0; i < N; i++) {
    for (let d = 0; d < sortedArrBySecond[i].secondGrade; d++) {
      rank[sortedArrBySecond[i].myIndex][1].add(sortedArrBySecond[d].myIndex);
    }
  }
  for (let i = 0; i < N; i++) {
    console.log(rank[i]);
    console.log(rank[i][0].intersection(rank[i][1]));
  }

  console.log();
  console.log();
  lineNumber += N;
}
