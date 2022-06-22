#baekjoon_10870
#피보나치 수 5

def func(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return func(num-1) + func(num-2)

print(func(int(input())))