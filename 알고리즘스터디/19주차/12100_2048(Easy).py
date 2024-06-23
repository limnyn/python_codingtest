# https://www.acmicpc.net/problem/12100
'''
[문제]
    최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램

[입력]
    보드의 크기 N*N (1 <= N <= 20)
    블록에 쓰여있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다.

    시간 제한 1초

[접근]
    완전 탐색 시 경우의 수는?

    한 상태에서 이동할 수 있는 경우는 최대 4가지

    모든 경우의 수 4^5
    N = 20일 때, 한 칸에 대한 이동을 400 * 1024 -> 409600번 연산

    시간 내 충분히 연산 가능하다.

[필요한 함수]
    
    1. 그래프가 주어졌을 때, 이동시키는 함수

    2. 횟수별로 4방향 이동하는 경우를 생섣하는 함수

[그래프가 주어졌을 때 이동시키는 함수]
    
    [조건 1. 이동할 때 두 블럭은 합쳐진다.]

    [조건 2. 이미 이동한 블럭은 합쳐지지 않는다.]

    [조건 3. 이동시키는 경우 이동 방향에 먼저 있는 두 블록이 합쳐진다.]

    
    조건을 만족하는 이동함수 만들기

    def move(dir, before_board):
        joined_node = [[False] * n for _ in range(n)]
        board = copy.deepcopy(before_board)
        방향에 따라서
        
        if dir == 좌
            0,0 0,1 0,2, ... 순서로 한 칸씩 탐색하며 이동한다.        
        
        LEFT만 구현한뒤 상, 하, 우방향은 보드를 회전하고 뒤집어서 상, 좌를 수행한 뒤 다시 뒤집어서 반환한다.
        
        LEFT 일때
            now_node의 이동경로에 prev_node가 존재하는지 확인한다.
            if prev_node가 존재하지 않으면:
                끝까지 이동하고 next_spot은 now_node의 옆자리로 표시한다.
            if prev_node가 존재하면:
                if joined_node 노드가 아니고 숫자가 동일하면:
                    prev_node *= 2를 수행하고 joined_node를 True로 변경한다.
                else:
                    next_spot으로 이동한다.
        return board
'''
import sys, copy
def input(): return sys.stdin.readline().rstrip()
LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3


def rotate_board_90degree(board):
    new_board = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_board[c][n-r-1] = board[r][c]
    return new_board

def rotate_board_270degree(board):
    new_board = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n): 
            new_board[n-c-1][r] = board[r][c]
    return new_board


def move(dir, before_board):
    global max_num
    joined_node = [[False] * n for _ in range(n)]
    board = copy.deepcopy(before_board)


    if dir == LEFT:
        for r in range(n):
            prev_node, next_spot = -1, -1
            c = 0
            while c < n:
                if board[r][c] == 0:
                    c += 1
                    continue

                if prev_node == -1:
                    board[r][0] = board[r][c]
                    if c != 0:
                        board[r][c] = 0
                    max_num = max(board[r][0], max_num)
                    prev_node = 0
                    next_spot = 1
                    c += 1
                    continue
                
                else:
                    if joined_node[r][prev_node] == False and board[r][prev_node] == board[r][c]:
                        board[r][prev_node] *= 2
                        max_num = max(board[r][prev_node], max_num)
                        joined_node[r][prev_node] = True
                        board[r][c] = 0
                    else:
                        
                        board[r][next_spot] = board[r][c]
                        max_num = max(board[r][next_spot], max_num)
                        prev_node = next_spot
                        if next_spot != c:
                            board[r][c] = 0
                        next_spot += 1
                    c += 1

    elif dir == UP: #board를 시계방향으로 270도 뒤집고 LEFT 수행하고 다시 뒤집으면 된다
        board = rotate_board_270degree(board)    
        board = move(LEFT, board)
        board = rotate_board_90degree(board)

    elif dir == DOWN: #board를 시계방향으로 90도 뒤집고 LEFT 수행하고 다시 뒤집으면 된다
        board = rotate_board_90degree(board)    
        board = move(LEFT, board)
        board = rotate_board_270degree(board)

    elif dir == RIGHT:
        for i in range(n):
            board[i].reverse()
        board = move(LEFT, board)
        for i in range(n):
            board[i].reverse()

    return board

        

def dfs(level, board):
    if level >= 5:
        return
    for dir in range(4):
        next_board = move(dir, board)
        dfs(level+1, next_board)
    return

if __name__ == '__main__':
    n = int(input())
    board_origin = [list(map(int, input().split())) for _ in range(n)]
    max_num = 1
    dfs(0, board_origin)
    print(max_num)