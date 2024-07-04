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

    백준 공유기 설치 문제처럼 구간을 나누는 좌표 간격을 i로 고정한다.문어

    구간의 갯수가 M으로 제한되어 있다.
    
    따라서 배열을 A개로 쪼갰을 때, M개보다 갯수가 많아지면 조건을 수정하고
    
    구간에서 X = max(최대-최소)값 이라 할 때 X는 최댓값 - 0을 초과할 수 없다.
    따라서 해당 값 X를 기준으로 이분탐색을 하며
    만약 구간수가 M보다 크거나 같으면 mid 값을 증가시키고
    구간의 수가 M과 같거나 작으면 mid값을 감소시킨다
    해당 과정을 이분탐색을 통해 반복한다.
[1, 5, 4, 6, 2, 1, 3, 7]

[1 5 4 6 2 1 3 7]
idx 0~7
0~7
mid = 3
0부터 리스트 탐색
[1 5 4 6 2 1 3 7]
탐색하며 최대-최소값을 mid보다 클 때 까지 탐색하고 mid보다 크지않은 인덱스 반환
1 = 0
1 5  = 4 -> mid 보다 크다, 이전까지를 한 구간으로 설정
[1] [5 4 6 2 1 3 7]
5 = 0
5 4 = 1
5 4 6 = 2
5 4 6 2 = 4 mid보다 큰 경우, 따라서 [5,4,6]를 구간으로 지정
[1] [5 4 6] [2 1 3 7]
2  = 0
2 1 = 1
2 1 3 = 2
2 1 3 7 = 5, mid 초과, [2,1,3]으로 구간 설정
[1][5 4 6][2 1 3][7] -> 구간의 수가 m인 3 초과

left : right = 0 : 7 에서
mid = (mid + 7) // 2로 변경

해당 방식으로 이분탐색을 진행해보자
'''
import sys
def input(): return sys.stdin.readline().rstrip()

def is_possible(mid):
    count = 1
    min_n = float('inf')
    max_n = float('-inf')
    
    i = 0
    while i < n:
        min_n = min(min_n, arr[i])
        max_n = max(max_n, arr[i])
        if max_n - min_n > mid:
            count += 1
            max_n = float('-inf')
            min_n = float('inf')
            i -= 1
        i += 1
    return count

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    left, right = 0, max(arr)
    while left < right:
        mid = (left + right)//2
        if is_possible(mid) <= m:
            right = mid
        else:
            left = mid + 1
    print(right)
        