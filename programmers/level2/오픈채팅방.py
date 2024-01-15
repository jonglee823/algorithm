#프로그래머스 오픈채팅방
def solution(record):
    answer = []
    nickDic = {}
    tempList = []

    for rec in record:
        recList = rec.split()

        if recList[0] == 'Enter':
            nickDic[recList[1]] = recList[2]
            tempList.append((recList[1], recList[2] + '님이 들어왔습니다.'))
        elif recList[0] == 'Leave':
            tempList.append((recList[1], nickDic[recList[1]] + '님이 나갔습니다.'))
        else:  # Change NickName
            nickDic[recList[1]] = recList[2]

    for temp in tempList:
        if temp[1][:temp[1].find('님이')] != nickDic[temp[0]]:
            answer.append(temp[1].replace(temp[1][:temp[1].find('님이')], nickDic[temp[0]]))
        else:
            answer.append(temp[1])

    return answer