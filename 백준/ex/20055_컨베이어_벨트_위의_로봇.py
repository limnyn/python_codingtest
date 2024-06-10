# https://www.acmicpc.net/problem/20055
'''
입력
    N, K, Ai ~ A2n 까지

    2 <= N <= 100
    1 <= K <= 2N
    1 <= Ai <= 1000

출력
    몇 번째 단계가 진행 중일때 종료되었는지 출력한다.

접근
    입력의 크기가 작고, 단순한 시뮬레이션 구현 문제라고 생각된다.


    [내구도]
        로봇이 1번칸에 올라가거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소
    [단계별 진행]
        1. 벨트+로봇을 한 칸 회전한다.
        2. 회전 이후 "먼저 벨트에 올라간 순서로" 각 로봇을 한칸씩 더 움직인다 (for each 로봇)
            2-1. 이때 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    
    [목표]
        종료되었을 때 몇 번째 까지 진행중이였는지
        -> 컨베이어 벨트가 몇 칸 회전했는지?
    
필요한 모듈

    [단계별 흐름]
    level += 1
    [1. 벨트 + 로봇회전]
        python의 deque 자료구조의 rotate를 사용해보자.
        벨트 1번, 로봇 1번 회전 시킨다.
        이 때, N번 칸에 로봇이 있다면 제거한다.
    
    [2. 로봇의 이동]
        n-1 번째 칸에서 부터 1번째 칸까지 역순으로 반복
        
        로봇이 존재할 때
            if 각 칸의 다음 칸에 로봇이 있지않고 내구도가 0 이상일때
                로봇을 다음 칸으로 이동시키고 해당 칸의 내구도 -= 1
                만약 내구도가 0이면 durability_zero += 1

    만약 로봇이 이동해서 N-1칸 도달하면 로봇 제거
    [3. 로봇 올리기]
        if 1번째 칸의 내구도 != 0:
            로봇 추가
            내구도 -= 1
            만약 내구도가 0이면 durability_zero += 1
    
    [4. 내구도 0인 칸 갯수 count]
        if durability_zero >= k:
            return level
'''
from collections import deque
import sys
input = sys.stdin.readline


def belt_and_robot_rotate():
    '''
    [1. 벨트 + 로봇회전]
    python의 deque 자료구조의 rotate를 사용해보자.
    벨트 1번, 로봇 1번 회전 시킨다.
    이 때, N번 칸에 로봇이 있다면 제거한다.
    '''
    belt.rotate(1)
    robot.rotate(1)
    if robot[n-1] == True:
        robot[n-1] = False

def robot_move():
    global durability_zero
    '''
    [2. 로봇의 이동]
    n-1 번째 칸에서 부터 1번째 칸까지 역순으로 반복
    
    로봇이 존재할 때
        if 각 칸의 다음 칸에 로봇이 있지않고 내구도가 0 이상일때
            로봇을 다음 칸으로 이동시키고 해당 칸의 내구도 -= 1
            만약 내구도가 0이면 durability_zero += 1

    만약 로봇이 이동해서 N-1칸 도달하면 로봇 제거
    '''

    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i] = False
            robot[i+1] = True

            belt[i+1] -= 1
            if belt[i+1] == 0:
                durability_zero += 1
    robot[n-1] = False

def load_robot():
    global durability_zero
    '''
    [3. 로봇 올리기]
    if 1번째 칸의 내구도 != 0:
        로봇 추가
        내구도 -= 1
        만약 내구도가 0이면 durability_zero += 1
    '''
    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            durability_zero += 1





if __name__ == "__main__":
    level = 0
    durability_zero = 0
    n, k = map(int, input().split())
    belt = deque(list(map(int, input().split())))
    robot = deque([False]*n)


    while True:
        level += 1
        # 1,2,3번 반복
        belt_and_robot_rotate()
        robot_move()
        load_robot()
        if durability_zero >= k:
            break
    print(level)
    


'''
[후기]
== 부호와 = 을 잘못 입력했는데 에러가 안나서 디버깅에 시간이 많이 걸렸다.
주의하도록 하자.
'''