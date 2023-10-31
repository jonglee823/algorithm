#프로그래머스 폰켄몬
def solution(nums):
    answer = 0
    count = int(len(nums) / 2)

    if len(set(nums)) > count:
        answer = count
    else:
        answer = len(set(nums))

    return answer