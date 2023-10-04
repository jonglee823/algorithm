#2023.10.04
def solution(food):
    answer = ''

    for i in range(1, len(food)):
        count = food[i] // 2
        strFood = str(i) * count
        answer += strFood

    revAns = answer[::-1]
    answer += str(0)
    answer += revAns

    return answer