#2023-10-13
#프로그래머스 LEVEL1 대충 만든 자판

def solution(keymap, targets):
    answer = []

    keySet = {}

    for keyList in keymap:
        for i, key in enumerate(keyList):
            # print("i : ", i, " key : ", key)
            if keySet.get(key) == None:
                keySet[key] = i + 1
                continue
            if keySet.get(key) > i:
                keySet[key] = i + 1

    for target in targets:
        x = 0
        for tarNumber in target:
            if keySet.get(tarNumber) == None:
                x = -1
                break
            else:
                x += keySet[tarNumber]
        answer.append(x)

    return answer