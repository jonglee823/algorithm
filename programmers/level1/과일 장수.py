#프로그래머스 LEVEL 1 과일장수

def solution(k, m, score):
    answer = 0

    score.sort(reverse=True)

    for i in range(0, len(score), m):
        if i + m > len(score):
            break
        answer += (min(score[i:i + m]) * m)

    return answer