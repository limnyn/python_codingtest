# 효율적인 화폐 구성

# 입력 조건
#     첫째 줄에 N, M이 주어진다.(1<=N<=100, 1<=M<=10000)
#     이후의 N개의 줄에는 각 화페의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.

# 출력 조건
#     첫째 줄에 경우의 수 X를 출력한다.
#     불가능할 때는 -1을 출력한다.

# 입력 예시 1
#     2 15
#     2
#     3

# 출력 예시 1
#     5

# 입력 예시 2
#     3 4
#     3 
#     5 
#     7

# 출력 예시 2
#     -1
n, m = list(map(int, input().split()))
d = [0] * (m+1)
wage = []
for _ in range(n):
    wage.append(int(input()))

for i in wage:
    d[i] = 1


for i in range(min(wage), m+1):
    arr = []
    for w in wage:
        if d[i-w] != 0:
            arr.append(d[i-w]+1)
    if len(arr) != 0:
        d[i] = min(arr)

if d[m] == 0:
    print(-1)
else:
    print(d[m])

            