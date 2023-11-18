
for t_c in range(1, int(input())+1):
    n = int(input())
    nums = []
    for _ in range(n):
        a, b = map(int, input().split())
        nums.append((a,b))
    p = int(input())
    bus_station = []
    
    for _ in range(p):
        bus_station.append(int(input()))
    bus_count = [0]*p
    for i in range(p):
        station = bus_station[i]
        for num in nums:
            low, high = num
            if low <= station <= high:
                bus_count[i] += 1
    
    print(f'#{t_c}',end=' ')
    for cnt in bus_count:
        print(cnt, end=' ')
    print()
    