#프로그래머스 둘만의 암호
#2023-10-13
#내가 짠 소스코드

def solution(s, skip, index):
    answer = ''

    alphaList = [i for i in range(97, 123)]

    for i in skip:
        alphaList.remove(ord(i))

    for x in s:
        idx = alphaList.index(ord(x)) + index
        if idx >= len(alphaList):
            idx %= len(alphaList)
        answer += chr(alphaList[idx])
    return answer

#다른 사람 소스코드 참고한 리펙터링 소스코드

def solution(s, skip, index):
    answer = ''

    alphaList = [i for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]

    for x in s:
        answer += chr(alphaList[(alphaList.index(ord(x)) + index) % len(alphaList)])
    return answer