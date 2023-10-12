# https://www.acmicpc.net/problem/1927

answer = []
import heapq, sys

input = sys.stdin.readline
hq = []
for i in range(int(input())):
    oper = int(input())
    if oper == 0:
        if len(hq) == 0:
            answer.append(0)
        else:
            answer.append(heapq.heappop(hq))
    else:
        heapq.heappush(hq, oper)

for ans in answer:
    print(ans)
