#2023-10-16
#프로그래머스 LEVEL1
#명예의 전당

def solution(k, score):
    rank = []
    answer = []

    for s in score:
        rank.append(s)
        if (len(rank) > k):
            rank.remove(min(rank))
        answer.append(min(rank))
    return answer