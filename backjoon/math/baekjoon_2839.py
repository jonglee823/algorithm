#baekjoon_2839
#설탕배달

weight = int(input())

array = [3, 5]
d = [5001] * (weight + 1)

d[0] = 0
for i in range(2):
    for j in range(array[i], weight+1):
        if d[j-array[i]] != 5001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[weight] == 5001:
    print(-1)
else:
    print(d[weight])