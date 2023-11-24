#프로그래머스 LEVEL2
import math
from collections import Counter
def jakad(word):
    jakadList = []

    for i in range(len(word) - 1):
        if word[i:i + 2].isalpha():
            jakadList.append(word[i:i + 2].upper())

    return Counter(jakadList)


def solution(str1, str2):
    answer = 1
    strDic1 = jakad(str1)
    strDic2 = jakad(str2)

    inters = sum((strDic1 & strDic2).values())
    union = sum((strDic1 | strDic2).values())

    if inters == 0 or union == 0:
        return 65536

    answer = math.floor((inters / union) * 65536)

    return answer