#BAEJOON 1157
#다른분 풀이 참고 출처 : haseungho
# start
# word = input().upper()
# word_list = list(set(word))
# 
# cnt = []
# for i in word_list:
#   cnt.append(word.count(i))
#
# if cnt.count(max(cnt)) > 1:
#   print("?")
#
# else:
#   print(word_list[(cnt.index(max(cnt)))])

# end

alphArry = {chr(y) : 0 for y in range(65, 91)}
inputString = (str(input())).upper()
listString = list(inputString)
for index in range(0, len(listString)):
    alphArry[listString[index]] +=1
maxAlph = [k for k,v in alphArry.items() if max(alphArry.values()) ==v]
if(len(maxAlph) >= 2):
    print("?")
else:
    print(maxAlph[0])
