

7# 입력 조건
#     첫째 줄에 정수 N이 주어진다.
#     둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다.
#     이때 정수는 1보다 크고 1000000 이하이다.
#     셋째 줄에는 정수 M이 주어진다.
#     넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고  10억 이하이다.

# 출력 조건
#     첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.


# 입력 예시
#     5
#     8 3 7 9 2
#     3
#     5 7 9

# 출력 예시
#     no yes yes


# 계수 정렬 / 카운팅 정렬로 풀기





stock = int(input())
items = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in items:
        print('yes', end=' ')
    else:
        print('no', end=' ')

print()

    

