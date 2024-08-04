# https://www.acmicpc.net/problem/2565
'''
LIS로 가장 긴 증가수열을 찾는다
-> 해당 경우가 교차 없이 가장 전깃줄을 많이 설치하는 경우

i   0 1 2 3 4 5 6 7 8
a   0 8 2 9 1 4 6 7 10
d   
dp_arr = [0, 1, 2, 3, 4, 5]
a_arr =  [0, 1, 4, 6, 7, 10]
for num in nums:
    1. 현재 값보다 작은 가장 큰 값 X를 이분탐색으로 a_arr에서 찾는다
    2. 해당 X의 인덱스 x_i의 dp값 dp[x_i]에 + 1 한 값 D를 찾는다.
    3-1. 만약 해당 값이 없으면(dp배열 길이가 dp[x_i]+1보다 작으면) 현재값을 dp배열에 추가
    3-2. 만약 해당 값이 있으면 a_arr[x_i+1]값이 값이 num보다 크면 num으로 갱신해준다.
'''


import sys, bisect
def input(): return sys.stdin.readline().rstrip()
if __name__ == "__main__":
    n = int(input())
    max_a, max_b = -100, -100
    wire = []
    for _ in range(n):
        a, b = map(int, input().split())
        wire.append([a,b])
        max_a = max(max_a, a)
        max_b = max(max_b, b)
    wire.sort()
    nums = [b for a, b in wire]
    nums = [0] + nums
    dp = [0]
    a_arr = [0]
    for i in range(1, len(nums)):
        num = nums[i]
        before_idx = bisect.bisect_left(a_arr, num) - 1
        if len(dp) - 1 <= dp[before_idx]:
            dp.append(dp[-1]+1)
            a_arr.append(num)
        else:
            before_num = a_arr[before_idx + 1]
            if before_num > num:
                a_arr[before_idx + 1] = num
    
    print(n - dp[-1])



