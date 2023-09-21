#옹알이
#2022 11 09

canWord = ["aya", "ye", "woo", "ma"]
babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
result = 0

for chkWord in babbling:
    if chkWord in canWord:
        result+=1
    else:
        word = list(chkWord)[0]




print(result)