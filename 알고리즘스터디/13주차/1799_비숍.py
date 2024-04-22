# https://www.acmicpc.net/problem/1799

'''
bishop
solution explore


목표 - 최대한 많이 놓을 수 있는 경우의 놓은 수

좌상단
12345
23456
34567
45678
56789

1 2 3 4 5 6 7 8 9 10
비숍은 "대각선 당 한 개만 놓을 수 있다"
따라서 각 대각선 길이 1~10 중 한 개 씩 넣어 보며 조합을 계산해 보면 된다
좌상단, 우상단 부터 출발하여 한 번 씩 탐색하면 
10! * 2 -> 7,257,600번


따라서 좌상단 대각선 한번 우상단 대각선 한번 조사하면 끝


수정 및 todos
    비숍의 특성
        체스판은 흑/백 교차되어 색칠되어 있다
        이 때 비숍은 흑색 칸에 있다면 흑색 칸에만 영향을 주고 반대쪽 색에는 영향을 주지 못한다
        따라서 백색 칸에 몇 개가 놓여 있던 흑색에 놓는 경우에 영향을 주지 않는다.

        이를 통해 흑색 칸에 최대한 비숍을 많이 두는 경우 + 백색 칸에 최대한 비숍을 많이 두는 경우
        두 조합을 나눔으로써 계산수를 줄일 수 있다
    비숍 방문 처리에 대한 해결법
        비숍에 대해 매 번 공간을 침해하는 지 계산을 하면 비효율 적이다 
        따라서 대각선에 대한 level에 대해 하나만 놓을 수 있는 공식이 있다
        즉 (0,0), (1,1) (2,2) --는 같은 위치이므로 놓을 수 없고
        (0,1)은 (2,1) (3,2)와 같은 위치이다
        이는 level에 대해서 j-i+N-1로 방문 처리를 1차원 배열로 확인할 수 있어 계산을 줄일 수 있다
        이 방법과 비숍의 특성을 적용해서 시간복잡도를 줄여 해결해보자
    위 방법으로 처음부터 다시짜기

'''

def n_bishops_left_upper(comb):
    '''
    index 처리에 대해 고민해보기
    대각선 인덱스는? 
        level의 갯수만큼 탐색가능
    좌상단의 대각선 갯수만큼 인덱스를 순회하려면?
    if level == 3일떄
        (3 0) (2 1) (1 2) (0 3) 순으로 진행한다
    이걸 for문으로 인덱스 만드는 코드
        for i in range(level):
            r, c = level-i, i

    따라서 해당 과정을 통해 level 별로 r,c에 대해 하나씩 순회해 보면서 level이 n만큼 되었을 때 계산해보기
    
    Todos
        예외 case 검사해보기
    '''
    global result
    level = len(comb)
    
    if level == n:

        result = max(bishop_counter(comb), result)
    
    for i in range(level):
        r, c = level - i, i
        if board[r][c] != 0: # 비숍을 놓을 수 있는 경우라면
            if bishop_counter(comb, (r,c)):
                n_bishops_left_upper(comb + [(r,c)])
    n_bishops_left_upper(comb+[(-1,-1)]) # 비숍을 선택하지 않은 경우
    


dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]
def bishop_counter(comb):
    '''
    조합에 유효하면 bishop 갯수 반환
    조합이 유효하지 않으면 -1 반환
    '''
    checker = copy.deepcopy(board)
    for c_r, c_c in comb:
        checker[c_r][c_c] = 1
    for r, c in comb:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            while 0 <= nr < n and 0 <= nc < n:
                if checker[nr][nc] ==


    return -1

import sys, copy
input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    board = list(map(int, input().split()))
    result = 0
    result = max(result, n_bishops_left_upper())
    # result = max(result, n_bishops_left_upper()) #n_bishops_right_upper 수행하기
``
    

