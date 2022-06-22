#baekjoon_1712
#손익분기점
#참고 : https://somjang.tistory.com/entry/BaekJoon-1712번-손익분기점-Python
#손익분기점 = 고정비용 / (가격-가변비용)

#A 고정비용 B 가변비용 C 노트북 가격
from sys import stdin, stdout

A,B,C = map(int, stdin.readline().split())
if (B >= C):
    stdout.write("-1")
else:
    print(int((A / (C - B)) + 1))