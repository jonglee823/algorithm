#프로그래머스 LEVEL2
#JadenCase 문자열 만들기


#splite할 경우 공백을 원상태로 복구할 수 없음..
def solution(s):
    answer = ''

    for string in s.split():
        if string[0].isalpha():
            answer += string[0].upper() + string[1:].lower()
        else:
            answer += string.lower()
        answer += " "
    return answer[0:len(answer) - 1]

#find할 경우에 같은 알파벳이 나올경우 list의 어떤위치인지 탐색 불가. Ex) "aaaa aaa"
def solution(s):
    answer = [" "] * len(s)

    for string in s.split():
        # print('string : ', string)
        changeString = ''
        if string[0].isalpha():
            changeString += string[0].upper() + string[1:].lower()
        else:
            changeString += string.lower()

        answer[s.find(string):s.find(string) + len(changeString)] = changeString

    return ''.join(answer)


from collections import deque

#최종 답안코드
def solution(s):
    answer = ''
    queue = deque(s)

    while queue:
        value = queue.popleft()
        if value.isalnum():
            while queue and queue[0] != " ":
                value += queue.popleft()
            answer += value[0].upper() + value[1:].lower()
        else:
            answer += value

    return answer