# https://www.acmicpc.net/problem/1764
# import sys


# input = sys.stdin.readline
n, m = map(int, input().split())
unh = []
uns = []
for i in range(n):
    unh.append(input())
for i in range(m):
    uns.append(input())
s_unh = set(unh)
s_uns = set(uns)

answer = list(s_unh.intersection(s_uns))

print(len(answer))
for a in sorted(answer):
    print(a)
