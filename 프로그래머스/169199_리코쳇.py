# https://school.programmers.co.kr/learn/courses/30/lessons/19199
# https://school.programmers.co.kr/learn/courses/30/lessons/169199?language=python3
# 해당 문제에 대한 접근을 하는 방법
# inf로 행렬을 정리해 놓고
# stop스팟에 대해 해당 위치에 대한 count보다작으면 그 경로가 최단 경로이므로 deque에 넣고 나머지는 생략한다
# 그러면 deque에 대하여 위치와 count만 들어가면 된다.


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

그 다음 solution에 대해
그냥 4방향 다 가는 걸로 한다. 이건 최적화의 문제이기 때문에
그리고 deque에 시작점과 count 1을 넣는다

while문을 통해 충돌할 때까지 직진한다.
충돌 시에 현 위치 그리드에 대해 count값과 비교하고, 만약 작다면 deque에 넣는다.


BFS는 한 루프마다 닿는 곳이 최소 이동 거리이기 때문에
goal에 최초로 닿으면 거기가 최단거리이다.


"""


# DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
# INF = float("inf")


# def solution(board):
#     MAX_R, MAX_C = len(board), len(board[0])

#     start, end = [0, 0], [0, 0]
#     for r in range(MAX_R):
#         for c in range(MAX_C):
#             if board[r][c] == "R":
#                 start = [r, c]
#             elif board[r][c] == "G":
#                 end = [r, c]

#     start_r, start_c = start
#     end_r, end_c = end
#     counts = [[INF] * MAX_C for _ in range(MAX_R)]
#     counts[start_r][start_c] = 0
#     dq = deque([[start_r, start_c, counts[start_r][start_c]]])
#     while dq:
#         if counts[end_r][end_c] != INF:
#             return counts[end_r][end_c]

#         curr_r, curr_c, curr_count = dq.popleft()

#         for dir_r, dir_c in DIRS:
#             post_r, post_c, post_count = curr_r, curr_c, curr_count + 1

#             while (
#                 0 <= post_r + dir_r < MAX_R
#                 and 0 <= post_c + dir_c < MAX_C
#                 and board[post_r + dir_r][post_c + dir_c] != "D"
#             ):
#                 post_r, post_c = post_r + dir_r, post_c + dir_c

#             if post_count < counts[post_r][post_c]:
#                 counts[post_r][post_c] = post_count
#                 dq.append([post_r, post_c, post_count])

#     return -1


# print(solution(board))
