def solution(s):
    answer = []
    #dict를 통해 각 글자별로 위치 기억하기.

    dic ={}
    for idx, i in enumerate (s):
        if i not in dic:
            dic[i]=idx+1
            answer.append(-1)
        else:
            answer.append(idx-dic[i]+1)
            dic[i]=idx+1
    return answer