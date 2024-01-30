#Softeer Level2
#비밀메뉴
import sys


M, N, K = map(int, input().split())
secrit = ''.join(input().split())
user = ''.join(input().split())


if secrit in user:
    print('secret')
else:
    print('normal')


##다시 짠 코드
import sys

m, n, k = map(int, input().split())

secretList = input()
selectList = input()

if secretList in selectList:
    print('secret')
else :
    print('normal')