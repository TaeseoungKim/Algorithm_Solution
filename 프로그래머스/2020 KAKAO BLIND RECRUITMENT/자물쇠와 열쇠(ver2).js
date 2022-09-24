key = [
  [0, 0, 0],
  [1, 0, 0],
  [0, 1, 1],
];

lock = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 1],
];

function solution(key, lock) {
  const keyLen = key.length;
  const lockLen = lock.length;

  let board = new Array(lockLen + keyLen * 2 - 2)
    .fill()
    .map((_) => new Array(lockLen + keyLen * 2 - 2).fill());
}

function rotate(key, lock) {}
