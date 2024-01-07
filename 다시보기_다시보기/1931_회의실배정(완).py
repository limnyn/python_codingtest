

n = int(input())
times = []

for _ in range(n):
    s, e = map(int, input().split())
    times.append([s,e])

times.sort(key=lambda x : (x[1], x[0]))
count = 1
end_time = times[0][1]

for time in times[1:]:
    s, e = time
    if end_time <= s:
        count += 1
        end_time = e

print(count)
