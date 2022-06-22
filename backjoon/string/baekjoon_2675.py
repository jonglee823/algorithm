#Baekjoon_2675

testCase = int(input())
arr = [list(map(str, input().split())) for _ in range(testCase)]

for index in range(len(arr)):
    for str in list(arr[index][1]):
        print(str * int(arr[index][0]), end='')
    print()