# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 
# 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
# 예를 들어 수열 [1,1,2,2,2,2,3]이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.


# 입력조건
#     첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다.
#     (1 <= N <= 1000000), (-10^9 <= x <= 10^9)
#     둘째 줄에 N개의 우너소가 정수 형태로 공백으로 구분되어 입력됩니다.

# 출력조건
#     수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다.
#     단 값이 x인 원소가 하나도 없다면 -1을 출력합니다.

# 입력 예시 1
#     7 2
#     1 1 2 2 2 3

# 출력 예시 1
#     4
    
# 입력 예시 2
#     7 4
#     1 1 2 2 2 2 3
    

# # 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
# def count_by_value(array, x):
#     # 데이터의 개수
#     n = len(array)
    
#     # x가 처음 등장한 인덱스 계산
#     a = first(array, x, 0, n-1)
    
#     # 수열에 x가 조재하지 않는 경우
#     if a == None:
#         return 0 # 값이 x인 
    
#     # x가 마지막으로 등장한 인덱스 계산
#     b = last(array, x, 0, n - 1)
    
#     # 개수를 반환
#     return b - a + 1

# # 처음 위치를 찾는 이진 탐색 메서드
# def first(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 해당 값을 가지는 원소중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
#     if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
#         return mid
#     # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
#     elif array[mid] >= target:
#         return first(array, target, start ,mid - 1)
#     # 중간점의 값 보다 찾고자 하는 값이 큰 경우 올느쪽 화긴
#     else:
#         return first(array, target, mid + 1, end)
    
    
# # 마지막 위치를 찾ㅈ는 이진 탐색 메서드
# def last(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 해당 값을 가지는 원소중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
#     if (mid == n-1 or target <  array[mid + 1]) and array[mid] == target:
#         return mid
#     # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
#     elif array[mid] > target:
#         return last(array, target, start ,mid - 1)
#     # 중간점의 값 보다 찾고자 하는 값이 큰 경우 올느쪽 화긴
#     else:
#         return last(array, target, mid + 1, end)
    
    
# https://heytech.tistory.com/79
from bisect import bisect_left, bisect_right
# 값이 [left_alue, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())

line = list(map(int, input().split()))
    
count = count_by_range(line, x, x)

if count == 0:
    print(-1)
else:
    print(count)