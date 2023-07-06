/* repository가 undefined인 경우 */
const object1 = {
  repository: undefined,
};

/* repository의 readme가 undefined인 경우 */
const object2 = {
  repository: {
    readme: undefined,
  },
};

/** repository.readme 모두가 존재하는 경우 */
const object3 = {
  repository: {
    readme: {
      extension: "md",
      content: "금융을 쉽고 간편하게",
    },
  },
};

const safelyGet = (object, opcode) => {
  const op = opcode.split(".");
  let tempObj = object;
  for (let i = 0; i < op.length; i++) {
    const key = op[i];
    if (tempObj === undefined) {
      console.log("반환 값: ", undefined);
      return undefined;
    }
    tempObj = tempObj[key];
  }

  console.log("반환 값: ", tempObj);
  return tempObj;
};
