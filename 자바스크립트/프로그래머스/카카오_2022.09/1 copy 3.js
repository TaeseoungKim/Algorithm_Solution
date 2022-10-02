// 4번 문제

let numbers = [63, 111, 95];
let perfectBinTree = [1];

let result = [];

for (let i = 1; i < 1023; i++) {
  perfectBinTree.push(2 ** i + perfectBinTree[i - 1]);

  if (i < 10) console.log("perfectBinTree:", perfectBinTree[i].toString(2));
}

for (let num of numbers) {
  console.log("--------------", num, " 시작", "--------------");
  let binNum = num.toString(2);

  let lastIdx = binNum.length - 1;
  let binNumLen = binNum.length;
  let i = 1;

  let start = binNumLen;
  //   let end = binNumLen;

  let tmpDiff = 0;

  for (let i = 1; i < 1023; i++) {
    if (perfectBinTree[i].toString(2).length > binNumLen) {
    }

    if (num > perfectBinTree[i]) continue;
  }

  let perBinNum;
  let DistDiff = 0;
  let end = 0;

  let tmpsex = 0;
  for (let i = 1; i < 1023; i++) {
    if (num > perfectBinTree[i]) continue;
    else {
      let tmpStr = "";
      for (let bb = 0; bb < perfectBinTree[i]; bb++) tmpStr += "1";

      console.log("tmpstr", tmpStr);
      tmpsex = perfectBinTree[i - 1];
      perBinNum = perfectBinTree[i].toString(2);
      end = perfectBinTree[i].toString(2).length;
      tmpDiff =
        perfectBinTree[i].toString(2).length -
        perfectBinTree[i - 1].toString(2).length;
      DistDiff = perBinNum.length - binNum.length;
      if (DistDiff != 0) binNum = "0" * DistDiff + binNum;
      break;
    }
  }

  console.log("tmpSex", tmpsex.toString(2));
  console.log("test:", binNum.slice(tmpDiff, end));

  console.log("DistDiff", DistDiff);
  console.log("perBinNum", perBinNum);
  console.log("binNum", binNum);

  let LastLen = binNum.length;
  let tmp = 0;
  let sumV = 0;

  while (true) {
    sumV += 2 ** tmp;
    tmp++;
    if (sumV >= LastLen) {
      tmp -= 1;
      sumV -= 2 ** tmp;
      break;
    }
    // tmp = 2 ** tmp;
  }

  console.log("tmp", tmp);
  console.log("제발222", binNum.slice(2 ** tmp - 1, binNum.length - 1));

  if (binNum.slice(2 ** tmp - 1, binNum.length - 1).indexOf("0") == -1) {
    console.log("넌 틀렸어!!!!");
  } else {
    console.log("넌 맞았어!!!!!!!");
  }

  //   만약에 리프노드에 0이 있다? 그럼 만들 수 없는 것이다.

  if (perBinNum == binNum) {
    console.log("같다!", num);
    result.push(1);
  } else {
    result.push(0);
  }

  console.log(num.toString(2), "\n프로그램 종료\n\n");
}

console.log("제발", result);
