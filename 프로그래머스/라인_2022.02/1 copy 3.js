function solution(n, m, fires, ices) {
  let firesInfo = [];
  let icesInfo = [];
  let firesLen = fires.length;
  let icesLen = ices.length;

  let resultBoard = new Array(n).fill().map((_) => new Array(n).fill(0));

  fires.forEach((value) => {
    let [x, y] = value;
    let newBoard = new Array(n).fill().map((_) => new Array(n).fill(0));
    newBoard[x - 1][y - 1] = 1;

    firesInfo.push([[x - 1, y - 1], 0, newBoard]);
  });

  ices.forEach((value) => {
    let [x, y] = value;
    let newBoard = new Array(n).fill().map((_) => new Array(n).fill(0));
    newBoard[x - 1][y - 1] = -1;

    icesInfo.push([[x - 1, y - 1], 0, newBoard]);
  });

  let count = 0;
  for (let i = 1; i <= m; i++) {
    for (let d = 0; d < firesLen; d++) {
      let [pos, size, fireBoard] = firesInfo[d];
      firesInfo[d] = expandFire(pos, size, fireBoard);
      for (let a = 0; a < n; a++)
        for (let b = 0; b < n; b++) {
          resultBoard[a][b] += fireBoard[a][b];
        }
    }

    for (let d = 0; d < icesLen; d++) {
      let [pos, size, iceBoard] = icesInfo[d];
      icesInfo[d] = expandIce(pos, size, iceBoard);

      for (let a = 0; a < n; a++)
        for (let b = 0; b < n; b++) {
          resultBoard[a][b] += iceBoard[a][b];
        }
    }
  }

  function expandFire(pos, size, fireBoard) {
    let [x, y] = pos;
    size++;

    let curX = x - size;
    while (curX <= x + size) {
      if (0 <= y + size && y + size < n && 0 <= curX && curX < n)
        fireBoard[curX][y + size] = 1;
      curX++;
    }
    curX = x - size;
    while (curX <= x + size) {
      if (0 <= y - size && y - size < n && 0 <= curX && curX < n)
        fireBoard[curX][y - size] = 1;

      curX++;
    }
    let curY = y - size;
    while (curY <= y + size) {
      if (0 <= x + size && x + size < n && 0 <= curY && curY < n)
        fireBoard[x + size][curY] = 1;

      curY++;
    }
    curY = y - size;
    while (curY <= y + size) {
      if (0 <= x - size && x - size < n && 0 <= curY && curY < n)
        fireBoard[x - size][curY] = 1;

      curY++;
    }
    return [pos, size, fireBoard];
  }

  function expandIce(pos, size, iceBoard) {
    let [x, y] = pos;
    size++;

    for (let m of [
      [x + size, y],
      [x, y + size],
      [x - size, y],
      [x, y - size],
    ]) {
      let [ix, iy] = m;
      if (0 <= iy && iy < n && 0 <= ix && ix < n) {
        iceBoard[ix][iy] = -1;
      }
    }

    let [curX, curY] = [x + size, y];
    while (true) {
      curX--;
      curY--;
      if (x == curX && y - size == curY) break;
      if (0 <= curY && curY < n && 0 <= curX && curX < n)
        iceBoard[curX][curY] = -1;
      else continue;
    }
    [curX, curY] = [x, y - size];
    while (true) {
      curX--;
      curY++;
      if (x - size == curX && y == curY) break;
      if (0 <= curY && curY < n && 0 <= curX && curX < n)
        iceBoard[curX][curY] = -1;
      else continue;
    }
    [curX, curY] = [x - size, y];
    while (true) {
      curX++;
      curY++;
      if (x == curX && y + size == curY) break;
      if (0 <= curY && curY < n && 0 <= curX && curX < n)
        iceBoard[curX][curY] = -1;
      else continue;
    }
    [curX, curY] = [x, y + size];
    while (true) {
      curX++;
      curY--;
      if (x + size == curX && y == curY) break;
      if (0 <= curY && curY < n && 0 <= curX && curX < n)
        iceBoard[curX][curY] = -1;
      else continue;
    }
    return [pos, size, iceBoard];
  }

  return resultBoard;
}
