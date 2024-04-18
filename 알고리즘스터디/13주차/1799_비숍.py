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
    - 시간 초과


    효율적인, 적게 계산할 방법 찾기

    -> 대각선으로 놓기

    비숍은 대각선에 하나만 존재가 가능하다. 
    따라서 n-queen을 대각선으로 접근해서 풀어보자
    대각선에 하나만 놓고, 놓았을 때 역 대각선에 존재하는지 보면 된다!

    n*(n+1)

        
    
    

'''
import sys, copy
sys.setrecursionlimit(10**6)
dr = [-1,-1,1,1]
dc = [-1,1,-1,1]
board_bishops = []

def board_setter(bishops):
    '''
    보드를 받아서 비숍을 설정한 뒤
    '''
    next_board = copy.deepcopy(board)
    for next_bishop in bishops:    
        r, c = next_bishop
        if next_board[r][c] == 2:
            return False
        next_board[r][c] = 2
        for i in range(4):
            nr, nc = next_bishop
            while True:
                nr = nr + dr[i]
                nc = nc + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if next_board[nr][nc] == 2:
                        return False
                    next_board[nr][nc] = 2
                else:
                    break
                
    return True




bishop_lst = []
def bishop_comb(r,c,bishops):
    global max_bishop, bishop_lst

    for i in range(r,n):
        for j in range(n):
            if i == r and j <= c:
                continue
            if board[i][j] == 1:
                # 해당 칸에 비숍을 놓지 않았을 때

                bishop_comb(i,j,bishops)
                # 비숍을 놓았을 때
                if board_setter(bishops + [[i,j]]):
                    if max_bishop < len(bishops) + 1:
                        max_bishop = len(bishops) + 1    
                    bishop_comb(i,j, bishops+[[i, j]])
                

                # bishops -= 1
                
                
                
'''
5
1 1 0 1 1
0 1 0 0 0
1 0 1 0 1
1 0 0 0 0
1 0 1 1 1

3
0 1 1
1 1 1
1 1 1

4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1

5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1


8
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
'''


        


# if __name__ == "__main__":
n = int(input())
max_bishop = 0
bishops = 0
board = [list(map(int, input().split())) for _ in range(n)]

bishop_comb(0,-1,[])

print(max_bishop)

                




