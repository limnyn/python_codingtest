# 평면상에 points 목록이 있을 때, 원점 (0, 0)에서 K번 가까운 점 목록을 순서ㅐ로 출력하라.
# 평면상 두 점의 거리는 유클리드 거리로 한다.

# 입력

points = [[3,3],[5,-1],[-2,4]]
K = 2
# 출력


import heapq
def getUclidDist(points,K):
    dists = []
    for x, y in points:
        dist = x*x + y*y
        heapq.heappush(dists,[dist, [x,y]])
    result = []
    for _ in range(K):
        result.append(heapq.heappop(dists)[1])
    return result
print(getUclidDist(points, K))
    
         