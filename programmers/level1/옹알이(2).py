#옹알이(2)
def solution(babbling):
    answer = 0
    canTalk = ["aya", "ye", "woo", "ma"]

    for talk in babbling:
        for can in canTalk:
            if can * 2 not in talk:
                talk = talk.replace(can, " ")
        if talk.isspace():
            answer += 1

    return answer

#test
# canTalk = ["aya", "ye", "woo", "ma"]
# for i in canTalk:
#     print( i * 2)
