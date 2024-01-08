def binarySearch(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        elif array[mid] < target:
            start = mid +1
    return None

N = int(input())
nList = list(map(int, input().split()))
nList.sort()

M = int(input())
mList = list(map(int, input().split()))

for i in mList:
    result = binarySearch(nList, 0, N-1, i)
    if result == None:
        print(0)
    else:
        print(1)

