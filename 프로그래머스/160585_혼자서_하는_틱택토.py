# https://school.programmers.co.kr/learn/courses/30/lessons/160585

"""
선공은 항상 O부터 시작한다.

조건들
    0인 경우
        O X 갯수 안맞을 때
        둘다 이기지 않을 때
    
    
    1인 경우 
        
        1개더 많을 때
            => X가 이기지 않을 때
        같을 때
            x만 이기거나 둘다 안이기거나
            => O가 이기지 않을 때
            
        O가 3개 미만인 경우에는 통과
        
        아무것도 없을때



    상태
        1. 시작 전
        2. 중간
        3. 승부 후
            
"""

def check_is_win(board, mark):
    if (
        (board[0][0] == board[0][1] == board[0][2] == mark)
        or (board[1][0] == board[1][1] == board[1][2] == mark)
        or (board[2][0] == board[2][1] == board[2][2] == mark)
        or (board[0][0] == board[1][0] == board[2][0] == mark)
        or (board[0][1] == board[1][1] == board[2][1] == mark)
        or (board[0][2] == board[1][2] == board[2][2] == mark)
        or (board[0][0] == board[1][1] == board[2][2] == mark)
        or (board[0][2] == board[1][1] == board[2][0] == mark)
    ):
        return 1
    else:
        return 0


def solution(board):
    # 기호의 갯수를 세는 기능
    count = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                count[0] += 1
            elif board[i][j] == "O":
                count[1] += 1
            elif board[i][j] == "X":
                count[2] += 1

    gap = count[1] - count[2]

    if gap > 1 or gap < 0:
        return 0

    if gap == 0:
        if check_is_win(board, "O"):
            return 0

    if gap == 1:
        if check_is_win(board, "X"):
            return 0

    return 1


# board = ["O.X", ".O.", "..X"]
# board = ["OXO", "XOX", "OXO"]
# board = ["XOX", "OOO", "XOX"]
# board = ["XXX", "OOO", "OX"]
# print(check_is_win(board, "X"))
# board = ["...", ".X.", "..."]
board = ["...", "...", "..."]
# board = ["OOO", "XOX", "OXX"]

print(solution(board))
