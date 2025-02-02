# https://www.acmicpc.net/problem/2310
"""
[접근]
모든 경우에 대해 가능한지 불가능한지 확인하는 경우
-> dfs를 통해 가능하면 탈출해보자
"""
import sys
def input(): return sys.stdin.readline().strip()

def dfs(graph, visited, node, pocket):
    """ DFS 탐색을 수행하여 목적지(n번 방) 도달 가능 여부 확인 """
    n = len(graph) - 1

    info, cost, neighbors = graph[node]

    if info == "L":
        pocket = max(pocket, cost)  # 최소 금액 보장
    elif info == "T" and pocket < cost:
        return False  # 돈이 부족하면 탐색 종료
    else:
        pocket -= cost

    if node == n:  # 마지막 방 도달
        return True

    for next_node in neighbors:
        if not visited[next_node]:
            visited[next_node] = True
            if dfs(graph, visited, next_node, pocket):
                return True
            visited[next_node] = False  # 백트래킹

    return False

def main():
    """ 여러 개의 테스트 케이스를 처리하는 메인 함수 """
    results = []
    
    while True:
        n = int(input())
        if n == 0:
            break

        graph = [None] * (n + 1)
        for i in range(1, n + 1):
            data = input().split()
            info, cost = data[0], int(data[1])
            neighbors = list(map(int, data[2:-1]))  # 마지막 값("-1") 제외
            graph[i] = (info, cost, neighbors)

        # 방문 배열 초기화 후 DFS 실행
        visited = [False] * (n + 1)
        visited[1] = True
        result = "Yes" if dfs(graph, visited, 1, 0) else "No"
        results.append(result)

    # 결과 한 번에 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
