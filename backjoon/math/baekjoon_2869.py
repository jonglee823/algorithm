#baekjoon_2869
#달팽이는 올라가고싶다..

#v 나무 높이
#a 낮에 올라간 높이
#b 밤에 미끄러진 높이

a,b,v = map(int,input().split())
day = (v-b)/(a-b)
print(int(day) if day == int(day) else int(day)+1)



# while location < height:
#     day +=1
#     location += up
#     if(location >= height):
#         break
#     else:
#         location -= down
# print(day)


#참고 https://stultus.tistory.com/entry/Python-백준-2869-달팽이는-올라가고-싶다
