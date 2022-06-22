#baekjoon_1065
#어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면,
# 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고,
# N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

def find_hansu():
    N = int(input())
    if(N < 100):
        return N
    else:
        count = 99
        drawDiffNum = 0
        for num in range(100, N+1):
            strNumList = str(num)
            strLen = len(strNumList)
            drawDiffNum = int(strNumList[strLen-1]) - int(strNumList[strLen - 2])
            for x in reversed(range(strLen - 1)):
                if(x != 0):
                    if(drawDiffNum != (int(strNumList[x]) - int(strNumList[x - 1]))):
                        break
                else:
                    count+=1
    return count

if __name__ =="__main__":
    print(find_hansu())
