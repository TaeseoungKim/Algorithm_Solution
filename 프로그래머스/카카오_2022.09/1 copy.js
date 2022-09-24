cap = 4;
n = 5;
deliveries = [1, 0, 3, 1, 2];
pickups = [0, 3, 0, 4, 0];

solution(cap, n, deliveries, pickups);

function solution(cap, n, deliveries, pickups) {
  result = 0;

  while (!(deliveries.length == 0 && deliveries.length == 0)) {
    let del_endIdx = deliveries.length - 1;
    let pick_endIdx = pickups.length - 1;
    let curCap = cap;

    let delDist = 0;
    let pickDist = 0;

    if (deliveries) {
      while (deliveries[del_endIdx] == 0) {
        del_endIdx -= 1;

        deliveries.pop();
      }
    }
    if (pickups) {
      while (pickups[pick_endIdx] == 0) {
        pick_endIdx -= 1;
        pickups.pop();
      }
    }

    for (let i = del_endIdx; 0 <= i; i--) {
      if (!delDist) delDist = i + 1;
      if (curCap >= deliveries[i]) {
        curCap -= deliveries[i];
        deliveries[i] = 0; // pop 고려
      } else {
        deliveries[i] -= curCap;
        curCap = 0;
      }

      if (curCap == 0) break;
    }

    if (pick_endIdx > del_endIdx) pickDist += pick_endIdx - del_endIdx;
    curCap = cap;

    let oneTime = false;
    for (let i = pick_endIdx; 0 <= i; i--) {
      if (pick_endIdx <= del_endIdx && !oneTime) {
        oneTime = true;
        pickDist += delDist;
      }
      if (curCap >= pickups[i]) {
        curCap -= pickups[i];
        pickups[i] = 0; // pop 고려
      } else {
        curCap = 0;
        pickups[i] -= curCap;
      }

      if (curCap == 0) break;
    }

    result += delDist + pickDist;
  }

  return result;
}
