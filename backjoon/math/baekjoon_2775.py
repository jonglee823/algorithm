#baekjoon_2775
#부녀회장이 될테야

arr = [list(x for x in range(1, 15))]
for x in range(0, 15):
    arr2 = []
    for i in range(1, len(arr[x])+1):
        arr2.append(sum(arr[x][:i]))
    arr.append(arr2)

testCase = int(input())
for _ in range(testCase):
    floor = int(input())
    num = int(input())
    print(arr[floor][num-1])
