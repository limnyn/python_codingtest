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


import sys

maxNum = int(input())
max2 = int(1.7*maxNum)
result = []
array = [False]*(max2)
for i in range (2, int(max2**0.5)+1):
    square = i**2
    for j in range(0, max2, square):
        if not array[j]:
            array[j] = True
    result.append(square)
# print(result)
for i in range(max2):
    if array[i] == True:
        array[i] = 0
    else:
        array[i] = i
array = [i for i in array if i != 0]
print(array[maxNum-1])

# i = 2
# while(maxNum > 0):
#     if(i,int(max2))


# 1000000000