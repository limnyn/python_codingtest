import sys
from bisect import bisect_left
def input(): return sys.stdin.readline().rstrip()
'''
숫자가 정답 LIS의 가장 뒤에 들어갈 경우에는 추가,
LIS 내부에 들어갈 때는 교체
'''

n = int(input()) 
nums = list(map(int, input().split())) 

lis = [] 

# LIS 이분탐색
for num in nums:
    pos = bisect_left(lis, num) 
    if pos < len(lis):
        lis[pos] = num 
    else:
        lis.append(num) 

print(len(lis)) 
