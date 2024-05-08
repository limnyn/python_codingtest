# https://www.acmicpc.net/problem/2638
'''
[문제]
    제약 조건
        5 <= N, M <= 100
    
    치즈가 녹는 조건
        -> 2 변 이상 외부와 노출되면 치즈가 녹는다
    
    출력
        "주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간"

[필요한 모쥴]
    1. 치즈 내부와 외부를 구분하는 모듈
        
        내부와 외부를 어떻게 구분할 수 있을까?
            문제에서 주어진 조건을 사용해 보자
            "모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다."
            
            따라서 맨 가장자리와 연결된 부분은 외부, 나머지 공간은 치즈 또는 내부공간이다.
            이를 AIR, CHEESE, UNKNOWN 상수로 설정했다.
    
[구현 방법에 대해서]
-> 백준의 백조의 호수 문제와 유사하게 접근해보자

    1. 치즈, 내부, 외부에 대해서 section 2차원 배열을 통해 구획을 표현해놓는다.
    
    A. 탐색 과정
        2. 현재 치즈 now_cheese에 대해서 다음 녹는 부분들을 next_melt deque에 넣는다.
            2-1. next_melt가 아닌 치즈들은 next_cheese에 넣어준다.
    
    B. 융해 과정
        3. 시간을 증가시킨다.    

        4. next_melt인 칸들에 대해서 모두 air으로 만들면서 next_air deque에 넣는다.
            4-1. 만약 녹인 치즈 주변에 unknown(치즈 내부)가 있다면 next_air에 넣는다.
            4-2. next_air를 통해 air와 연결된 치즈 내부 unknown을 air로 만들어준다.
        
        5. now_cheese = next_cheese로 넣어주고. next_cheese값을 비워준다.

    next_melt deque가 빌 때 까지 A - B를 반복한다.     
'''
from collections import deque
import sys
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
UNKNOWN = -1
CHEESE = 1
AIR = 2


def divide_sections():
    '''
        section 2차원 배열에 외부, 치즈, 치즈 내부를 구분한다.
        이를 AIR, CHEESE, UNKNOWN 상수로 구분한다.
    '''

    air_dq = deque([])
    air_dq.append((0,0))
    section[0][0] = AIR

    cheese_dq = deque([])
    while air_dq:
        r, c = air_dq.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if section[nr][nc] == UNKNOWN and grid[nr][nc] == 0:
                    section[nr][nc] = AIR
                    air_dq.append((nr,nc))
    for r in range(n):
        for c in range(m):
            if grid[r][c] == CHEESE:
                section[r][c] = CHEESE
                now_cheese.append((r,c))

    # 이제 section은 inside : -1, cheese : 1 air : 2, 로 마킹되어 있다






def find_next_melt_cheese():
    '''
    현재 치즈에서 다음 melt할 구역을 찾자.
    1. bfs 탐색을 하면서
    2. 4방향 탐색 시 2방향 이상 air면 next_melt에 넣자
    2-1. else경우에 다음시간의 치즈묶음 deque에 넣는다.
    '''
    while now_cheese:
        r, c = now_cheese.popleft()
        air_count = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if section[nr][nc] == AIR:
                    air_count += 1

        if air_count >= 2:
            next_melt.append((r,c))
        else:
            next_cheese.append((r,c))


def fill_up_air():
    '''
    1. 치즈를 녹이고 녹은 자리를 air로 바꾼다.
    2. 녹은 자리의 4방향 탐색을 하면서 주변에 치즈내부(UNKNOWN)이 있으면 air로 바꾸고 next_air큐에 넣는다.
        -> 이 경우 치즈가 녹아 치즈내부가 외부와 연결된 상태이다.
    3. next_air를 bfs탐색하며 연결된 치즈내부를 air로 채워준다.

    이를 통해 치즈를 녹이고 치즈 내부가 외부와 연결되면 air로 채울 수 있다.
    '''
    while next_melt:
        r, c = next_melt.popleft()
        section[r][c] = AIR
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
        
            if 0 <= nr < n and 0 <= nc < m:
                if section[nr][nc] == UNKNOWN:
                    section[nr][nc] = AIR
                    next_air.append((nr,nc))

    while next_air:
        r, c = next_air.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if section[nr][nc] == UNKNOWN:
                    section[nr][nc] = AIR
                    next_air.append((nr,nc))

    

if __name__ == "__main__":
    n, m = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(n)]
    section = [[-1] * m for _ in range(n)]
    time = 0

    now_cheese = deque([])
    next_cheese = deque([])
    next_melt = deque([])
    next_air = deque([])
    
    # 구획 나누기
    divide_sections()
    
    # 다음 melt 구역 구하기
    find_next_melt_cheese()

    while next_melt: # 다 녹을 때 까지
        time += 1 # 시간 증가시키기
        
        fill_up_air() # 녹이고 air 팽창시키기 + inside 정리하기
        now_cheese = next_cheese 
        next_cheese = deque([])

        find_next_melt_cheese() # 다음 melt 구역 정하기

    
    print(time)

