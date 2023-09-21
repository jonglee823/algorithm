#맨처음에 생각한 소스코드, but 시간초과 발생..
# def solution(players, callings):
#     answer = players
#     for i in range (len(callings)):
#         arrIndex = answer.index(callings[i])
#         answer[arrIndex], answer[arrIndex+1] =answer[arrIndex+1], answer[arrIndex+1]
#     return answer


#인터넷에서 본 해답
def solution(players, callings):
    result = {players : i for i, players in enumerate(players)}
    print(result)

    for who in callings:
        idx = result[who]
        result[who] -= 1
        result[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players
#
players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
solution(players, callings)