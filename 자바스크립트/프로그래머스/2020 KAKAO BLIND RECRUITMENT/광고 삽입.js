// 시간을 초 단위(nunmber)로 바꿔주는 함수
function timeToseconds(time) {
  time = time.split(":");
  return 3600 * parseInt(time[0]) + 60 * parseInt(time[1]) + parseInt(time[2]);
}
// 초를 시간(string)으로 바꿔주는 함수
function secondsToTime(seconds) {
  let hour = parseInt(seconds / 3600);
  let minute = parseInt((seconds % 3600) / 60);
  let second = seconds % 60;

  hour = hour < 10 ? "0" + hour : hour;
  minute = minute < 10 ? "0" + minute : minute;
  second = second < 10 ? "0" + second : second;

  return hour + ":" + minute + ":" + second;
}

function solution(play_time, adv_time, logs) {
  // logs를 초 단위 구간으로 변환
  const intervalLogs = logs.map((value) => {
    let interval = value.split("-");
    interval = interval.map((value) => {
      return timeToseconds(value);
    });
    return interval;
  });

  // play_time,adv_time을 초 단위 구간으로 변환
  play_time = timeToseconds(play_time);
  adv_time = timeToseconds(adv_time);

  // play_time+1 크기의 배열, dp 배열 선언
  let arr = new Array(play_time + 1).fill(0, 0, play_time + 1);
  let dp = new Array(play_time + 1).fill(0, 0, play_time + 1);

  // arr 배열에 겹치는 구간 만큼 더해준다.
  intervalLogs.map((value) => {
    for (i = value[0]; i <= value[1]; i++) {
      arr[i] += 1;
    }
  });

  // (index~index+adv_time)의 합을 모두 더해준다.
  dp.map((value, index) => {
    if (index == 0) {
      dp[index] = arr.slice(0, adv_time).reduce(function add(sum, currValue) {
        return sum + currValue;
      });
    } else if (index + adv_time > play_time) {
      dp[index] = arr
        .slice(index, play_time + 1)
        .reduce(function add(sum, currValue) {
          return sum + currValue;
        });
    } else {
      dp[index] = dp[index - 1] - arr[index - 1] + arr[index + adv_time];
    }
  });

  // 앞서 구한 값 중, 가장 큰 합의 값을 구하고 출력
  const resultIndex = dp.indexOf(Math.max(...dp));
  return secondsToTime(resultIndex);
}
