# https://www.acmicpc.net/problem/1620


n, m = map(int, (input().split()))

poketmon_name = {}
poketmon_list = {}
for i in range(n):
    pmon = input()
    poketmon_name[pmon] = i + 1
    poketmon_list[i + 1] = pmon

asks = []
for _ in range(m):
    asks.append(input())

for ask in asks:
    if ask.isdigit():
        print(poketmon_list[int(ask)])
    else:
        print(poketmon_name[ask])
