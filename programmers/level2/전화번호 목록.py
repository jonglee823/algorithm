#프로그래머스 LELVE2
#전화번호 목록

def solution(phone_book):
    answer = True

    phoneDic = {}
    for num in phone_book:
        phoneDic[num] = 0

    for phone in phone_book:
        arr = ""
        for num in phone:
            arr += num
            if arr in phoneDic and arr != phone:
                return False

    return answer