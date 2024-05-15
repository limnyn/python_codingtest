# https://www.acmicpc.net/problem/2138
'''
[조건]
    N(2 ≤ N ≤ 100,000)
[목적]
    시작 상태와 마무리 상태가 주어졌을 때
    마무리 상태로 변경하기 위해서 최소한으로 바꿔야 하는 경우는?

[접근]
    현재 상태가 주어졌을 때 원하는 값으로 변경하는 방법


    A. 첫 전구(0번 전구)를 켜는 경우, 끄는 경우에 대해 2번을 수행

    B. i >= 1부터 뒤의 값에 대비해서 변경

        [2. i >= 1부터 뒤의 값에 대비해서 변경]
            start[i] 전구를 end[i] 전구 상태로 만들기 위해서는
            [i+1]번째 전구를 조작한다.

            이런 과정을 통해 
                start의 0~i번째 전구는 
                end의 0~i번째 전구까지 동일한 상태로 만들 수 있다.
            
'''

import sys
input = sys.stdin.readline


def rev(num):
    if num == 0:
        return 1
    else:
        return 0
def switching_bulbs():
    count_1 = 0
    # A - 첫 번째 전구를 바꾸지 않는 경우
    start_1 = init[:]
    # B - i >= 1 부터 end 상태로 i를 세팅
    for i in range(1, n):
        if start_1[i-1] != end[i-1]:
            count_1 += 1
            start_1[i-1] = rev(start_1[i-1])
            start_1[i] = rev(start_1[i])
            if i+1 < n:
                start_1[i+1] = rev(start_1[i+1])
    
    # A - 첫 번째 전구를 바꾸는 경우
    start_2 = init[:]
    start_2[0] = rev(start_2[0])
    if n >= 2:
        start_2[1] = rev(start_2[1])
    count_2 = 1
    # B - i >= 1 부터 end 상태로 i를 세팅
    for i in range(1, n):
        if start_2[i-1] != end[i-1]:
            count_2 += 1
            start_2[i-1] = rev(start_2[i-1])
            start_2[i] = rev(start_2[i])
            if i+1 < n:
                start_2[i+1] = rev(start_2[i+1])

    # 두 경우 중 일치할 때의 최솟값 출력
    min_count = float('inf')
    if start_1 == end:
        min_count = min(count_1, min_count)
    if start_2 == end:
        min_count = min(count_2, min_count)
    if min_count == float('inf'):
        return -1
    return min_count






if __name__ == "__main__":
    
    n = int(input())
    init = list(map(int, list(input().strip())))
    end = list(map(int, list(input().strip())))

    print(switching_bulbs())