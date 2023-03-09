# https://www.acmicpc.net/problem/15686

N, M = map(int, input().split())

houses = []
chickens = []
for row in range(N):
    line = list(map(int, input().split()))
    for col, spot in enumerate(line):
        if spot == 1:
            houses.append([row, col, 1e9])
        if spot == 2:
            chickens.append([row,col])                   



def calc_dist(houses, chickens):
    chicken_dist = 0
    for house in houses:
        house[2] = 1e9
        for cx, cy in chickens:
            x, y = house[0], house[1]
            dist = abs(x - cx) + abs(y - cy)
            house[2] = min(dist, house[2])
        chicken_dist += house[2]
    return chicken_dist

            
# 치킨집 갯수중에 M개를뽑는 조합 
import itertools
combination = list(itertools.combinations(chickens, M))
result = 1e9
for comb in combination:
    result = min(result, calc_dist(houses,comb))

print(result)
