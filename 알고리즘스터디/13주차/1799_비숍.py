# https://www.acmicpc.net/problem/1799

'''
문제
    놓을 수 있는 공간이 주어졌을 때
    비숍을 "가장 많이" 놓는 경우의 비숍의 수

    1 <= N <= 10

접근 
    모든 경우를 탐색하면서 비숍의 수보다 많은 경우를 출력해야 한다
    
    그러면 경우에 대해서 어떻게 해야할까?
    2차원 행렬에 대해 넣었을 때 안넣었을 때를 계산해 볼까?

        
    
    

'''
import sys, copy
sys.setrecursionlimit(10**6)
dr = [-1,-1,1,1]
dc = [-1,1,-1,1]
board_bishops = []
def board_setter(next_bishop):
    global board
    '''
    보드를 받아서 비숍을 설정한 뒤
    보드 갱신
    '''
    r, c = next_bishop
    # next_board = copy.deepcopy(board)

    board[r][c] = 0
    for i in range(4):
        nr, nc = next_bishop
        while True:
            nr = nr + dr[i]
            nc = nc + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                board[nr][nc] = 0
            else:
                break

    


def bishop_comb(r,c):
    global bishops, max_bishop
    for i in range(r,n):
        for j in range(n):
            if i == r and j <= c:
                continue
            if board[i][j] == 1:
                # 해당 칸에 비숍을 놓지 않았을 때
                bishop_comb(i,j)
                # 비숍을 놓았을 때
                bishops += 1
                board_setter((i,j))
                if max_bishop < bishops:
                    max_bishop = bishops
                bishop_comb(i,j)
                # bishops -= 1
                '''
                해당 코드에 대해 백트래킹 시간을 줄이기 위해 맵을 여러 개 사용하는 방식을 구현하려 했지만 맵을 되돌리는 과정이 부족한 것 같다. 따라서 이 부분 수정 필요
                '''
                
                
                



        


# if __name__ == "__main__":
n = int(input())
max_bishop = 0
bishops = 0
board = [list(map(int, input().split())) for _ in range(n)]
bishop_comb(0,-1)
# if board[0][0] == 1:
#     board_setter((0,0))
#     if max_bishop < 1:
#         max_bishop = 1        
#     bishop_comb(0,0,1)
print(max_bishop)

                




