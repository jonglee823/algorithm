#오븐시계
h, m = map(int, input().split())
time = int(input())

if(m+time >= 60):
    h += (m+time)/60
    if(h >= 24):
        h -= 24
    print(int(h), (m+time)%60)
else:
    print(h, m+time)