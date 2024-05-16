# https://www.acmicpc.net/problem/10775
'''
[문제]
    G개의 개이트, P개의 비행기
    1 <= G <= 10^5
    1 <= P <= 10^5

    비행기 p[i] = x일 때
    해당 비행기 p[i]는 1 ~ i번째 게이트 사이에만 도킹 가능하다

    만약 충돌이 일어나면 break Or return

    최대한 많은 비행기를 도킹시킬수 있는 경우?

[접근]
    [1. 비행기는 "순서대로" 도착한다]
        비행기가 순서대로 도착하므로, 해당 시점에서 가장 이득이 되는 경우를 생각해보자
        -> 현재 주어진 비행기번호에 대해 도킹할 수 있는 경우

        testcase 1
            G = 4, P = 3, 4, 1, 1 일 때

            gate = 1, 2, 3, 4
            plane= 3, 4, -사고

            result = 2


        testcase 2
            G = 6, P = 2, 2, 3, 3, 4, 4 일 때

            gate = 1, 2, 3, 4, 5, 6
            plane= 2, 2, 3, -사고

            result = 3

    [그리디 한 방법?]
        만약 현재 비행기가 3번이라면
        3, 2, 1번 순서로 탐색하면서 빈 곳이 있으면 도킹한다
        
        해당 방법 선택 이유
            x = p[i]일 때 
            p[i]비행기는 1~x까지 게이트 중에 하나를 선택할 수 있지만
            x보다 수가 작은 비행기는 x번 게이트를 갈 수 없으므로
            큰 수의 비행기가 큰 게이트부터 채워주는 것이 최대한 많이 비행기를 도킹 시킬 수 있는 경우이다.

            def airport_docking(plane_num):
                airport_close = True
                for i in range(plane_num-1, -1, -1): #plane_num이 5일때 4~0번 인덱스 순서로 탐색
                    if gate[i] == False:
                        gate[i] = True
                        airport_close = False
                        break
                
                
                return airport_close # 공항이 폐쇄되면 False, 비행기가 성공적으로 도킹하면 True

            
            메인함수
                count = 0
                for plane_num in planes:
                    if airport_docking(plane_num):
                        break
                    else:
                        count += 1
                print(count)

        해당 방법의 시간복잡도
            -> n^2 -> 10^10, 시간초과

    [시간 복잡도를 줄일려면?]
        같은 숫자에 대해서 반복 연산을 줄여보자
        
        만약 3번 비행기가 연속으로 들어오면 탐색이 반복된다.
        따라서 해당 비행기가 마지막으로 도킹한 게이트를 기록해두면 탐색 시간을 줄일 수 있다.

        3번 비행기가 처음 도착하면 3번 게이트에 들어가고 
            다음 3번 비행기는 2번 비행기가 도착했을 때 가야할 게이트와 동일하다. 
    
    ->[union find 적용]

            i번 비행기를 도킹하고 다음 i번 비행기 도킹장소를 i-1번 비행기 도킹 장소와 일치시킨다. 

        def find_parent(x):
            if gate[x] != x:
                gate[x] = find_parent(gate[x])
            return gate[x]

        def airport_docking(plane_num):

            
            # 다음 도킹할 탑승구 찾기
            b = find_parent(plane_num)
            if b == 0:
                return False # 없으면 (0이면) false

            a = find_parent(b-1)
            if a < b:
                gate[b] = a
            else:
                gate[a] = b

            return True
                
                

        
        

'''

import sys
input = sys.stdin.readline

def find_parent(x):
    if gate[x] != x:
        gate[x] = find_parent(gate[x])
    return gate[x]

def airport_docking(plane_num):

    
    # 다음 도킹할 탑승구 찾기
    b = find_parent(plane_num)
    if b == 0:
        return False # 없으면 (0이면) false

    a = find_parent(b-1)
    if a < b:
        gate[b] = a
    else:
        gate[a] = b

    return True
    
            

if __name__ == "__main__":
    g = int(input())
    p = int(input())

    gate = [x for x in range(g+1)]

    planes = [int(input()) for _ in range(p)]
    
    count = 0
    for plane_num in planes:
        if airport_docking(plane_num):
            count += 1
        else:
            break

    print(count)