
# 그래프의 노드 N 갯수 -> 2 <= N <= 10

# 10! = 3628800
# 모두 다 돌면 터질 수 도 있지만 
# 백트래킹으로 구간 별 이미 최소거리보다 큰 경우는 
# 탐색하지 않도록 하여 탐색 경우를 줄일 수 있다.


n = 0
corp = []
house = []
customers = []
visited = []

result = 2e9
house = []
def calc(nodes):
    # nodes[-1] 부터 house까지 거리를 계산해서 distance에 더해서 반환한다.
    distance = 0
    if len(nodes) > 1:
        for i in range(1, len(nodes)):
            n1x, n1y = customers[nodes[i-1]]
            n2x, n2y = customers[nodes[i]]
            distance += abs(n1x - n2x) + abs(n1y - n2y)
        
    nx, ny = customers[nodes[-1]]
    hx, hy = house
    
    return distance + (abs(hx - nx) + abs(hy - ny))


def backtracking(nodes, depth):
    global result, visited
    distance = calc(nodes)

    if result < distance:
        return
    if depth == n: 
        # 거리 계산하기.
        result = min(distance, result)
        return

    # 만약 현재까지 거리의 합이 result보다 크다면 가지치기, return

    # 탐색 시작
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            backtracking(nodes + [i], depth + 1)
            visited[i] = False

def solution():
    global n, house, corp, customers, nums, visited, result
    result = 2e9
    n = int(input())
    visited = [False] * (n+1)
    line = list(map(int, input().split()))
    corp = line[0:2]
    house = line[2:4]
    customers = [(line[0], line[1])]
    for i in range(n):
        customers.append((line[4+2*i], line[4+2*i+1]))

    visited[0] = True
    backtracking([0],0)


for t_c in range(1, int(input())+1):

    solution()
    print(f"#{t_c} {result}")



