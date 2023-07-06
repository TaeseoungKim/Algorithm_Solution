const input1 = [`/foo`, `bar`, `baz/asdf`];
const input2 = [`/foo`, `bar`, `baz/asdf`, `quux`, `..`];
const input3 = [`/foo`, `bar`, `baz/./asdf`];
const input4 = [`/foo`, `bar`, `baz`, `...`, `/asdf`];
const input5 = [`/foo`, `bar`, `...`, `.`, `ab`];

function solution(paths) {
  const resultPath = [];
  for (const path of paths) {
    const splitedPaths = path.split("/");

    for (const splitedPath of splitedPaths) {
      if (splitedPath === "") continue;

      if (splitedPath === `.`) {
        continue;
      } else if (splitedPath === `..`) {
        resultPath.pop();
      } else if (splitedPath === `...`) {
        resultPath.pop();
        resultPath.pop();
      } else resultPath.push(splitedPath);
    }
  }
  var answer = "/";
  for (let i = 0; i < resultPath.length; i++) {
    answer += resultPath[i];
    if (i !== resultPath.length - 1) answer += "/";
  }

  return answer;
}

console.log(solution(input1));
console.log(solution(input2));
console.log(solution(input3));
console.log(solution(input4));
console.log(solution(input5));
