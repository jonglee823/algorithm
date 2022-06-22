#baekjoon_2447
#별찍기
#참고 : https://study-all-night.tistory.com/5

def draw_star(n):
    global Map

    if n == 3:
        Map[0][:3] = Map[2][:3] = ["*", "*", "*"]
        Map[1][:3] = ["*", " ", "*"]
        return

    a = n // 3
    draw_star(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]

N = int(input())

Map = [[" " for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map:
    for j in i:
        print(j, end='')
    print()