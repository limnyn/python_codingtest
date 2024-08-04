# https://www.acmicpc.net/problem/2568
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

LIS 원소 찾기
이후 dp에서 가장 큰 수부터 작은수까지 뒤에서 부터 찾는다
    
    이후 True인 값을 순서대로 출력


'''

import sys
import bisect

def input():
    return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    wires = []
    a_set = set()

    for _ in range(n):
        a, b = map(int, input().split())
        wires.append((a, b))
        a_set.add(a)

    wires.sort(key=lambda x: x[0])  # A 전봇대 기준으로 정렬

    b_array = [wire[1] for wire in wires]
    lis = []
    lis_idx = []

    for i, b in enumerate(b_array):
        if not lis or b > lis[-1]:
            lis.append(b)
            lis_idx.append(len(lis) - 1)
        else:
            pos = bisect.bisect_left(lis, b)
            lis[pos] = b
            lis_idx.append(pos)

    lis_length = len(lis)
    to_remove = n - lis_length

    print(to_remove)  # 제거해야 할 전깃줄의 개수

    keep = set()
    for i in range(n - 1, -1, -1):
        if lis_length > 0 and lis_idx[i] == lis_length - 1:
            keep.add(wires[i][0])
            lis_length -= 1

    remove = a_set - keep
    for a in sorted(remove):
        print(a)