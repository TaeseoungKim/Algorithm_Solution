// 미완

lines = [
  "2016-09-15 20:59:57.421 0.351s",
  "2016-09-15 20:59:58.233 1.181s",
  "2016-09-15 20:59:58.299 0.8s",
  "2016-09-15 20:59:58.688 1.041s",
  "2016-09-15 20:59:59.591 1.412s",
  "2016-09-15 21:00:00.464 1.466s",
  "2016-09-15 21:00:00.741 1.581s",
  "2016-09-15 21:00:00.748 2.31s",
  "2016-09-15 21:00:00.966 0.381s",
  "2016-09-15 21:00:02.066 2s",
];

lines = lines.map((value) => value.split(" ").slice(1, 3));
lines = lines.map((value) => {
  [second, milliSecond] = value[1].replace("s", "").split(".");
  throughput = 0;
  if (!milliSecond) throughput += Number(second) * 1000;
  else {
    switch (milliSecond.length) {
      case 1:
        throughput += Number(second) * 1000 + Number(milliSecond) * 100;
        break;
      case 2:
        throughput += Number(second) * 1000 + Number(milliSecond) * 10;
        break;
      case 3:
        throughput += Number(second) * 1000 + Number(milliSecond);
        break;
    }
  }

  endTime = 0;
  [time, milliSecond] = value[0].split(".");
  [hour, minute, second] = time.split(":");
  endTime +=
    (Number(hour) * 3600 + Number(minute) * 60 + Number(second)) * 1000;
  switch (milliSecond.length) {
    case 1:
      endTime += Number(milliSecond) * 100;
      break;
    case 2:
      endTime += Number(milliSecond) * 10;
      break;
    case 3:
      endTime += Number(milliSecond);
      break;
  }

  return [endTime - throughput, endTime];
});

console.log(lines);
