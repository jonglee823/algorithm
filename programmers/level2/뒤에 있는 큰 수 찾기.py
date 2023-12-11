#프로그래머스 LELVE2
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, value in enumerate(numbers):
        while stack and numbers[stack[-1]] < value:
            i = stack.pop()
            answer[i] = value
        stack.append(idx)
    return answer