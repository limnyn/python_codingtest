# # https://school.programmers.co.kr/learn/courses/30/lessons/154540

# maps = ["XXX", "XXX", "XXX"]
maps = ["X591X", "X1X5X", "X231X", "1XXX1"]
# import sys

# sys.setrecursionlimit(10000)
from collections import deque


def solution(maps):
    MAXROW = len(maps)
    MAXCOL = len(maps[0])
    is_visited = [[0] * MAXCOL for _ in range(MAXROW)]
    answer = []

    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for r in range(MAXROW):
        for c in range(MAXCOL):
            if maps[r][c] == "X" or is_visited[r][c]:
                continue
            dq = deque()
            dq.append([r, c])
            is_visited[r][c] = 1
            maps_sum = int(maps[r][c])

            # 만약 방문한적 없는 곳이라면 큐에 넣고
            # 큐가 빌때까지 주변을 다 더하는 방식

            while dq:
                x, y = dq.popleft()
                for dr, dc in dir:
                    nr, nc = x + dr, y + dc
                    if (
                        0 <= nr < MAXROW
                        and 0 <= nc < MAXCOL
                        and not is_visited[nr][nc]
                        and maps[nr][nc] != "X"
                    ):
                        dq.append([nr, nc])
                        is_visited[nr][nc] = 1
                        maps_sum += int(maps[nr][nc])
            answer.append(maps_sum)
    answer.sort()

    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer


print(solution(maps))


# 아래는 비효율적인 DFS 정답
# def counting_cells(r, c, maps_mark):
#     if (r < 0 or r >= len(maps_mark)) or (c < 0 or c >= len(maps_mark[0])):
#         return 0
#     elif maps_mark[r][c] < 0:
#         return 0
#     else:
#         now = maps_mark[r][c]
#         maps_mark[r][c] = -1
#         return (
#             # maps_mark[r][c]
#             now
#             + counting_cells(r - 1, c, maps_mark)
#             + counting_cells(r, c - 1, maps_mark)
#             + counting_cells(r + 1, c, maps_mark)
#             + counting_cells(r, c + 1, maps_mark)
#         )


# def solution(maps):
#     MAX_ROW = len(maps)
#     MAX_COL = len(maps[0])
#     maps_mark = [[0] * MAX_COL for _ in range(MAX_ROW)]
#     for i in range(MAX_ROW):
#         for j in range(MAX_COL):
#             if maps[i][j] == "X":
#                 maps_mark[i][j] = -1
#             else:
#                 maps_mark[i][j] = int(maps[i][j])
#     answer = []
#     for i in range(MAX_ROW):
#         for j in range(MAX_COL):
#             if maps_mark[i][j] != -1:
#                 answer.append(counting_cells(i, j, maps_mark))
#     if answer:
#         return sorted(answer)

#     return [-1]


# # print(maps_mark)

# print(solution(maps))
# """
# 모든셀에 대해
# 각 셀이 0이 아니면 출발한다.


# """
