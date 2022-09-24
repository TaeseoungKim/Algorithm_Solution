function solution(today, terms, privacies) {
  const termsInfo = {};

  class info {
    year = 0;
    month = 0;
    day = 0;
  }

  terms.forEach((element) => {
    let [alpha, month] = element.split(" ");
    termsInfo[alpha] = month;
  });

  // 현재 날짜를 day로
  let [t_year, t_month, t_day] = today.split(".");
  today = parseInt(t_year) * 28 * 12 + parseInt(t_month) * 28 + parseInt(t_day);

  let privacies_Period = [];
  privacies.forEach((privacy) => {
    privacies_Period.push(privacyToPeriod(privacy));
  });

  result = [];

  count = 1;
  //약관 정보를 Period로 바꿔주는 함수
  for (let [startDay, endDay] of privacies_Period) {
    if (endDay <= today) result.push(count);
    count++;
  }

  function privacyToPeriod(privacy) {
    let [date, term] = privacy.split(" ");
    let [year, month, day] = date.split(".");
    startDay = parseInt(year) * 28 * 12 + parseInt(month) * 28 + parseInt(day);
    endDay = startDay + parseInt(termsInfo[term]) * 28;
    return [startDay, endDay];
  }
  return result;
}
