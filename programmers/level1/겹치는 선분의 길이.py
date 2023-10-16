def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                print('i : ', i , '(n // i) :', (n // i))
                divisorsList.append(n // i)

    return divisorsList


print(getMyDivisor(100))