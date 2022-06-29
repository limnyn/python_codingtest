# 두 배열의 원소 교체

# 입력 조건
#     첫 번째 줄에 N, K가 공백으로 구분되어 입력된다.
#     두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다.
#     모든 원소는 10,000,000보다 작은 자연수이다.
#     세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다.
#     모든 원소는 10,000,000보다 작은 자연수입니다.

# 출력 조건
#     최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 보든 원소의 합의 최댓값을 출력한다.

# 입력 예시
#     5 3
#     1 2 5 4 3
#     5 5 6 6 5

# 출력 예시
#     26

n, k = map(int,input().split())

a = list(map(int,(input().split())))
b = list(map(int,(input().split())))

for _ in range(k):
    minA = min(a) 
    maxB = max(b)
    if minA < maxB:
        a.remove(minA)
        a.append(maxB)
        b.remove(maxB)
        b.append(minA)
    else:
        break
print(sum(a))