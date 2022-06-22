#baekjoon_4948
#베르트랑 공준

while True:
    M = int(input())

    if M ==0:
        break
    N = M * 2
    numList = [True] * (N+1)

    for i in range(2,int((N+1)**0.5)+1):
        if numList[i]:
            for j in range(i+i,N+1,i):
                numList[j]=False

    answer = [i for i in range(2,N+1) if (numList[i] and i >M)]
    print(len(answer))
