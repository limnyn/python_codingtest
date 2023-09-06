import copy


def solution(board):
    answer = 0

    n = len(board)
    safe_area = [[0] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                safe_area[i][j] = 1
                safe_area[i + 1][j] = 1
                safe_area[i + 2][j] = 1
                safe_area[i][j + 1] = 1
                safe_area[i][j + 2] = 1
                safe_area[i + 1][j + 1] = 1
                safe_area[i + 1][j + 2] = 1
                safe_area[i + 2][j + 1] = 1
                safe_area[i + 2][j + 2] = 1
    answer = 0
    for line in safe_area[1:-1]:
        answer += sum(line[1:-1])
    return n**2 - answer


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
# result = 13
print(solution(board))
