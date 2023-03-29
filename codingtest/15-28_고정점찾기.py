# # 아마존 인터뷰

# 고정점이란 수열의 원소 중에서 그 값 ㅣ인덱스와 동일한 원소를 의미합니다.
# 예를 들어 수열 a = {-15, -4, 2, 8, 13} 이 있을 때 a[2] = 2 이므로 고정점은 2가 됩니다.
# 하나의 수열이 N개의 서로 다을 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있습니다.
# 이떄 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하세요. 고정점은 최대 1개만 존재합나디.
# 만약 고정점이 없다면 -1을 출력합니다.

# 입력 조건
#     첫째 줄에 N이 입력됩니다.
#     둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다.
#     (-1e9 <= 각 원소의 값 <= 1e9)

# 출력 조건
#     고정점을 출력하고, 없으면 -1 출력
    
# 입력 에시 1
    # 5
    # -15 -6 1 3 7

# 츨력 예시 1
#     3


# 5
# -15 -6 1 3 7


n = int(input())

line = list(map(int, input().split()))


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
    
    
def binary_serarch(array,start, end):
 
    if start > end:
        return None
    
    mid = (start + end)//2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_serarch(array,start,mid-1)
    elif array[mid] < mid:
        return binary_serarch(array,mid+1, end)
        
result = binary_serarch(line, 0 ,len(line))
if result == None:
    print(-1)
else:
    print(result)