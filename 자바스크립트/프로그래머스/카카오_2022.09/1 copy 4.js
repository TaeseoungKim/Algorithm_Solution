let result = [];
numbers.forEach((number) => {
  numberToBin = number.toString(2);
  numberToBinLength = numberToBin.length;

  let perfectBinTree = [1];

  for (let i = 1; i < 1023; i++) {
    perfectBinTree.push(2 ** i + perfectBinTree[i - 1]);
  }

  let tmpRe = 0;
  let tmpDiff = 0;
  let isPos = false;
  for (let i = 0; i < 1023; i++) {
    if (perfectBinTree[i] > numberToBinLength) {
      tmpRe = perfectBinTree[i];
      tmpDiff = perfectBinTree[i] - perfectBinTree[i - 1];
      break;
    }
  }

  for (let i = 0; i < tmpRe - numberToBinLength; i++) {
    numberToBin = "0" + numberToBin;
  }

  if (numberToBin.slice(tmpDiff).indexOf("0") == -1) {
    result.push(1);
  } else {
    result.push(0);
  }
});

return result;
