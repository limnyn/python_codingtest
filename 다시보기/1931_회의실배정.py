# https://www.acmicpc.net/problem/1931
import sys

input = sys.stdin.readline

n = int(input())
meetings = []
for i in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: (x[1], x[0]))

count = 1
endtime = meetings[0][1]
for s, e in meetings[1:]:
    if s < endtime:
        continue
    else:
        endtime = e
        count += 1


print(count)
