// 5번 셀 문제
function solution(commands) {
  class cell {
    value = "EMPTY";
    isMerged = false;
    beforeValue = false;
  }

  class valueInfo {}
  let valueObj = new valueInfo();
  let result = [];

  let board = new Array(51)
    .fill()
    .map((_) => new Array(51).fill().map((_) => new cell()));

  commands.forEach((command) => {
    let kindOfCom = command.split(" ")[0];
    if (kindOfCom == "UPDATE") {
      let op = command.split(" ");
      // r,c의 값을 value로 없데이트
      if (op.length == 4) {
        board[parseInt(op[1])][parseInt(op[2])].value = op[3];
        board[parseInt(op[1])][parseInt(op[2])].isMerged = false;
        board[parseInt(op[1])][parseInt(op[2])].beforeValue = false;
        if (valueObj.hasOwnProperty(op[3]))
          valueObj[op[3]].push([parseInt(op[1]), parseInt(op[2])]);
        else {
          valueObj[op[3]] = [];
          valueObj[op[3]].push([parseInt(op[1]), parseInt(op[2])]);
        }
      }
      // value1의 값을 가지고 있는 모든 셀을 value2로 업데이트
      else if (op.length == 3) {
        if (valueObj.hasOwnProperty(op[1])) {
          valueObj[op[1]].forEach((ele) => {
            let [r, c] = ele;
            board[r][c].value = op[2];
            board[r][c].isMerged = false;
            board[r][c].beforeValue = false;
          });

          delete valueObj[op[1]];
        }
      }
    } else if (kindOfCom == "MERGE") {
      let op = command.split(" ");

      if (
        board[parseInt(op[1])][parseInt(op[2])] == "EMPTY" &&
        board[parseInt(op[3])][parseInt(op[4])] == "EMPTY"
      ) {
        let Paaas = 0;
      } else if (
        board[parseInt(op[1])][parseInt(op[2])] != "EMPTY" &&
        board[parseInt(op[3])][parseInt(op[4])] != "EMPTY"
      ) {
        board[parseInt(op[3])][parseInt(op[4])].value =
          board[parseInt(op[1])][parseInt(op[2])].value;
        board[parseInt(op[3])][parseInt(op[4])].isMerged = true;
        board[parseInt(op[3])][parseInt(op[4])].beforeValue =
          board[parseInt(op[3])][parseInt(op[4])].value;

        if (valueObj.hasOwnProperty(board[parseInt(op[3])][parseInt(op[4])])) {
          for (
            let i = 0;
            i < valueObj[board[parseInt(op[3])][parseInt(op[4])]].length;
            i++
          ) {
            valueObj[board[parseInt(op[3])][parseInt(op[4])]] = [
              ...valueObj[board[parseInt(op[3])][parseInt(op[4])]].slice(0, i),
              valueObj[board[parseInt(op[3])][parseInt(op[4])]].slice(i + 1),
            ];
          }

          valueObj[board[parseInt(op[1])][parseInt(op[2])]].push([
            parseInt(op[3]),
            parseInt(op[4]),
          ]);
        }

        valueObj[board[parseInt(op[1])][parseInt(op[2])].value].forEach(
          (ele) => {
            let [r, c] = ele;

            board[r][c].value = op[2];
            board[r][c].isMerged = false;
            board[r][c].beforeValue = false;
          }
        );
      } else if (
        board[parseInt(op[1])][parseInt(op[2])] == "EMPTY" &&
        board[parseInt(op[3])][parseInt(op[4])] != "EMPTY"
      ) {
        board[parseInt(op[1])][parseInt(op[2])].value =
          board[parseInt(op[3])][parseInt(op[4])].value;
        board[parseInt(op[1])][parseInt(op[2])].isMerged = true;
        board[parseInt(op[1])][parseInt(op[2])].beforeValue = "EMPTY";
      } else if (
        board[parseInt(op[1])][parseInt(op[2])] != "EMPTY" &&
        board[parseInt(op[3])][parseInt(op[4])] == "EMPTY"
      ) {
        board[parseInt(op[3])][parseInt(op[4])].value =
          board[parseInt(op[1])][parseInt(op[2])].value;
        board[parseInt(op[3])][parseInt(op[4])].isMerged = true;
        board[parseInt(op[3])][parseInt(op[4])].beforeValue = "EMPTY";
      }
    } else if (kindOfCom == "UNMERGE") {
      let op = command.split(" ");

      board[parseInt(op[1])][parseInt(op[2])].value =
        board[parseInt(op[1])][parseInt(op[2])].beforeValue;
      board[parseInt(op[1])][parseInt(op[2])].isMerged = false;
      board[parseInt(op[1])][parseInt(op[2])].beforeValue = false;
    } else if (kindOfCom == "PRINT") {
      let op = command.split(" ");
      result.push(board[parseInt(op[1])][parseInt(op[2])].value);
    }
  });
  return result;
}
