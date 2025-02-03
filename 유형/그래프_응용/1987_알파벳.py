# https://www.acmicpc.net/problem/1987
"""
bfs를 활용한 풀이
"""
from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

def main():
    # 입력 처리
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]

    # 큐와 방문한 경로 추적용 set
    dq = deque([(0, 0, grid[0][0])])
    visited = set([(0, 0, grid[0][0])])  # (r, c, trace)로 방문 기록

    # 상하좌우 이동 방향
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    
    result = 0
    while dq:
        r, c, trace = dq.popleft()

        # 가장 긴 경로 갱신
        result = max(result, len(trace))

        # 상하좌우 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위 체크
            if 0 <= nr < R and 0 <= nc < C:
                char = grid[nr][nc]
                
                # 아직 지나지 않은 알파벳일 경우
                if char not in trace:
                    new_trace = trace + char
                    # 새로운 경로가 set에 없을 경우에만 추가
                    if (nr, nc, new_trace) not in visited:
                        dq.append((nr, nc, new_trace))
                        visited.add((nr, nc, new_trace))

    print(result)

if __name__ == "__main__":
    main()
