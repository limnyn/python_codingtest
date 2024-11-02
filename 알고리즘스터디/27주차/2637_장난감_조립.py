# https://www.acmicpc.net/problem/2637
'''
[문제]
기본 부품 - 중간 부품 - 완제품
각 완제품을 조힙하는데 필요한 기본 부품의 수를 한 줄에 하나씩 출력
반드시 기본 부품의 번호가 작은 것부터 큰 순서가 되도록 한다.
각 줄에는 기본 부품의 번호와 소요 개수를 출력한다.

[입력]
3 <= N <= 100

N
첫째 줄 N -> 1 ~ N-1 까지의 숫자는 기본 부품이나 중간 부품의 번호를 나타낸다
N은 완제품의 번호를 나타낸다

M
어떤 부품을 완성하는데 필요한 부품들 간의 관계가 3개의 자연수 X, Y, K로 주어진다.
중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다는 뜻이다.

예외
[두 중간 부품이 서로를 필요로 하는 경우가 없다]
-> 간선이 단방향이다. 
-> DAG 위상정렬로 접근이 가능하다.


[위상정렬 + memoization]
입력
- 각 입력에 대해 그래프로 만든다.
- 각 노드 별 입력간선의 수를 list로 가지고 있는다.
- 이때 입력간선이 0인 노드를 기본부품으로 기록한다.

연산
- (n + 1) * (n + 1) 으로 초기화된 배열을 가진다.
- 각 기본부품은 grid[i][i] = 1 로 초기화한다.

예시
1. 입력간선이 0인 노드 1번이 선택된다
2. 1번 노드가 5번 노드와 연결되어있을 때 (5번 부품이 1번 부품을 2개 필요로 할 때)
3. 1번부품의 5번 간선에 대해서
    for comp_num, comp_cnt in grid[1]:
        grid[5][comp_num] += comp_cnt * require_comp_cnt
        # require_comp_cnt : 5번 부품을 만들기 위해 필요한 1번 부품의 갯수
    이와 같이 함수를 적용하여 5번부품을 만들기 위한 1번 부품의 갯수를 구할 수 있다.
4. 5번부품의 입력간선 리스트에서 -1 한다.
    4-1. 만약 5번부품의 입력간선이 0이면 큐에 넣는다

1~4 과정을 반복한다.


[구현]
필요한 자료구조
memoization

'''
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    grid = [[0] * (n + 1) for _ in range(n + 1)] # 각 부품별 필요한 부품 수 저장
    graph = [[] for _ in range(n + 1)] # 그래프 구조 저장
    node_entry = [0] * (n + 1) # 입력 간선 저장
    
    for _ in range(int(input())): # m 입력
        x, y, k = map(int ,input().split())
        graph[y].append((x, k))
        node_entry[x] += 1
    
    # 입력간선 0인 노드 큐에 삽입
    basic_comp = []
    node_q = deque([])
    for i in range(1, n):
        if node_entry[i] == 0:
            basic_comp.append(i)
            node_q.append(i)
            grid[i][i] = 1 # comp_num, comp_cnt 초기화
    basic_comp.sort() # 기본부품 기록
    
    while node_q:
        start_node = node_q.popleft()
        start_node_comp_list = [] #현재 노드를 만들기 위해 필요한 부품번호와 해당 부품 수 -> 연산 횟수를 줄이기 위해 추가
        for comp_num in range(1, n+1):
            comp_cnt = grid[start_node][comp_num]
            if comp_cnt > 0:
                start_node_comp_list.append((comp_num, comp_cnt))

        for next_node, require_comp_cnt in graph[start_node]: 
            for comp_num, comp_cnt in start_node_comp_list:
                grid[next_node][comp_num] += (comp_cnt * require_comp_cnt) # 다음 노드에 현재 부품 갯수를 반영
            node_entry[next_node] -= 1
            if node_entry[next_node] == 0:
                node_q.append(next_node)
    
    for comp_num in basic_comp:
        print(comp_num, grid[-1][comp_num])
