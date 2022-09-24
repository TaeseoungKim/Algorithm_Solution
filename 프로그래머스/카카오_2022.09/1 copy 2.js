// 3번 문제
function solution(users, emoticons) {
  emoticonLength = emoticons.length;

  result = [];
  let ResultArray = [];

  recursion(0, []);

  function recursion(idx, curDiscout) {
    if (emoticonLength == idx) {
      let PlusUser = 0;
      let profit = 0;

      users.forEach((element) => {
        let [discountRate, wallet] = element;
        let sumValue = 0;
        for (let i = 0; i < emoticonLength; i++) {
          if (discountRate <= curDiscout[i])
            sumValue += emoticons[i] * ((100 - curDiscout[i]) / 100);
        }
        if (sumValue >= wallet) PlusUser++;
        else profit += sumValue;
      });
      ResultArray.push([PlusUser, profit]);
    } else {
      recursion(idx + 1, [...curDiscout, 10]);
      recursion(idx + 1, [...curDiscout, 20]);
      recursion(idx + 1, [...curDiscout, 30]);
      recursion(idx + 1, [...curDiscout, 40]);
    }
  }

  // 2차원 정렬
  ResultArray.sort((a, b) => b[0] + b[1] - (a[0] + a[1]));
  ResultArray.sort((a, b) => {
    if (a[0] === b[0]) {
      return a[1] - b[1];
    } else {
      return a[0] - b[0];
    }
  });

  return ResultArray[ResultArray.length - 1];
}

// users = [
//   [40, 10000],
//   [25, 10000],
// ];
// emoticons = [7000, 9000];

console.log("ResultArray", ResultArray[ResultArray.length - 1]);
