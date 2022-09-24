// 1번 문제

function solution(queries) {
  const ArrayInfo = {};

  class info {
    size = 0;
    curNumber = 0;
  }

  let squaredInfo = [1];
  let CurSquared = 2;
  while (true) {
    squaredInfo.push(CurSquared);
    CurSquared = CurSquared * 2;
    if (1000000000 < CurSquared) break;
  }

  let copyCount = 0;

  for (let [idx, number] of queries) {
    let Stringidx = String(idx);

    // 존재 시 로직
    if (ArrayInfo.hasOwnProperty(Stringidx)) {
      let sum = ArrayInfo[Stringidx].curNumber + number;

      if (sum > ArrayInfo[Stringidx].size) {
        for (let SquaredNumber of squaredInfo) {
          if (SquaredNumber >= sum) {
            copyCount += ArrayInfo[Stringidx].curNumber;
            ArrayInfo[Stringidx].size = SquaredNumber;
            ArrayInfo[Stringidx].curNumber = sum;
            break;
          }
        }
      } else {
        ArrayInfo[Stringidx].curNumber = sum;
      }
    }

    // 존재하지 않을 시 로직
    else {
      ArrayInfo[String(idx)] = new info();
      ArrayInfo[String(idx)].number = number;

      for (let SquaredNumber of squaredInfo) {
        if (SquaredNumber >= number) {
          ArrayInfo[String(idx)].size = SquaredNumber;
          ArrayInfo[String(idx)].curNumber = number;
          break;
        }
      }
    }
  }
  return copyCount;
}
