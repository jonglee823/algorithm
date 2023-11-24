#python3 test

testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(True  in (value > 9 for value in testList))
### ==> True

print(True  in (value > 11 for value in testList))
### ==> False
print(any())