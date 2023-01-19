# 제곱 ㄴㄴ 수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	512 MB	49278	9098	6290	20.813%
# 문제
# 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

# 입력
# 첫째 줄에 두 정수 min과 max가 주어진다.

# 출력
# 첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.

# 제한
# 1 ≤ min ≤ 1,000,000,000,000
# min ≤ max ≤ min + 1,000,000
# 예제 입력 1 
# 1 10
# 예제 출력 1 
# 7
# 예제 입력 2 
# 15 15
# 예제 출력 2 
# 1
# 예제 입력 3 
# 1 1000
# 예제 출력 3 
# 608


# 풀이
# 소수를 제곱시켜 min~max사이에 있는 수를 체크하며 제거, 

min, max = map(int, (input().split()))
result = max - min + 1

array = [False]*(max-min+1)
for i in range (2, int(max**0.5)+1):
    square = i**2
    for j in range((((min-1)//square)+1)*square, max+1, square):
        if not array[j-min]:
            array[j-min] = True
            result-=1
print(result)


# for j in range(((min-1//square)+1), max+1, square):
# https://chanhuiseok.github.io/posts/baek-16/
# min이 31일때 31//4 == 7 이고, (7+1)*4 = 32,  범위내 제일작은 제곱ㄴㄴ수이다
        # 따라서 32, 32+4, 32+8 32+12도 제곱 ㄴㄴ수로 찾을 수 있다)
# min이 32인 경우 이 공식이 성립되지 않기 때문에
        # 위 공식은 +1해주는 것 때문에 시작숫자를 -1해주면 전체적용이가능하다
        # 따라서 ((min-1)//square  +1)*square을 해준다.
    
        

# #메모리 초과한 답안 -> 탐색범위를 좁힐 수 있는데 좁히지 않음음
# min, max = map(int, input().split())
# answer = max - min + 1
# array = [False * (answer)]
# for i in range(2, int(max**0.5)+1):
#     squae = i ** 2
#     for j in range((((min-1)//squae)+1)*squae, max+1, squae):
#         if not array[j - min]:
#             array[j-min] =  True
#             answer -= 1




# # 소수 집합검색은 빨랐지만 밑의 반복문의 범위가 min max에 비례하지않고 정적으로 넓은 범위 검색
# # => 시간초과
# minNum , maxNum = map(int, input().split())

# n=int(math.sqrt(maxNum))

# a = [False,False] + [True]*(n-1)

# sqrList=[]

# for i in range(2,n+1):
#     if a[i]:
#         sqrList.append(i**2)
#     for j in range(2*i, n+1, i):
#         a[j] = False
# # print(sqrList)
# count = 0
# # print("sqrlist fin")
# # print(sqrList)
# # 시간 잡아먹는 부분
# for i in range(minNum,maxNum+1):
    
#     sqrhalf = sqrList[:]
#     if i in sqrhalf:
#         count+=1
#         continue
#     else:
#         sqrhalf = [x for x in sqrList if x <= i//2]
#     for s in sqrhalf:
#         if i % s == 0:
#             count += 1
#             break
# result = maxNum-minNum+1-count
# print(result)