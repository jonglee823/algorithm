#프로그래머스 LEVEL2
#귤 고르기

# def solution(k, tangerine):
#     answer = 0
#     sizeDic = {}
#
#     for i in tangerine:
#         if i in sizeDic:
#             sizeDic[i] += 1
#         else:
#             sizeDic[i] = 1
#
#     valueList = sorted(sizeDic.values(), reverse=True)
#
#     for i in valueList:
#         if k > i and k > 0:
#             answer += 1
#             k -= i
#         else:
#             answer += 1
#             return answer
#
#     return answer

# #리펙터링 소스코드
# import collections
#
# def solution(k, tangerine):
#     sizeDic = collections.Counter(tangerine)
#     print(sizeDic)
#
# solution(	4, [1, 3, 2, 5, 4, 5, 2, 3])


#collections Counter 테스트
import collections
c = collections.Counter(a=3, b=1)
d = collections.Counter(a=2, b=2, c=0)
print('c : ', c)
print('d : ', d)
print('c-d : ', c-d)
print('c & d : ', c & d)   #min
print('c | d  : ', c | d ) #max
print('c == d  : ', c == d ) #c == d
print('c <= d  : ', c <= d ) #C<=d

