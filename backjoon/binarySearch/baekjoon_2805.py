#baekjoon_2805
#나무 자르기

n, m = map(int, input().split())
nList = list(map(int, input().split()))

start = 0
end = max(nList)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for tree in nList:
        if tree >= mid:
            total += (tree - mid)

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)


