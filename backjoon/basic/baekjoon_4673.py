#baekjoon_4673
#https://somjang.tistory.com/entry/BaekJoon-4673번-셀프-넘버-Python 출처..

def find_none_self_number():
    selfNumberList = set(range(1, 10001))
    for num in range(1, 10001):
        for each_num in str(num):
            num += int(each_num)
        selfNumberList.discard(num)
    return selfNumberList

if __name__=="__main__":
    noneSelfNumberSet = find_none_self_number();
    for noneSelfNumber in noneSelfNumberSet:
        print(noneSelfNumber)