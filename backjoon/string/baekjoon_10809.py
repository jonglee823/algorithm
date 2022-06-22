#Baekjoon_10809
#알파벳 위치 찾기

apList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
          'q','r','s','t','u','v','w','x','y','z']

apaIndex =[-1 for _ in range(26)]

strWord = input()
for apa in strWord:
    if(apaIndex[apList.index(apa)] == -1):
        apaIndex[apList.index(apa)] = strWord.index(apa)

for x in range(len(apaIndex)):
    print(apaIndex[x], end=' ')


#출처는 모르지만 인터넷에서 발견한 코드
# string = input()
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in alphabet:
#     print(string.find(i), end = ' ')