#내가 짠 소스코드.
def solution(t, p):
    answer = 0

    listT = [x for x in str(t)]

    strvalue = ''
    for i in listT:
        strvalue += i
        if len(strvalue) > len(p):
            strvalue = strvalue[1:len(p) + 1]
            #문자열을 치환해주는것은 성능상 좋지 않음..

        if len(strvalue) == len(p) and int(strvalue) <= int(p):
            answer += 1
    return answer

#인터넷 참고
# def solution(t, p):
#     answer = 0
#
#     for i in range(len(t) - len(p) + 1):
#         if int(p) >= int(t[i:i + len(p)]):
#             answer += 1
#
#     return answer