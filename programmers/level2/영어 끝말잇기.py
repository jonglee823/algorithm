def solution(n, words):
    answer = [0, 0]

    wordDic = {words[0]}

    for i in range(1, len(words), 1):
        if words[i-1][-1] != words[i][0]:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break

        if words[i] in wordDic:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break
        else:
            wordDic.add(words[i])
    return answer

#리펙터링 소스코드
def solution(n, words):
    answer = [0, 0]

    wordDic = {words[0]}

    for i in range(1, len(words), 1):
        if words[i] in wordDic:
            return [(i % n) + 1, (i // n) + 1]
        else:
            wordDic.add(words[i])

        if words[i - 1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1]

    return answer