import re


def timeTominute(time, isZero):
    hour, minute = map(int, time.split(":"))

    if not isZero:
        return hour*60+minute
    else:
        return 24*60+minute


def encode(melody):
    result = ""
    resultIdx = -1

    for i in range(len(melody)):
        if melody[i] == "#":
            result = result[:resultIdx] + \
                result[resultIdx].lower()
        else:
            result += melody[i]
            resultIdx += 1
    return result


def solution(m, musicinfos):

    encoM = encode(m)
    p = re.compile(encoM)
    answer = []

    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(",")
        start = timeTominute(start, False)
        end = timeTominute(end, False)
        if start > end:
            end = timeTominute(end, True)
        playTime = end - start
        playMelody = ""
        melody = encode(melody)
        if len(melody) >= playTime:
            playMelody = melody[:playTime]
        else:
            for i in range(playTime//len(melody)):
                playMelody += melody
            playMelody += melody[:playTime % len(melody)]

        if len(p.findall(playMelody)) != 0:
            answer.append((playTime, title))
    answer.sort(key=lambda x: x[0])
    if len(answer) == 0:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][1]
    else:
        return answer[0][1]


m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))
