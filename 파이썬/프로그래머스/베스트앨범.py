genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def solution(genres, plays):
    N = len(genres)
    bestAlbum = [[genres[i], plays[i], i] for i in range(N)]
    bestAlbum.sort(key=lambda x: (-x[1], x[2]))

    print(bestAlbum)
    genreSum = {}
    for i in range(N):
        if genres[i] in genreSum:
            genreSum[genres[i]] += plays[i]
        else:
            genreSum[genres[i]] = plays[i]

    genrePriority = sorted(genreSum.items(), key=lambda x: -x[1])

    Answer = []
    print("genrePriority", genrePriority)
    for i in range(len(genrePriority)):
        Cnt = 0
        for d in range(N):
            genre, play, idx = bestAlbum[d]
            if Cnt >= 2:
                break
            elif genre != genrePriority[i][0]:
                continue
            else:
                Answer.append(idx)
                Cnt += 1

    return Answer
