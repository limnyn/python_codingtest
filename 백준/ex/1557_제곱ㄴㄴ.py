# 제곱 ㄴㄴ
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	3862	1436	975	37.299%
# 문제
# 어떤수 N이 1이 아닌 제곱수로 나누어지지 않을 때, 이 수를 제곱ㄴㄴ수라고 한다. 제곱수는 4, 9, 16, 25와 같은 것이고, 제곱ㄴㄴ수는 1, 2, 3, 5, 6, 7, 10, 11, 13, ...과 같은 수이다.

# K가 주어졌을 때, K번째 제곱ㄴㄴ수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 K가 주어진다.

# 출력
# 첫째 줄에 K번째 제곱ㄴㄴ수를 출력한다.

# 제한
# 1 ≤ K ≤ 1,000,000,000
# 예제 입력 1 
# 13
# 예제 출력 1 
# 19
# 예제 입력 2 
# 1
# 예제 출력 2 
# 1
# 예제 입력 3 
# 100
# 예제 출력 3 
# 163
# 예제 입력 4 
# 1234567
# 예제 출력 4 
# 2030745



# 정답은 나오지만 메모리 초과되는 답안안



# 1000000000

# 메모리 초과
# maxNum = int(input())
# max2 = int(1.7*maxNum)
# result = []
# array = [False]*(max2)
# for i in range (2, int(max2**0.5)+1):
#     square = i**2
#     for j in range(0, max2, square):
#         if not array[j]:
#             array[j] = True
#     result.append(square)
# # print(result)
# for i in range(max2):
#     if array[i] == True:
#         array[i] = 0
#     else:
#         array[i] = i
# array = [i for i in array if i != 0]
# print(array[maxNum-1])


# 4 9 16 25 36 49 64 81 100
# 4+9-4*9
# 4+9+16-(4*9+4*16+9*16)+4*9*16


# 만약 1000까지 소수가 아닌 갯수를 찾을 때
# 2*3*5*7*11  = 2310,
# 1000//2310 == 0, 따라서 1000 아래 중에 2*3*5*7*11의 배수는 없다.
# 따라서 최대로 뽑는 개수는 4개까지 이므로 

# 정답 ==
# 1000 - (2,3,5,7)의 배수 - 2개의 공배수, + 3개의 공배수 - +(2*3*5*7)의 공배수

# 필요한 함수 -> 
#     1. m**0.5의 소수 찾기 
#     2. 곱이 m을 초과하지 않는 횟수 찾기
    
# 1557번에 적용하기
# 우리가 찾는 것 = 제곱ㄴㄴ수의 배열과 그 안의 m번째 수
#     1. 리스트에 n(n<=10억)보다 작은 제곱수 넣기
#         for i = 2; i**2 <= m i++:
#             list.append(i**2)
#     2. 리스트에서 곱이 m을 초과하지 않는 횟수 찾기
#     3. 포함배제 알고리즘 함수 만들기


def squareNoNo(n):
    p = 0
    for i in range(1, int(n ** 0.5) + 1, 1):
        p += mobius[i] * (n // (i * i))
    return p

l, r = 0, 2000000000
mobius = [0] * 1000001
k = int(input())
mobius[1] = 1

for i in range(1, 1000001):
    if mobius[i]:
        for j in range(i * 2, 1000001, i):
            mobius[j] -= mobius[i]
while l < r - 1:
    mid = (l + r) // 2
    if squareNoNo(mid) < k:
        l = mid
    else:
        r = mid
print(r)
        
