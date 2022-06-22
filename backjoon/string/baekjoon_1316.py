#baekjoon 1316
#참고..https://fre2-dom.tistory.com/297

testCase = int(input())
count = testCase
testArr = [list(input()) for _ in range(testCase)]

for word in testArr:
    if(len(word) == 1 ):
        pass
    else:
        for index in range(len(word)-1):
            if(word[index] == word[index+1]):
                pass
            elif(word[index] in word[index+1:]):
                count-=1
                break
print(count)
