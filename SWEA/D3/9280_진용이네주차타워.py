from collections import deque
for t_c in range(1, int(input())+1):
    n, m = map(int, input().split())
    ri, wi, logs = [], [], []
    cost = 0
    for _ in range(n):
        ri.append(int(input()))
    for _ in range(m):
        wi.append(int(input()))
    for _ in range(2*m):
        logs.append(int(input()))
    logs = deque(logs)
    parking = {}
    num_to_park = {}
    for i in range(n):
        parking[i] = -1


    ready = []
    ready = deque(ready)
    while logs:
        log = logs.popleft() #popleft로 교체
        if log > 0: #만약 입차할때
            log -= 1
            is_empty = False
            for i in range(n):
                if parking[i] == -1:
                    parking[i] = log
                    num_to_park[log] = i
                    is_empty = True
                    break
            if not is_empty:
                ready.append(log)
        elif log < 0: #만약 출차를 하게 되면
            log += 1
            empty_spot = num_to_park[-log] #나가면 이제 비는 곳
            cost += (ri[empty_spot] * wi[-log])
            parking[empty_spot] = -1
            if ready:
                next = ready.popleft()
                parking[empty_spot] = next
                num_to_park[next] = empty_spot

    print(f'#{t_c} {cost}')



"""
주차 규칙
1. 빈 공간이 있으면 바로 주차를 시킨다. 
    1-1. 주차가 가능할 때, 번호가 가장 작은 주차공간에 주차
2. 공간이 없으면 순서대로 입구에서 대기한다.
3. 주차 요금은 차량무게 * 공간별 비용, 이용시간 고려 X
"""