function solution(key, lock) {
  // 배열을 회전하는 함수
  const rotateRight = (arr) => {
    const len = arr.length;
    const tmp = Array(len)
      .fill()
      .map((_) => Array(len).fill());
    for (let i = 0; i < len; i++) {
      for (let j = 0; j < len; j++) {
        tmp[j][len - 1 - i] = key[i][j];
      }
    }
    return tmp;
  };

  // 락 배열을 확장한 board 배열 생성
  const [keyLen, lockLen] = [key.length, lock.length];
  const totalLen = lockLen + keyLen * 2 - 2;
  // board 배열 생성
  const board = Array(totalLen)
    .fill()
    .map((_) => Array(totalLen).fill());

  // board 정중앙에 락 배열 값 삽입
  for (let i = keyLen - 1; i < keyLen + lockLen - 1; i++) {
    for (let j = keyLen - 1; j < keyLen + lockLen - 1; j++) {
      board[i][j] = lock[i - (keyLen - 1)][j - (keyLen - 1)];
    }
  }

  //   자물쇠가 열리는지 판단 여부를 파악하는 함수 작성
  const isValid = (arr) => {
    // board 배열에서 실제 락 배열의 값이 포함된 부분만 검사한다.
    for (let i = keyLen - 1; i < keyLen + lockLen - 1; i++) {
      for (let j = keyLen - 1; j < keyLen + lockLen - 1; j++) {
        if (arr[i][j] !== 1) return false;
      }
    }
    return true;
  };

  //키를 돌려가면서 모든 경우의 수를 탐색
  for (let rotate = 0; rotate < 4; rotate++) {
    // 작업 수행 최소화 위해 처음에는 로테이션 안 함
    key = rotate === 0 ? key : rotateRight(key);

    for (let i = 0; i <= totalLen - keyLen; i++) {
      for (let j = 0; j <= totalLen - keyLen; j++) {
        // 전개 연산자를 통해 board 원본 값에 영향주지 않도록 카피
        const boardCopy = board.map((arr) => [...arr]);
        for (let r = 0; r < keyLen; r++) {
          for (let c = 0; c < keyLen; c++) {
            // 열쇠의 홈과 자물쇠의 홈이 만나면 안 되기 때문에 홈끼리 만나는 경우 값 2로 수정
            if (key[r][c] === 1 && boardCopy[i + r][j + c] === 1)
              boardCopy[i + r][j + c] = 2;
            else if (key[r][c] === 1 && boardCopy[i + r][j + c] === 0)
              boardCopy[i + r][j + c] = 1;
          }
        }
        if (isValid(boardCopy) === true) return true;
      }
    }
  }

  return false;
}
