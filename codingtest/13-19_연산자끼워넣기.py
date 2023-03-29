# https://www.acmicpc.net/problem/14888

# # 개선 후 코드
# import sys
# from itertools import permutations
# input = sys.stdin.readline

# n = int(input())
# nums = list(map(int, input().split()))
# cals = list(map(int, input().split()))
# permut = []
# for i in range(4):
#     for j in range(cals[i]):
#         permut.append(i)
        


# ops = set(list(permutations(permut)))
# max_num = -1e9
# min_num = 1e9
# for op in ops:
#     tmp = nums[0]
#     for i in range(n-1):
#         if op[i] == 0:
#             tmp += nums[i+1]
#         elif op[i] == 1:
#             tmp -= nums[i+1]
#         elif op[i] == 2:
#             tmp *= nums[i+1]
#         else:
#             if tmp < 0:
#                 tmp *= (-1)
#                 tmp //= nums[i+1]
#                 tmp *= (-1)
#             else:
#                 tmp //= nums[i+1]
#     max_num = max(max_num, tmp)
#     min_num = min(min_num, tmp)
            
# print(max_num)
# print(min_num)

#dfs를 이용한 풀이
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_value = -1e9
min_value = 1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대해 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])   
            add += 1
        if sub >  0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0 :
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now/data[i])) #나눌 때는 나머지를 제거
            div += 1
            
dfs(1, data[0])
print(max_value)
print(min_value)

    

# 개선 전 코드 , 실패
# import itertools, sys
# input = sys.stdin.readline

# n = int(input())
# nums = list(map(int, input().split()))
# cals = list(map(int, input().split()))
# permut =[i for i in range(1, n)]

# def index_to_cal(cal_index, cals, a, b): # return a cal b
#     index = 0
#     while(1):
#         if cals[index] < cal_index:
#             cal_index -= cals[index]
#             index +=1
#         else:
#             break
#     if index == 0:
#         return a + b
#     elif index == 1:
#         return a - b
#     elif index == 2:
#         return a * b
#     else:
#         if a < 0:
#             a *= (-1)
#             a //= b
#             a *= (-1)
#             return a
#         else:
#             return a // b

# cal_indexs = list(set(list(itertools.permutations(permut, n-1)))                 )

# max_num = -1e9
# min_num = 1e9
# for cal in cal_indexs:
#     tmp = nums[0]
#     for i in range(1, n):
#         tmp = index_to_cal(cal[i-1],cals,tmp, nums[i])
#     max_num = max(tmp, max_num)    
#     min_num = min(tmp, min_num)
    
# print(max_num)
# print(min_num)



