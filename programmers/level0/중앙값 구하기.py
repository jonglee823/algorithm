#중앙값 구하기
def solution(array):
    answer = (len(array)//2)
    array.sort()
    return array[answer]

array = [1, 2, 3, 4, 5]
print(solution(array))