# https://www.acmicpc.net/problem/14499
'''
주사위 굴리기
[문제]
지도 위에서 주사위를 굴리며 이동할 때
바닥면에 닿은 부분의 값이 0이 아니면 바닥면으로 바뀌고 해당 좌표는 0으로 변경되며
좌표의 값이 0이면 주사위 바닥면의 값이 해당 좌표로 이동한다.
주어진 좌표대로 이동하면서 가장 위 숫자를 출력하는 문제

[접근]
주사위를 굴리는 방향은 상하좌우 4방향밖에 없다.


따라서 6면체 1차원 배열을 만들고
    상 하 좌 우 이동 시키기
    dice = [2, 1, 5 ,6, 4, 3] -> idx 1이 상단, 3이 하단, 5가 동쪽
    - [북,상단,남,하단,서,동]
    이때 상 하 좌 우 이동 시 배열이 어떻게 이동하는지 시뮬레이션으로 해결하기

[상]
    dice를 위로 이동시키면 index 4, 5번은 고정이고 
    0~3 사이의 인덱스가 역방향으로 rotate 된다
    dice = [2, 1, 5 ,6, 4, 3]
    next_dice = [1, 5, 6, 2, 4, 3] 
[하]
    dice를 위로 이동시키면 index 4, 5번은 고정이고 
    0~3 사이의 인덱스가 정방향으로 rotate 된다
    dice = [2, 1, 5 ,6, 4, 3]
    next_dice = [6, 2, 1, 5, 4, 3] 
[좌]
    dice를 왼쪽으로 이동시키면 index 0, 2번은 고정이고 
    4번 인덱스가 바닥, 1번 인덱스가 서쪽, 5번 인덱스가 천장, 3번 인덱스가 동쪽으로 이동한다
    dice = [2, 1, 5 ,6, 4, 3]
    next_dice = [2, 3, 5, 4, 1, 6]
[우]
    dice를 오른쪽으로 이동시키면 index 0, 2번은 고정이고 
    5번 인덱스가 바닥, 3번 인덱스가 서쪽, 4번 인덱스가 천장, 1번 인덱스가 동쪽으로 이동한다
    dice = [2, 1, 5 ,6, 4, 3]
    next_dice = [2, 4, 5, 3, 6, 1]
'''
from collections import deque
import sys

NORTH_IDX = 0
TOP_IDX = 1
SOUTH_IDX = 2
BOTTOM_IDX = 3
WEST_IDX = 4
EAST_IDX = 5

EAST_DIR = 1
WEST_DIR = 2
NORTH_DIR = 3
SOUTH_DIR = 4

def input(): return sys.stdin.readline().rstrip()


def move(dir, nr, nc):
    '''
    1. 주사위를 이동한다.
    2. 상단 값을 출력한다.
    3. 이동한 좌표의 값에 따라 값을 갱신한다.
    4. 이동한 좌표를 반환한다.
    '''
    global dice, grid
    # 1. 주사위를 이동한다
    roll_dice(dir)
    
    # 2. 상단 값을 출력한다.
    print(dice[TOP_IDX])

    # 3. 이동한 좌표의 값에 따라 값을 갱신한다.
    if grid[nr][nc] == 0:
        grid[nr][nc] = dice[BOTTOM_IDX]
    else:
        dice[BOTTOM_IDX] = grid[nr][nc]
        grid[nr][nc] = 0

    # 4. 이동한 좌표 반환
    return nr, nc

def roll_dice(dir):
    global dice
    temp_dice = dice[:]
    if dir == EAST_DIR:
        dice[BOTTOM_IDX], dice[WEST_IDX], dice[TOP_IDX], dice[EAST_IDX] = temp_dice[5], temp_dice[3], temp_dice[4], temp_dice[1]
    elif dir == WEST_DIR:
        dice[BOTTOM_IDX], dice[WEST_IDX], dice[TOP_IDX], dice[EAST_IDX] = temp_dice[4], temp_dice[1], temp_dice[5], temp_dice[3]
    elif dir == NORTH_DIR:
        dice[0], dice[1], dice[2], dice[3] = temp_dice[1], temp_dice[2], temp_dice[3], temp_dice[0]
    elif dir == SOUTH_DIR:
        dice[0], dice[1], dice[2], dice[3] = temp_dice[3], temp_dice[0], temp_dice[1], temp_dice[2]

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

if __name__ == "__main__":
    n, m, start_r, start_c, k  = map(int, input().split())
    
    dice = [0] * 6
    grid = [list(map(int, input().split())) for _ in range(n)]
    next_move = deque(map(int, input().split()))

    r, c = start_r, start_c
    while next_move:
        dir = next_move.popleft()
        nr, nc = r + dr[dir], c + dc[dir]
        if 0 <= nr < n and 0 <= nc < m:
            r, c = move(dir, nr, nc)
