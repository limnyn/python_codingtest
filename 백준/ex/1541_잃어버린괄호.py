# https://www.acmicpc.net/problem/1541

line = input().split("-")
for i in range(len(line)):
    line[i] = sum(map(int, line[i].split("+")))
if len(line) == 1:
    print(line[0])
else:
    result = line[0] - sum(line[1:])
    print(result)
