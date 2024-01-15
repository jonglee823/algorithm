#baekjoon_1654
#랜선자르기
k, n = map(int, input().split())
lanList = [int(input()) for _ in range(k)]

start = 1
end = max(lanList)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in lanList:
        total += (x // mid)

    if total >= n:
        start = mid + 1
    else:
        end = mid -1
print(end)

