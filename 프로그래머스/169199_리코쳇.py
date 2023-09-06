# https://school.programmers.co.kr/learn/courses/30/lessons/169199


board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]  # 7 출력
# board = [".D.R", "....", ".G..", "...D"] # -1 출력
INF = float("inf")


from collections import deque


def solution(board):
    # 입력단
    MAX_ROW, MAX_COL = len(board), len(board[0])

    count_board = [[INF] * MAX_COL for _ in range(MAX_ROW)]

    for i in range(MAX_ROW):
        for j in range(MAX_COL):
            if board[i][j] == "R":
                start_r, start_c = i, j
            elif board[i][j] == "G":
                end_r, end_c = i, j

    dq = deque([[start_r, start_c, 1]])

    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while dq:
        if count_board[end_r][end_c] != INF:
            return count_board[end_r][end_c]

        curr_r, curr_c, count = dq.popleft()
        for dr, dc in dir:
            post_r, post_c = curr_r, curr_c

            while (
                0 <= post_r + dr < MAX_ROW
                and 0 <= post_c + dc < MAX_COL
                and board[post_r + dr][post_c + dc] != "D"
            ):
                post_r = post_r + dr
                post_c = post_c + dc

            if count < count_board[post_r][post_c]:
                count_board[post_r][post_c] = count
                dq.append([post_r, post_c, count + 1])

    return -1


print(solution(board))


"""
시작하면 입력 그리드 크기만큼 INF로 초기화하고
시작점과 종결점의 위치를 받는다.

그리고 deque에 시작점과 count 1을 넣는다

while문을 통해 충돌할 때까지 직진한다.
충돌 시에 현 위치 그리드에 대해 count값과 비교하고, 만약 작다면 deque에 넣는다.


BFS는 한 루프마다 닿는 곳이 최소 이동 거리이기 때문에
goal에 최초로 닿으면 거기가 최단거리이다.


"""
