# https://www.acmicpc.net/problem/33094
"""
[문제]
N일 동안 하루에 마셔야 하는 우유 mL가 제공된다.
비스킷을 사용하면 우유를 마시지 않아도 된다.
최대 몇일 동안 버틸 수 있는지 구하는 문제

[입력]
N, M, K - 총 날짜, 전체 우유 량, 비스킷 갯수
Pi - 각 날짜별 마셔야 하는 우유 mL

[제약]
1 <= N <= 100

[출력]
가장 오래 버틸 수 있는 날짜를 계산하기

[접근]
# https://www.acmicpc.net/problem/1826
boj 1826 연료 채우기 처럼 풀기

    [최대힙]
        
        day_count = 0
        milk_max_heapq = []

        for milk in p_list:
            M -= milk
            heapq.heappush(milk_max_heapq, -1*milk) # 최대힙을 위해 음수로 삽입
            
            # 주어진 우유를 다 마신 경우
            if M < 0:
                
                # 비스킷이 남았을 때
                if K > 0: 
                    # 이전에 마셧던 우유 중 가장 큰 우유를 비스킷으로 대체
                    past_max_milk = heapq.heappop(milk_max_heapq)
                    M -= past_max_milk # 힙에 음수값으로 들어가있으므로 빼기 연산
                    
                # 비스킷이 없을 때
                else:
                    break
            
            day_count += 1
        
        print(day_count)
            

"""

import sys, heapq
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    p_list = list(map(int, input().split()))

    day_count = 0
    milk_max_heapq = []

    for milk in p_list:
        M -= milk
        heapq.heappush(milk_max_heapq, -1*milk) # 최대힙을 위해 음수로 삽입
        
        # 주어진 우유를 다 마신 경우
        if M < 0:
            
            # 비스킷이 남았을 때
            if K > 0: 
                # 이전에 마셧던 우유 중 가장 큰 우유를 비스킷으로 대체
                K -= 1
                past_max_milk = heapq.heappop(milk_max_heapq)
                M -= past_max_milk # 힙에 음수값으로 들어가있으므로 빼기 연산
                
            # 비스킷이 없을 때
            else:
                break
        
        day_count += 1
    
    print(day_count)