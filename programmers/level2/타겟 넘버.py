#프로그래머스 LELVEL2
#타켓 넘버

#BFS
def solution(numbers, target):
    answer = 0
    leaves = [0]

    for i in range(len(numbers)):
        temp = []

        for leav in leaves:
            temp.append(leav + numbers[i])
            temp.append(leav - numbers[i])

        leaves = temp

    for num in leaves:
        if num == target:
            answer += 1

    return answer


#DFS
answer = 0

def dfs(numbers, target, idx, values):
    global answer

    if idx == len(numbers) and values == target:
        answer += 1
        return

    elif idx == len(numbers):
        return

    dfs(numbers, target, idx + 1, values + numbers[idx])
    dfs(numbers, target, idx + 1, values - numbers[idx])


def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)

    return answer