def solution(park, routes):
    H, W = len(park)-1, len(park[0])-1
    y, x = [(i, line.find('S'))for i, line in enumerate(park) if 'S' in line][0]
    row_park = list(zip(*park))
    print("park : ", park)
    print("*park : ", *park)
    print("zip(*park) : ", zip(*park))
    print("row_park : ", row_park)

    for i in routes:
        way, dis = i.split()
        if way == 'E':
            if x + int(dis) <= W and 'X' not in park[y][x:x+int(dis)+1]:
                x += int(dis)
        elif way == 'W':
            if 0 <= x - int(dis) and 'X' not in park[y][x-int(dis):x]:
                x -= int(dis)
        elif way == 'S':
            if y + int(dis) <= H and 'X' not in park[x][y:y+int(dis)+1]:
                y += int(dis)
        else:
            if 0 <= y - int(dis) and 'X' not in park[x][y-int(dis):y]:
                y -= int(dis)
    return [y, x]


park = ["SOO", "OXX", "OOO"]
routes=["E 2", "S 2", "W 1"]

print(solution(park, routes))