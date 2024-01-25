#GBC

import sys

n, m = map(int, input().split())

regSpeed = []

realSpeed = []

for i in range(n):
    x, speed = map(int, input().split())
    for j in range(x):
        regSpeed.append(speed)

for i in range(m):
    x, speed = map(int, input().split())
    for j in range(x):
        realSpeed.append(speed)

temp = 0
for i in range(100):
    temp = max(temp, realSpeed[i] - regSpeed[i])

print(temp)

#리펙터링 소스코드
import sys

n, m = map(int, input().split())

def read_input_data(count):
    speeds = []
    for _ in range(count):
        x, speed = map(int, input().split())
        speeds.extend([speed] * x)
    return speeds

regSpeed = read_input_data(n)
realSpeed = read_input_data(m)

temp = max(real - reg for real, reg in zip(realSpeed, regSpeed))


if temp<0:
    print(0)
else:
    print(temp)