#baekjoon_10872
#팩토리얼

def func(num):
    if num==1 or num==0:
        return 1
    else:
        return num*(func(num-1))

print(func(int(input())))