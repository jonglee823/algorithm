def solution(n):
    answer = []
    

    return answer



# 다른사람 풀이 참고코드
#출처 : https://inspirer9.tistory.com/501
# def solution(n):
#     snake = [n]
#     print('start snake : ', snake)
#     d = ((0, 1), (1, 0), (0, -1), (-1, 0))
#     answer = [[0 for i in range(n)] for j in range(n)]
#     print('d(type) : ', type(d) )
#
#     count, x, y = 0, -1, 0
#
#     while n > 1:
#         n -= 1
#         snake.append(n)
#         snake.append(n)
#
#     print('snake : ', snake)
#     for i in range(len(snake)):
#         for j in range(snake[i]):
#             y += d[i % 4][0]
#             x += d[i % 4][1]
#             count += 1
#             answer[y][x] = count
#             print('i: ', i, ' y: ', y, 'x : ', x, ' y : ', y, ' answer[y][x]: ' ,answer[y][x])
#
#     return answer


solution(3)