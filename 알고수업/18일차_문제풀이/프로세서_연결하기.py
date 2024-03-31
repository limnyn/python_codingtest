# 01767. 프로세서 연결하기.
from collections import deque


def change(x, y, idx, paint):
    dq = deque()
    dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[nx][ny] == 1:
            continue
        board[nx][ny] = paint
        dq.append((nx, ny))


def getDist(x, y, d):
    dist = 0
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return dist
        if board[nx][ny] != 0:
            return -1
        dist += 1
        x, y = nx, ny


def dfs(depth, core, total):
    global maxCore, minTotal
    if length - depth + core < maxCore:
        return
    if depth == length:
        if core > maxCore:
            maxCore = core
            minTotal = total
        elif core == maxCore and total < minTotal:
            minTotal = total
        return
    x, y = arr[depth]
    for idx in range(4):
        dist = getDist(x, y, idx)
        if dist != -1:
            change(x, y, idx, 2)
            dfs(depth+1, core+1, total+dist)
            change(x, y, idx, 0)
    dfs(depth + 1, core, total)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    board = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(N):
            if tmp[j] == 1:
                arr.append((i, j))
        board.append(tmp)

    length = len(arr)
    maxCore = -1e9
    minTotal = 1e9
    dfs(0, 0, 0)
    print(f"#{tc} {minTotal}")