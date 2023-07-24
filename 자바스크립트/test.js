aa = [30, 20];

test(aa, 0);
function test(tt, count) {
  let [bb, cc] = aa;
  if (count == 5) return;
  else test([bb, cc + 10], count + 1);

  if (count == 0) {
    console.log(aa);
    console.log(bb, cc);
  }
}
