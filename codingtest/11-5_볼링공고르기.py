# 입력 조건
#     첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어집니다.
#     (1 <= N ,= 1000, 1 <= M <= 10)
#     둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어집니다.
#     (1 <= K <= M)

# 출력 조건
#     첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력합니다.

# 입력 예시
#     8 5
#     1 5 4 3 2 4 5 2

# 출력 예시
#     25



# 겹치는 공의 개수가 a 개라 할 때  nC2 - (a-1)! 
n, m = map(int, input().split())
balls = list(map(int, input().split()))

array = [0] * 11 # 1~10의무게를 담는다
for ball in balls:
    array[ball] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n
print(result)


# import collections, itertools, math
# counter = collections.Counter(balls)
# # 같은 무게의 공의 개수들의 list를 만든다
# sameballs = [counter[x] for x in counter if counter[x] != 1]
# permu = itertools.combinations(balls, 2)
# nC2 = len(list(permu))
# for ball in sameballs:
#     nC2 -= math.factorial(ball-1)
    
# print(nC2)

