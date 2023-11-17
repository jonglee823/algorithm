#프로그래머스 LEVEL2
#H-Index

def solution(citations):
    answer = 0
    citList = [0] * (max(citations) + 1)

    for num in citations:
        citList[num] += 1

    for idx, num in enumerate(citList):
        if sum(citList[idx:]) >= idx and len(citList[:idx]) > 0:
            answer = idx
    return answer
