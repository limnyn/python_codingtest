# https://www.acmicpc.net/problem/13397
'''
[문제]
    1차원 배열에 대해 M개 이하의 구간으로 나누어서 구간의 점수의 최댓값을 최소로 하려고 한다.
    구간은 다음과 같은 조건을 만족해야 한다.
    
    1. 하나의 구간은 하나 이상의 연속된 수들로 이루어져 있다.
    2. 배열의 각 수는 모두 하나의 구간에 포함되어 있어야 한다.
    
    구간의 점수란 구간에 속한 수의 최댓값과 최솟값의 차이다.

[입력]
    1 <= N <= 5000
    1 <= M <= N

[접근]
    이분탐색 - 파라매트릭 서치로 접근해보기

    특정 구간 내의 최대값고 최소값의 차이를 standard로 고정한다.
    그리고 구간이 standard를 초과하지 않는 단위로 구간을 나눈다

    이 때 정해진 standard에 따라 나눈 구간의 개수가 M개를 초과하면 안된다.
    
    구간의 개수가 M을 초과하면 standard를 줄이고,
    M과 같거나 작으면 standard를 늘인다.

    최종적으로 구간의 갯수가 m을 넘지 않는 마지막 right가 정답이된다

'''
import sys
def input(): return sys.stdin.readline().rstrip()

def section_counter():
    count = 1
    i = 0
    min_n, max_n = float('inf'), float('-inf')
    while i < n:
        min_n = min(arr[i], min_n)
        max_n = max(arr[i], max_n)
        if max_n - min_n > standard:
            count += 1
            min_n, max_n = float('inf'), float('-inf')
            i -= 1
        i += 1
    return count


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    left, right = 0, max(arr)
    
    while left < right:
        standard = (left + right)//2
        if section_counter() <= m:
            right = standard
        else:
            left = standard + 1
    
    print(right)