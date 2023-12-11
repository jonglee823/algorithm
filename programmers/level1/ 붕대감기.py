#프로그래머스 LEVEL1
#[PCCP 기출문제] 1번 /붕대감기

from collections import deque

def solution(bandage, health, attacks):
    answer = health
    queue = deque(attacks)
    lastATime = 0  # lastAttackTime

    while queue:
        attackTime, dealMount = queue.popleft()

        answer += ((attackTime - 1 - lastATime) // bandage[0] * bandage[2])
        answer += (((attackTime - 1 - lastATime)) * bandage[1])

        if answer > health: answer = health

        answer -= dealMount
        lastATime = attackTime

        if answer <= 0: return -1

    return answer