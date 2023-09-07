# https://school.programmers.co.kr/learn/courses/30/lessons/159993

maps = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
# maps = ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]

INF = float("inf")
from collections import deque


def bfs(start, end, count, maps):
    MAX_ROW = len(maps)
    MAX_COL = len(maps[0])
    map_count = [[INF] * MAX_COL for _ in range(MAX_ROW)]
    map_count[start[0]][start[1]] = count
    dq = deque([[start[0], start[1], count]])
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while dq:
        r, c, count = dq.popleft()
        if map_count[end[0]][end[1]] != INF:
            break
        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            if (0 <= nr < MAX_ROW) and (0 <= nc < MAX_COL):
                if maps[nr][nc] != "X":
                    if map_count[nr][nc] > count + 1:
                        map_count[nr][nc] = count + 1
                        dq.append([nr, nc, count + 1])

    if map_count[end[0]][end[1]] == INF:
        return -1
    return map_count[end[0]][end[1]]


def solution(maps):
    MAX_ROW = len(maps)
    MAX_COL = len(maps[0])

    for i in range(MAX_ROW):
        for j in range(MAX_COL):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "E":
                end = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)

    # 레버까지 최단경로
    len_to_lever = bfs(start, lever, 0, maps)

    if len_to_lever == -1:
        return -1
    len_to_end = bfs(lever, end, len_to_lever, maps)
    return len_to_end


print(solution(maps))
# bfs로 레버로 가는 길 찾고, save 한 다음 레버부터 end까지 start
