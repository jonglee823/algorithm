#BAEKJOON
#N과 M(2)


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
rs = []

def rcuv(start):
    if len(rs) == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(start, N+1):
            rs.append(i)
            rcuv(i+1)
            rs.pop()


rcuv(1)






