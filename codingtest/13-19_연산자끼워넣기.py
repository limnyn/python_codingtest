# https://www.acmicpc.net/problem/14888

import itertools, sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cals = list(map(int, input().split()))
permut =[i for i in range(1, n)]

def index_to_cal(cal_index, cals, a, b): # return a cal b
    index = 0
    while(1):
        if cals[index] < cal_index:
            cal_index -= cals[index]
            index +=1
        else:
            break
    if index == 0:
        return a + b
    elif index == 1:
        return a - b
    elif index == 2:
        return a * b
    else:
        if a < 0:
            a *= (-1)
            a //= b
            a *= (-1)
            return a
        else:
            return a // b

cal_indexs = list(itertools.permutations(permut, n-1))
max_num = -1e9
min_num = 1e9
for cal in cal_indexs:
    tmp = nums[0]
    for i in range(1, n):
        tmp = index_to_cal(cal[i-1],cals,tmp, nums[i])
    max_num = max(tmp, max_num)    
    min_num = min(tmp, min_num)
    
print(max_num)
print(min_num)



