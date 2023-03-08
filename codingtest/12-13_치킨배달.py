# https://www.acmicpc.net/problem/15686

N, M = map(int, input().split())


city = []
houses = []
chickens = []
for row in range(N):
    line = list(map(int, input().split()))
    for col, spot in enumerate(line):
        if spot == 1:
            houses.append([row, col, 1e9])
        if spot == 2:
            chickens.append([row,col])                   
    city.append(line)



def calc_dist(houses, chickens):

    chicken_dist = 0
    for house in houses:
         
        house[2] = 1e9
        for chicken in chickens:
            x, y, house_to_chicken = house[0], house[1], house[2]
            cx, cy = chicken[0], chicken[1]
            dist = abs(x - cx) + abs(y - cy)
            
            if dist < house_to_chicken:
                house[2] = dist
                
        chicken_dist += house[2]
    

    return chicken_dist

            
# 치킨집 갯수중에 M개를뽑는 조합 
import itertools
combination = itertools.combinations(chickens, M)
result = 1e9
for comb in combination:
    comb_chicken = []
    for i in comb:
        # print("i = ",i)
        comb_chicken.append(i)
    dist = calc_dist(houses,comb_chicken)
    if dist < result:
        result = dist



print(result)
