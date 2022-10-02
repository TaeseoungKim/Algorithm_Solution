function solution(p) {
  let [u, v] = separate(p);
  let result = [];

  while (true) {
    if (u.length == 0) {
      break;
    } else if (isCorrect(u)) {
      result.push(u);
      [u, v] = separate(v);
    } else {
      let open = 0;
      let close = 0;
      let length = 0;
      for (let c of u) {
        if (c === "(") {
          result.push(")");
          open++;
          length++;
        } else if (c === ")") {
          result.push("(");
          close++;
          length++;
        }

        if (open === close) {
          u = u.slice(length) + v;
          v = "";
        }
      }
    }
  }
  return result.join("");
}

function separate(p) {
  let length = 0;
  let open = 0;
  let close = 0;

  for (let c of p) {
    length++;
    if (c === "(") {
      open++;
    } else if (c === ")") {
      close++;
    }
    if (open == close) {
      return [p.slice(0, length), p.slice(length)];
    }
  }
  return ["", ""];
}

function isCorrect(p) {
  let open = 0;
  let close = 0;
  if (p.length == 0) return true;

  for (let c of p) {
    if (c === "(") {
      open++;
    } else if (c === ")") {
      close++;
    }

    if (open == close) {
      open--;
      close--;
    } else if (close > open) {
      return false;
    }
  }

  return true;
}
