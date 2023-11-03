#프로그래머스 LEVEL2
def solution(s):
    intList = list(map(int, s.split()))
    answer = str(min(intList)) +' '+ str(max(intList))
    return answer