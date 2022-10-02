const { strict } = require("assert");

function MatchingScore(
  url,
  index,
  normalScore = 0,
  linkToMe = [],
  linkToOther = []
) {
  this.url = url;
  this.index = index;
  this.normalScore = normalScore;
  this.linkToMe = linkToMe;
  this.linkToOther = linkToOther;
}

function FindLink(bodyScript, NewMatchingScore) {
  links = bodyScript.split('<a href="');
  if (links.length == 1) {
    return 0;
  } else {
    for (let i = 1; i < links.length; i++) {
      links.forEach((value, index) => {
        NewMatchingScore.linkToOther.push(value.split("</a>")[0]);
      });
    }
  }
}

word = "Muzi";
LowerWord = word.toLowerCase();
pages = [
  '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://careers.kakao.com/interview/list"/>\n</head>  \n<body>\n<a href="https://programmers.co.kr/learn/courses/4673"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>',
  '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://www.kakaocorp.com"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href="https://hashcode.co.kr/tos"></a>\n\n\t^\n</body>\n</html>',
];
MS_Objs = [];

pages.forEach((value, index) => {
  //   console.log("valueType:", typeof value);
  //   console.log("\n\n\n\n\nvalue!!!!", value);

  url = bodyScript.split('content="')[1].split("/>")[0];
  bodyScript = value.split("<body>")[1].split("</body>")[0];
  console.log(index, "bodyScript:", bodyScript);
  LowerbodyScript = bodyScript.toLowerCase();
  Spited_LowerbodyScript = LowerbodyScript.split(LowerWord);

  // LowerbodyScript.
  //   hiasdsad1@#hiasdasdhi!@#@!#hi@#hi!@#$%hi!@#!@#hi

  //   helloworld.split("hi").forEach((value,index)=>{

  //   })

  //   asdasdhiasdsad1@#hiasdasdhi!@#@!#hi@#hi!@#$%hi!@#!@#hi

  //   hiasdsad1@#hiasdasdhi!@#@!#hi@#hi!@#$%hi!@#!@#hi

  NewMatchingScore = new MatchingScore(url, index);
  FindLink(bodyScript, NewMatchingScore);
  // 0이면 검색어가 포함되지 않음
  if (Spited_LowerbodyScript.length == 0) {
  } else {
  }

  // 다 소문자로 바꾸고 ..
});
